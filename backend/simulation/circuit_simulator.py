import numpy as np
import matplotlib.pyplot as plt

class CircuitSimulator:
    def __init__(self, circuit_parameters):
        self.parameters = circuit_parameters
        self.time = np.linspace(0, 1, 1000)  # Simulation time from 0 to 1 second
        self.voltage = np.zeros_like(self.time)
        self.current = np.zeros_like(self.time)

    def simulate(self):
        # Simple simulation logic for a PFC circuit
        for i, t in enumerate(self.time):
            self.voltage[i] = self.parameters['input_voltage'] * np.sin(2 * np.pi * self.parameters['frequency'] * t)
            self.current[i] = self.voltage[i] / self.parameters['load_resistance']

    def plot_results(self):
        plt.figure(figsize=(12, 6))
        plt.subplot(2, 1, 1)
        plt.plot(self.time, self.voltage, label='Voltage (V)')
        plt.title('Circuit Voltage Over Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Voltage (V)')
        plt.grid()
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.plot(self.time, self.current, label='Current (A)', color='orange')
        plt.title('Circuit Current Over Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Current (A)')
        plt.grid()
        plt.legend()

        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    circuit_params = {
        'input_voltage': 230,  # Input voltage in volts
        'frequency': 50,       # Frequency in Hz
        'load_resistance': 10   # Load resistance in ohms
    }
    
    simulator = CircuitSimulator(circuit_params)
    simulator.simulate()
    simulator.plot_results()