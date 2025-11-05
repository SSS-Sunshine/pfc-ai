from sklearn.neural_network import MLPRegressor
import numpy as np
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'KaiTi', 'FangSong', 'SimSun', 'Arial Unicode MS'] 
plt.rcParams['axes.unicode_minus'] = False  # 解决坐标轴负号显示问题

class PFCModel:
    def __init__(self, hidden_layers=(100, 50), max_iter=1000):
        """
        初始化PFC电路模型
        
        Parameters:
        hidden_layers : tuple
            神经网络隐藏层结构
        max_iter : int
            最大迭代次数
        """
        self.model = MLPRegressor(
            hidden_layer_sizes=hidden_layers, 
            max_iter=max_iter,
            activation='relu',
            solver='adam',
            random_state=42,
            verbose=True
        )
        self.trained = False
        self.scaler_X = StandardScaler()
        self.scaler_y = StandardScaler()

    def train(self, X, y):
        """
        训练PFC模型，使用提供的输入-输出对
        
        Parameters:
        X : np.ndarray
            训练用输入特征
        y : np.ndarray
            训练用目标输出
        """
        # 数据标准化
        X_scaled = self.scaler_X.fit_transform(X)
        y_scaled = self.scaler_y.fit_transform(y.reshape(-1, 1)).ravel()
        
        # 训练模型
        self.model.fit(X_scaled, y_scaled)
        self.trained = True
        
        return self

    def predict(self, X):
        """
        使用给定的输入特征预测输出
        
        Parameters:
        X : np.ndarray
            预测用输入特征
        
        Returns:
        np.ndarray
            预测结果
        """
        if not self.trained:
            raise Exception("必须先训练模型才能进行预测")
        
        # 数据标准化
        X_scaled = self.scaler_X.transform(X)
        
        # 预测并反标准化结果
        y_scaled_pred = self.model.predict(X_scaled)
        return self.scaler_y.inverse_transform(y_scaled_pred.reshape(-1, 1)).ravel()

    def evaluate(self, X, y_true):
        """
        评估模型在测试集上的性能
        
        Parameters:
        X : np.ndarray
            测试用输入特征
        y_true : np.ndarray
            实际目标值
            
        Returns:
        dict
            包含各种评估指标的字典
        """
        y_pred = self.predict(X)
        mse = mean_squared_error(y_true, y_pred)
        r2 = r2_score(y_true, y_pred)
        
        return {
            'mse': mse,
            'rmse': np.sqrt(mse),
            'r2': r2
        }

    def save_model(self, filepath):
        """
        将训练好的模型保存到文件
        
        Parameters:
        filepath : str
            模型保存路径
        """
        # 创建目录（如果不存在）
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # 保存模型
        model_data = {
            'model': self.model,
            'scaler_X': self.scaler_X,
            'scaler_y': self.scaler_y,
            'trained': self.trained
        }
        joblib.dump(model_data, filepath)
        print(f"模型已保存至：{filepath}")

    def load_model(self, filepath):
        """
        从文件加载训练好的模型
        
        Parameters:
        filepath : str
            模型加载路径
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"模型文件不存在：{filepath}")
            
        model_data = joblib.load(filepath)
        self.model = model_data['model']
        self.scaler_X = model_data['scaler_X']
        self.scaler_y = model_data['scaler_y']
        self.trained = model_data['trained']
        print(f"模型已从{filepath}加载")

def visualize_predictions(y_true, y_pred, title="模型预测结果对比"):
    """可视化预测结果"""
    plt.figure(figsize=(10, 6))
    plt.scatter(y_true, y_pred, alpha=0.5)
    
    # 理想预测线
    min_val = min(np.min(y_true), np.min(y_pred))
    max_val = max(np.max(y_true), np.max(y_pred))
    plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei', 'Microsoft YaHei', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot([min_val, max_val], [min_val, max_val], 'r--')
    
    plt.xlabel('实际值')
    plt.ylabel('预测值')
    plt.title(title)
    plt.grid(True)
    plt.savefig('../data/results/prediction_comparison.png')
    plt.show()

def visualize_feature_importance(model, feature_names):
    """可视化特征重要性"""
    try:
        importances = np.abs(model.model.coefs_[0])
        importances = np.mean(importances, axis=1)
        plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei', 'Microsoft YaHei', 'DejaVu Sans']
        plt.rcParams['axes.unicode_minus'] = False
        plt.figure(figsize=(12, 6))
        plt.bar(feature_names, importances)
        plt.xticks(rotation=45, ha='right')
        plt.title('输入参数影响程度')
        plt.tight_layout()
        plt.savefig('../data/results/feature_importance.png')
        plt.show()
    except:
        print("该模型不支持直接提取特征重要性")

def main():
    """主函数：数据加载、模型训练与评估"""
    
    # 确保结果目录存在
    os.makedirs('../data/results', exist_ok=True)
    
    # 加载数据集
    print("加载PFC和Buck电路数据...")
    try:
        data = pd.read_csv('../data/training/pfc_buck_data.csv')
        print(f"成功加载数据，共{len(data)}条记录")
    except Exception as e:
        print(f"数据加载失败: {e}")
        return
    
    print("\n数据预览:")
    print(data.head())
    print("\n数据统计信息:")
    print(data.describe())
    
    # 检查是否存在缺失值
    if data.isnull().sum().any():
        print("\n警告：存在缺失值，正在进行清洗...")
        data.dropna(inplace=True)
        print(f"清洗后剩余{len(data)}条记录")
    
    # 特征选择
    print("\n准备训练数据...")
    features = data.drop('target_variable', axis=1)
    target = data['target_variable']
    feature_names = features.columns.tolist()
    
    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )
    print(f"训练集: {X_train.shape[0]}条记录, 测试集: {X_test.shape[0]}条记录")
    
    # 初始化并训练模型
    print("\n开始训练模型...")
    model = PFCModel(hidden_layers=(100, 80, 50), max_iter=10)
    model.train(X_train.values, y_train.values)
    
    # 评估模型
    print("\n评估模型性能...")
    metrics = model.evaluate(X_test.values, y_test.values)
    print(f"均方误差(MSE): {metrics['mse']:.6f}")
    print(f"均方根误差(RMSE): {metrics['rmse']:.6f}")
    print(f"决定系数(R²): {metrics['r2']:.6f}")
    
    # 可视化预测结果
    print("\n生成预测结果可视化...")
    y_pred = model.predict(X_test.values)
    visualize_predictions(y_test.values, y_pred)
    
    # 尝试可视化特征重要性
    try:
        visualize_feature_importance(model, feature_names)
    except:
        print("无法可视化特征重要性")
    
    # 保存模型
    print("\n保存训练好的模型...")
    model.save_model('../models/trained_pfc_model.pkl')
    
    print("\nPFC模型训练和评估完成！")

if __name__ == "__main__":
    main()