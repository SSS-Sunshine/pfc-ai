import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

class PFCModelTrainer:
    def __init__(self, data_path):
        self.data_path = data_path
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)

    def load_data(self):
        data = pd.read_csv(self.data_path)
        X = data.drop('target', axis=1)
        y = data['target']
        return X, y

    def preprocess_data(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test

    def train_model(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def evaluate_model(self, X_test, y_test):
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f'Model Mean Squared Error: {mse}')

    def save_model(self, model_path):
        joblib.dump(self.model, model_path)

    def run(self, model_path):
        X, y = self.load_data()
        X_train, X_test, y_train, y_test = self.preprocess_data(X, y)
        self.train_model(X_train, y_train)
        self.evaluate_model(X_test, y_test)
        self.save_model(model_path)

if __name__ == "__main__":
    trainer = PFCModelTrainer(data_path='path/to/your/data.csv')
    trainer.run(model_path='path/to/save/model.pkl')