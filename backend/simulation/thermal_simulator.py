import numpy as np
import matplotlib.pyplot as plt

class ThermalSimulator:
    def __init__(self, power_loss, thermal_resistance, ambient_temperature):
        self.power_loss = power_loss  # Power loss in watts
        self.thermal_resistance = thermal_resistance  # Thermal resistance in °C/W
        self.ambient_temperature = ambient_temperature  # Ambient temperature in °C

    def calculate_junction_temperature(self):
        """Calculate the junction temperature based on power loss and thermal resistance."""
        junction_temperature = self.ambient_temperature + (self.power_loss * self.thermal_resistance)
        return junction_temperature

    def plot_temperature_profile(self, time_duration, time_step):
        """Plot the temperature profile over time."""
        time_points = np.arange(0, time_duration, time_step)
        temperatures = [self.calculate_junction_temperature() for _ in time_points]

        plt.figure(figsize=(10, 5))
        plt.plot(time_points, temperatures, label='Junction Temperature', color='red')
        plt.axhline(y=self.ambient_temperature, color='blue', linestyle='--', label='Ambient Temperature')
        plt.title('Junction Temperature Profile')
        plt.xlabel('Time (s)')
        plt.ylabel('Temperature (°C)')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    simulator = ThermalSimulator(power_loss=10, thermal_resistance=1.5, ambient_temperature=25)
    print(f"Calculated Junction Temperature: {simulator.calculate_junction_temperature()} °C")
    simulator.plot_temperature_profile(time_duration=60, time_step=1)