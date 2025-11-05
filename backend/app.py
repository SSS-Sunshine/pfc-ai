import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from api.routes import api_bp
import threading
import time
import random

app = Flask(__name__)

# CORS配置
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:3000", "http://127.0.0.1:3000", "http://192.168.31.42:3000"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    }
})

# 初始化SocketIO
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

# 注册API蓝图
app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the PFC AI Optimization Backend!",
        "status": "running",
        "version": "1.0.0"
    })

# WebSocket事件处理
@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('status', {'message': 'Connected to PFC optimization server'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('start_optimization')
def handle_start_optimization(data):
    print(f'Starting optimization with data: {data}')
    # 启动优化进程
    start_optimization_process(data)

@socketio.on('request_thermal_data')
def handle_thermal_request():
    # 发送实时热数据
    send_thermal_data()

# 优化进程模拟
def start_optimization_process(params):
    def optimization_worker():
        for progress in range(0, 101, 5):
            time.sleep(0.5)  # 模拟计算时间
            socketio.emit('optimization_progress', {
                'progress': progress,
                'status': 'running' if progress < 100 else 'completed',
                'currentStep': f'Step {progress//20 + 1}',
                'estimatedTime': max(0, (100-progress) * 0.5)
            })
            
            if progress == 100:
                # 发送优化完成结果
                socketio.emit('optimization_complete', {
                    'results': {
                        'efficiency': 97.8,
                        'thd': 1.9,
                        'powerFactor': 0.99,
                        'peakTemp': 65
                    }
                })
    
    thread = threading.Thread(target=optimization_worker)
    thread.start()

# 热数据推送
def send_thermal_data():
    def thermal_worker():
        while True:
            thermal_data = {
                'timestamp': time.time(),
                'mosfetTemp': 65 + random.uniform(-5, 15),
                'inductorTemp': 55 + random.uniform(-3, 8),
                'diodeTemp': 60 + random.uniform(-4, 10),
                'controllerTemp': 40 + random.uniform(-2, 5),
                'ambientTemp': 25 + random.uniform(-1, 2)
            }
            socketio.emit('thermal_update', thermal_data)
            time.sleep(2)  # 每2秒推送一次数据
    
    thread = threading.Thread(target=thermal_worker, daemon=True)
    thread.start()

if __name__ == '__main__':
    # 启动热数据推送
    send_thermal_data()
    # 启动服务器
    socketio.run(app, debug=True, host='0.0.0.0', port=3001)