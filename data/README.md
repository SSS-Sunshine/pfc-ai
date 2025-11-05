## 数据生成方案

以下是三个关键数据文件的生成代码和格式说明：

### 1. PFC/Buck参数训练数据集

用于model_exploration.ipynb的训练数据：

```python
# 生成PFC和Buck电路训练数据集
import pandas as pd
import numpy as np
import os

# 确保目录存在
os.makedirs('../data/training', exist_ok=True)

# 设置随机种子
np.random.seed(42)

# 样本数量
n_samples = 5000

# 生成PFC电路特征
data = {
    # 输入条件
    'input_voltage': np.random.uniform(176, 265, n_samples),  # 输入电压范围176-265V
    'load_current': np.random.uniform(0.1, 8.25, n_samples),  # 负载电流范围(对应10%-100%负载)
    'ambient_temp': np.random.uniform(25, 55, n_samples),     # 环境温度
  
    # 电路参数
    'inductor_value': np.random.uniform(100e-6, 500e-6, n_samples),  # 电感值
    'capacitor_value': np.random.uniform(100e-6, 1000e-6, n_samples), # 电容值
    'switching_freq': np.random.uniform(70e3, 120e3, n_samples),  # 开关频率
  
    # 控制参数
    'kp': np.random.uniform(0.01, 0.5, n_samples),  # 比例系数
    'ki': np.random.uniform(1, 100, n_samples),     # 积分系数
    'kd': np.random.uniform(0, 0.01, n_samples),    # 微分系数
    'zbf': np.random.uniform(0, 1, n_samples),      # 过零检测阈值
    'compval': np.random.uniform(0, 0.2, n_samples) # 补偿值
}

# 创建数据框
df = pd.DataFrame(data)

# 生成目标变量(效率)，模拟轻载效率低问题
df['target_variable'] = 0.9 + 0.08 * (1 - np.exp(-df['load_current'] / 2)) \
                        - 0.01 * np.random.random(n_samples) \
                        - 0.02 * np.abs(df['kp'] - 0.25) / 0.25 \
                        - 0.02 * np.abs(df['inductor_value'] - 300e-6) / 300e-6

# 保存到CSV
df.to_csv('../data/training/pfc_buck_data.csv', index=False)
print("训练数据集已生成: ../data/training/pfc_buck_data.csv")
```

### 2. PFC仿真结果数据

用于simulation_analysis.ipynb的PFC波形数据：

```python
import pandas as pd
import numpy as np
import os

# 确保目录存在
os.makedirs('../data/simulation_results', exist_ok=True)

# 设置参数
sampling_rate = 10000  # 采样率
duration = 0.05        # 持续时间(秒)
line_freq = 50         # 电网频率
switching_freq = 100e3 # 开关频率

# 创建时间点
time = np.linspace(0, duration, int(sampling_rate * duration))

# 正常工作仿真波形(含参数坐标)
voltage = 400 + 5 * np.sin(2 * np.pi * line_freq * 2 * time)  # 输出电压(含纹波)
current = np.zeros_like(time)

# 模拟TCM模式下的电流(三角波+整流后的正弦包络)
for i, t in enumerate(time):
    envelope = 8 * np.abs(np.sin(2 * np.pi * line_freq * t))  # 电流包络
    triangle_period = 1/switching_freq
    triangle_phase = (t % triangle_period) / triangle_period
  
    if triangle_phase < 0.5:
        current[i] = envelope * (2 * triangle_phase)
    else:
        current[i] = envelope * (2 - 2 * triangle_phase)

# 模拟轻载工况数据(20%负载)
light_load_start = int(sampling_rate * 0.015)
light_load_end = int(sampling_rate * 0.025)
current[light_load_start:light_load_end] *= 0.2

# 模拟负载阶跃(50%→100%)
step_change_idx = int(sampling_rate * 0.03) 
current[step_change_idx:] *= 2.0
voltage[step_change_idx:step_change_idx+50] -= 20  # 电压短暂下降
voltage[step_change_idx+50:] += 2  # 电压回升后稍高

# 创建数据帧
pfc_results = pd.DataFrame({
    'time': time,
    'voltage': voltage,
    'current': current,
    'power': voltage * current,
    'efficiency': 0.9 + 0.08 * (1 - np.exp(-current/2))  # 效率随电流增大而提高
})

# 保存到CSV
pfc_results.to_csv('../data/simulation_results/pfc_simulation.csv', index=False)
print("PFC仿真数据已生成: ../data/simulation_results/pfc_simulation.csv")
```

