# 用户指南

欢迎使用PFC AI优化项目！本指南旨在帮助用户理解如何使用本项目的功能，特别是在图腾柱PFC电路和交错并联Buck电路的设计环节中应用人工智能技术。

## 1. 项目概述

本项目旨在通过人工智能技术优化图腾柱PFC电路和交错并联Buck电路的设计。我们提供了一套具有人机交互界面的AI算法，用户可以通过该界面实时调整参数，进行动态拓扑渲染，并观察波形对比。

## 2. 系统要求

- Python 3.7或更高版本
- Node.js 12或更高版本
- 安装所需的Python库（请参阅`backend/requirements.txt`）
- 安装前端依赖（请参阅`frontend/package.json`）

## 3. 安装与配置

1. **克隆项目**：
   ```
   git clone <项目仓库地址>
   cd pfc-ai-optimization
   ```

2. **后端安装**：
   ```
   cd backend
   pip install -r requirements.txt
   ```

3. **前端安装**：
   ```
   cd frontend
   npm install
   ```

4. **配置设置**：
   根据需要修改`backend/config/settings.py`中的配置。

## 4. 启动项目

1. **启动后端**：
   ```
   cd backend
   python app.py
   ```

2. **启动前端**：
   ```
   cd frontend
   npm start
   ```

3. 打开浏览器，访问 `http://localhost:3000`。

## 5. 使用功能

### 5.1 拓扑实验室

在拓扑实验室页面，用户可以进行动态拓扑渲染，实时调整电路参数，并观察波形变化。

### 5.2 数字孪生调试台

用户可以在数字孪生调试台页面进行器件级参数调整，模拟故障注入，并查看热力学分布云图。

### 5.3 AI优化

在AI优化页面，用户可以利用AI算法进行电路设计优化，提升动态响应和轻载效率。

## 6. 贡献

我们欢迎社区的贡献！请遵循以下步骤：

1. Fork本项目。
2. 创建功能分支 (`git checkout -b feature/YourFeature`)。
3. 提交更改 (`git commit -m 'Add some feature'`)。
4. 推送到分支 (`git push origin feature/YourFeature`)。
5. 创建拉取请求。

## 7. 联系我们

如有任何问题或建议，请通过以下方式与我们联系：

- 邮箱：support@example.com
- GitHub Issues：在项目页面提交问题

感谢您使用PFC AI优化项目！希望您能在电力电子设计中获得更好的体验与成果。