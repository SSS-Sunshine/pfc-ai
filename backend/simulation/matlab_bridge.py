import numpy as np
import scipy.io
import matlab.engine

class MatlabBridge:
    def __init__(self):
        self.eng = matlab.engine.start_matlab()

    def run_simulation(self, parameters):
        """
        Run the MATLAB simulation with the given parameters.

        :param parameters: A dictionary of parameters to pass to the MATLAB function.
        :return: The results from the MATLAB simulation.
        """
        # Convert parameters to MATLAB struct
        matlab_params = matlab.struct(parameters)
        results = self.eng.run_simulation(matlab_params)
        return results

    def load_results(self, file_path):
        """
        Load simulation results from a .mat file.

        :param file_path: Path to the .mat file.
        :return: Loaded data from the .mat file.
        """
        data = scipy.io.loadmat(file_path)
        return data

    def close(self):
        """
        Close the MATLAB engine.
        """
        self.eng.quit()