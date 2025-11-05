from flask import Blueprint, jsonify, request
import random
import time
from datetime import datetime

api_bp = Blueprint('api', __name__)

# 系统状态接口
@api_bp.route('/system/status', methods=['GET'])
def get_system_status():
    return jsonify({
        "status": "online",
        "lastUpdated": datetime.now().isoformat(),
        "components": {
            "aiModel": "active",
            "api": "responsive", 
            "database": "connected"
        }
    })

# 获取拓扑数据
@api_bp.route('/topology/<topology_type>', methods=['GET'])
def get_topology_data(topology_type):
    topology_names = {
        'totem-pole-pfc': '图腾柱无桥PFC',
        'bridgeless-pfc': '无桥PFC',
        'interleaved-pfc': '交错并联PFC',
        'buck-converter': 'Buck变换器'
    }
    
    return jsonify({
        "id": topology_type,
        "name": topology_names.get(topology_type, '未知拓扑'),
        "description": "这是一个PFC拓扑结构，用于功率因数校正。",
        "defaultParams": {
            "inductorValue": 0.5,
            "switchingFrequency": 100,
            "dutyCycle": 50,
            "inputVoltage": 220,
            "outputVoltage": 400,
            "loadPower": 1000,
            "temperature": 25
        },
        "modelUrl": f"/models/{topology_type}.glb"
    })

# 运行电路仿真
@api_bp.route('/simulation/run', methods=['POST'])
def run_simulation():
    params = request.get_json()
    
    # 模拟仿真计算
    time.sleep(0.5)  # 模拟计算时间
    
    # 根据参数生成模拟结果
    base_efficiency = 93 + random.uniform(-2, 5)
    thd = 5 - (params.get('inductorValue', 0.5) * 4) + random.uniform(0, 2)
    power_factor = 0.9 + (params.get('inductorValue', 0.5) * 0.1) - random.uniform(0, 0.05)
    peak_temp = 45 + (params.get('loadPower', 1000) / params.get('outputVoltage', 400)) * 10 + random.uniform(0, 5)
    
    return jsonify({
        "metrics": {
            "efficiency": round(base_efficiency, 1),
            "thd": round(thd, 1),
            "powerFactor": round(power_factor, 2),
            "peakTemp": round(peak_temp, 1),
            "simulationTime": random.randint(200, 500)
        },
        "waveforms": {
            "voltage": {
                "labels": [i/100 for i in range(100)],
                "values": [311 * (0.8 + 0.4 * random.random()) for _ in range(100)],
                "reference": [400] * 100
            },
            "current": {
                "labels": [i/100 for i in range(100)],
                "values": [15 * (0.5 + 0.5 * random.random()) for _ in range(100)],
                "reference": [0] * 100
            },
            "switchingSignal": {
                "labels": [i/100 for i in range(100)],
                "values": [15 if i % 10 < 5 else 0 for i in range(100)]
            }
        }
    })

# 保存拓扑设置
@api_bp.route('/topology/settings/save', methods=['POST'])
def save_topology_settings():
    settings = request.get_json()
    
    # 模拟保存操作
    time.sleep(0.2)
    
    return jsonify({
        "success": True,
        "message": "设置已成功保存",
        "timestamp": datetime.now().isoformat()
    })

# 获取AI优化结果
@api_bp.route('/ai/results', methods=['POST'])
def get_ai_results():
    params = request.get_json()
    
    # 模拟AI分析
    time.sleep(1)
    
    return jsonify({
        "before": {
            "efficiency": 93.2,
            "thd": 4.5,
            "powerFactor": 0.95,
            "peakTemp": 75
        },
        "after": {
            "efficiency": 97.8,
            "thd": 1.9,
            "powerFactor": 0.99,
            "peakTemp": 65
        },
        "waveformData": {
            "before": {
                "voltage": [310 * (0.9 + 0.2 * random.random()) for _ in range(100)],
                "current": [10 * (0.8 + 0.4 * random.random()) for _ in range(100)]
            },
            "after": {
                "voltage": [310 * (0.95 + 0.1 * random.random()) for _ in range(100)],
                "current": [10 * (0.9 + 0.2 * random.random()) for _ in range(100)]
            }
        }
    })

# 执行AI优化
@api_bp.route('/ai/optimize', methods=['POST'])
def run_ai_optimization():
    params = request.get_json()
    
    # 模拟优化过程
    task_id = f"task-{int(time.time())}"
    
    return jsonify({
        "success": True,
        "taskId": task_id,
        "message": "AI优化任务已启动",
        "estimatedTime": "2-3分钟"
    })

# 获取热分布数据
@api_bp.route('/thermal/data', methods=['GET'])
def get_thermal_data():
    import datetime
    
    data = []
    now = datetime.datetime.now()
    
    # 生成过去1小时的数据点
    for i in range(12):
        time_point = now - datetime.timedelta(minutes=i*5)
        data.append({
            "time": time_point.strftime("%H:%M"),
            "temperature": 60 + random.uniform(0, 15),
            "mosfetTemp": 65 + random.uniform(0, 20),
            "inductorTemp": 55 + random.uniform(0, 10),
            "diodeTemp": 60 + random.uniform(0, 15),
            "controllerTemp": 40 + random.uniform(0, 5),
            "ambientTemp": 25 + random.uniform(0, 2)
        })
    
    return jsonify(data[::-1])  # 反转列表，最新的在后面

# 错误处理
@api_bp.errorhandler(400)
def bad_request(error):
    return jsonify({
        "error": "Bad Request",
        "message": "请求参数错误"
    }), 400

@api_bp.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Not Found",
        "message": "请求的资源不存在"
    }), 404