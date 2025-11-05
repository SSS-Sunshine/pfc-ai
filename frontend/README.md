# PFC电路AI优化平台前端项目详细说明

## 项目概述

这是一个基于React的PFC（功率因数校正）电路AI优化平台前端应用，主要用于图腾柱PFC电路和交错并联Buck电路的智能设计与优化。该平台提供了交互式界面，包括拓扑渲染、参数调节、数字孪生仿真等功能。

## 项目入口文件

### 1. 主入口文件
```
src/index.jsx
```
这是整个React应用的入口点，负责将主组件渲染到DOM中：

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

### 2. 应用主组件
```
src/App.jsx
```
负责路由配置和整体布局管理：

```jsx
function App() {
  return (
    <BrowserRouter>
      <div className="app-wrapper">
        <Sidebar />
        <div className="content-wrapper">
          <Header />
          <div className="main-content-area">
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/topology-lab" element={<TopologyLabPage />} />
              <Route path="/ai-optimization" element={<AIOptimizationPage />} />
            </Routes>
          </div>
          <Footer />
        </div>
      </div>
    </BrowserRouter>
  );
}
```

## 核心页面组件

### 1. **仪表盘页面** (Dashboard.jsx)
- 系统状态概览
- 效率对比图表
- 温度分布图表
- 最近优化历史
- 快捷操作入口

### 2. **拓扑实验室页面** (TopologyLabPage.jsx)
- 3D拓扑结构渲染
- 实时参数调节面板
- 电路仿真功能
- 波形分析对比
- AI优化参数跳转

### 3. **AI优化页面** (AIOptimizationPage.jsx)
- 电路拓扑选择
- 优化目标设定
- 参数配置界面
- 算法设置
- 优化进度监控
- 结果对比展示

## 后端接口配置

### 1. API配置文件
```
src/services/api.js
```

这是后端接口调用的核心配置文件，包含：

#### API基础配置：
```javascript
// API基础URL配置
const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:3001/api';

// 创建axios实例
const apiClient = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});
```

#### 主要API接口：

1. **系统状态接口**
```javascript
export const getSystemStatus = async () => {
    const response = await apiClient.get('/system/status');
    return response.data;
};
```

2. **拓扑数据接口**
```javascript
export const fetchTopologyData = async (topologyType) => {
    const response = await apiClient.get(`/topology/${topologyType}`);
    return response.data;
};
```

3. **电路仿真接口**
```javascript
export const simulateCircuit = async (params) => {
    const response = await apiClient.post('/simulation/run', params);
    return response.data;
};
```

4. **AI优化接口**
```javascript
export const runAIOptimization = async (params) => {
    const response = await apiClient.post('/ai/optimize', params);
    return response.data;
};
```

5. **热分布数据接口**
```javascript
export const fetchThermalData = async () => {
    const response = await apiClient.get('/thermal/data');
    return response.data;
};
```

### 2. 环境变量配置

在项目根目录创建 `.env` 文件配置后端地址：

```env
REACT_APP_API_BASE_URL=http://localhost:3001/api
```

### 3. WebSocket服务配置
```
src/services/socketService.js
```

用于实时数据通信：

```javascript
const SOCKET_SERVER_URL = 'http://localhost:4000';

class SocketService {
    connect() {
        this.socket = io(SOCKET_SERVER_URL);
    }
    
    on(event, callback) {
        if (this.socket) {
            this.socket.on(event, callback);
        }
    }
}
```

## 组件架构说明

### 1. **通用组件** (`src/components/common/`)
- Header.jsx: 顶部导航栏
- Sidebar.jsx: 侧边导航菜单
- `Footer.jsx`: 底部信息栏
- UIComponents.jsx: 通用UI组件（按钮、选项卡、工具提示等）

### 2. **拓扑实验室组件** (`src/components/TopologyLab/`)
- `Renderer3D.jsx`: 3D拓扑结构渲染器
- `ParameterPanel.jsx`: 参数调节面板
- `WaveformCanvas.jsx`: 波形画布组件

### 3. **AI优化组件** (`src/components/AIOptimization/`)
- `CircuitTopologySelector.jsx`: 电路拓扑选择器
- `OptimizationProgress.jsx`: 优化进度显示
- `WaveformComparison.jsx`: 波形对比组件
- ParameterConfig.jsx: 参数配置组件

### 4. **数字孪生组件** (`src/components/DigitalTwin/`)
- `ThermalMap.jsx`: 热分布图组件
- `DeviceParameters.jsx`: 设备参数组件
- `FaultInjector.jsx`: 故障注入组件

## 启动和开发流程

### 1. 环境准备
```bash
# 进入前端目录
cd pfc-ai-optimization/frontend

# 安装依赖
npm install
```

### 2. 启动开发服务器
```bash
# 启动前端开发服务器（默认端口3000）
npm start
```

### 3. 构建生产版本
```bash
# 构建生产版本
npm run build
```

## 样式和主题配置

### 1. 全局样式
```
src/index.css
```
定义了CSS变量、基础重置样式和通用工具类：

```css
:root {
  --color-primary: #1e40af;
  --color-text: #1e293b;
  --color-background: #f8fafc;
  --spacing-md: 16px;
  --radius-md: 8px;
}
```

### 2. 组件样式
每个组件都有对应的CSS文件，采用模块化样式管理。

## 数据流和状态管理

项目使用React Hooks进行状态管理，主要包括：

- `useState`: 组件局部状态
- `useEffect`: 副作用处理（API调用、数据加载）
- `useCallback`: 函数缓存优化
- `useLocation`: 路由信息获取

## 开发建议

1. **从仪表盘页面开始**: 这是用户的主要入口点
2. **关注API接口**: 确保后端服务正常运行在3001端口
3. **样式一致性**: 使用定义好的CSS变量保持设计一致
4. **组件复用**: 优先使用common目录下的通用组件
5. **错误处理**: API调用都包含错误处理和模拟数据回退

这个项目采用现代React开发模式，具有良好的组件化架构和清晰的职责分离，便于维护和扩展。

找到具有 2 个许可证类型的类似代码