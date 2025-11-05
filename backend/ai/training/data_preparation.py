import os
import pandas as pd
from sklearn.model_selection import train_test_split

def prepare_data(data_directory, test_size=0.2, random_state=42):
    """
    Prepare the dataset for training by loading, cleaning, and splitting the data.

    Parameters:
    - data_directory: str, path to the directory containing the dataset files
    - test_size: float, proportion of the dataset to include in the test split
    - random_state: int, random seed for reproducibility

    Returns:
    - X_train: DataFrame, training features
    - X_test: DataFrame, testing features
    - y_train: Series, training labels
    - y_test: Series, testing labels
    """
    # Load data
    data_files = [f for f in os.listdir(data_directory) if f.endswith('.csv')]
    data_frames = [pd.read_csv(os.path.join(data_directory, f)) for f in data_files]
    full_data = pd.concat(data_frames, ignore_index=True)

    # Data cleaning (example: drop rows with missing values)
    full_data.dropna(inplace=True)

    # Split features and labels
    X = full_data.drop('target', axis=1)  # Assuming 'target' is the label column
    y = full_data['target']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    data_dir = "path/to/your/data"  # Update this path
    X_train, X_test, y_train, y_test = prepare_data(data_dir)
    print("Data preparation complete. Training and testing sets are ready.")