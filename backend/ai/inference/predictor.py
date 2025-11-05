import numpy as np
import joblib

class Predictor:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, input_data):
        """
        Predict the output based on the input data.

        Parameters:
        input_data (array-like): The input features for prediction.

        Returns:
        array: The predicted output.
        """
        input_data = np.array(input_data).reshape(1, -1)  # Reshape for a single sample
        prediction = self.model.predict(input_data)
        return prediction

    def evaluate(self, input_data, true_output):
        """
        Evaluate the model's predictions against the true output.

        Parameters:
        input_data (array-like): The input features for prediction.
        true_output (array-like): The true output for comparison.

        Returns:
        float: The mean squared error of the predictions.
        """
        predictions = self.predict(input_data)
        mse = np.mean((predictions - true_output) ** 2)
        return mse

# Example usage:
# predictor = Predictor('path/to/your/model.pkl')
# prediction = predictor.predict([feature1, feature2, feature3, ...])
# mse = predictor.evaluate([feature1, feature2, feature3, ...], true_value)