### 3. Buck仿真结果数据

用于simulation_analysis.ipynb的Buck转换器波形数据：

```python
import pandas as pd
import numpy as np
import os

# 确保目录存在
os.makedirs('../data/simulation_results', exist_ok=True)

# 设置参数
sampling_rate = 10000  # 采样率
duration = 0.01        # 持续时间(秒)
switching_freq = 500e3 # 开关频率

# 创建时间点
time = np.linspace(0, duration, int(sampling_rate * duration))

# 输出电压(稳定在12V，含纹波)
voltage = 12 + 0.2 * np.sin(2 * np.pi * switching_freq * time) * np.exp(-time/0.002)

# 模拟交错并联Buck的电流
current1 = 20 + 5 * np.sin(2 * np.pi * switching_freq * time)
current2 = 20 + 5 * np.sin(2 * np.pi * switching_freq * (time + 0.5/switching_freq))
current = current1 + current2  # 总电流

# 模拟负载阶跃
step_idx = int(sampling_rate * 0.005)
current[step_idx:] *= 1.5
voltage[step_idx:step_idx+20] -= 0.5  # 电压短暂下降
voltage[step_idx+20:] += 0.1  # 电压稳定在新水平

# 创建数据帧
buck_results = pd.DataFrame({
    'time': time,
    'voltage': voltage,
    'current': current,
    'current_phase1': current1,
    'current_phase2': current2,
    'power': voltage * current,
    'efficiency': 0.94 - 0.02 * np.exp(-current/10)  # 效率随负载变化
})

# 保存到CSV
buck_results.to_csv('../data/simulation_results/buck_simulation.csv', index=False)
print("Buck仿真数据已生成: ../data/simulation_results/buck_simulation.csv")
```

## 数据详细说明

### 1. 参数训练数据集 (`pfc_buck_data.csv`)

这个数据集模拟了PFC电路的各项参数及其效率表现：

- **输入特征列**:

  - `input_voltage` - 输入电压(176-265V)
  - `load_current` - 负载电流(0.1-8.25A)
  - `ambient_temp` - 环境温度(25-55°C)
  - `inductor_value` - 电感值(100-500μH)
  - `capacitor_value` - 电容值(100-1000μF)
  - `switching_freq` - 开关频率(70-120kHz)
  - `kp`, `ki`, `kd` - PID控制参数
  - `zbf` - 过零检测阈值
  - `compval` - 补偿值
- **目标变量**:

  - `target_variable` - 电路效率，特意模拟了轻载效率低的特性

### 2. 仿真结果数据 (`pfc_simulation.csv` & `buck_simulation.csv`)

这两个文件包含了电路运行时的波形数据：

- **PFC仿真数据**:

  - 模拟了TCM模式下的三角形电流波形
  - 包含正常工作、轻载和负载阶跃响应
  - 清晰展示轻载状态下效率下降问题
- **Buck仿真数据**:

  - 模拟了交错并联Buck转换器波形
  - 包含相位错开的两路电流
  - 展示了负载阶跃时的动态响应特性

## 使用方法

1. 将以上三段代码保存为Python脚本并运行，或直接在Jupyter中执行
2. 生成的数据将自动保存到正确位置
3. 运行model_exploration.ipynb和simulation_analysis.ipynb进行分析

可以灵活调整参数范围和特性，真实模拟电路在各种条件下的表现，特别是重点关注的轻载效率低和动态响应延迟问题。
