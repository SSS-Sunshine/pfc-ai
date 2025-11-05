from sklearn.linear_model import LinearRegression
import numpy as np

class BuckConverterModel:
    def __init__(self):
        self.model = LinearRegression()
        self.trained = False

    def train(self, input_data, output_data):
        """
        Train the Buck Converter model using input and output data.
        
        Parameters:
        input_data (np.array): The input parameters for the Buck converter.
        output_data (np.array): The corresponding output parameters.
        """
        self.model.fit(input_data, output_data)
        self.trained = True

    def predict(self, input_data):
        """
        Predict the output parameters based on input data.
        
        Parameters:
        input_data (np.array): The input parameters for prediction.
        
        Returns:
        np.array: The predicted output parameters.
        """
        if not self.trained:
            raise Exception("Model must be trained before prediction.")
        return self.model.predict(input_data)

    def get_coefficients(self):
        """
        Get the coefficients of the trained model.
        
        Returns:
        np.array: The coefficients of the model.
        """
        if not self.trained:
            raise Exception("Model must be trained to get coefficients.")
        return self.model.coef_

    def get_intercept(self):
        """
        Get the intercept of the trained model.
        
        Returns:
        float: The intercept of the model.
        """
        if not self.trained:
            raise Exception("Model must be trained to get intercept.")
        return self.model.intercept_