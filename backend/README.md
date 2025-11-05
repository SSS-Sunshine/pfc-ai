# pfc-ai-optimization Backend Documentation

## Overview

The pfc-ai-optimization project aims to enhance the design and performance of PFC (Power Factor Correction) circuits and interleaved Buck converters using artificial intelligence techniques. This backend component serves as the core of the application, providing APIs, models, and AI functionalities to support the frontend interface.

## Project Structure

- **api/**: Contains the API routes and endpoints for handling requests.
  - `routes.py`: Defines the routes for the API.
  - `endpoints.py`: Implements the specific API endpoints.

- **models/**: Contains the definitions of circuit models.
  - `pfc_model.py`: Defines the PFC circuit model.
  - `buck_model.py`: Defines the Buck converter model.

- **ai/**: Contains AI-related functionalities.
  - **training/**: Handles data preparation and model training.
    - `data_preparation.py`: Prepares data for training.
    - `model_training.py`: Implements the model training process.
  - **inference/**: Handles model inference.
    - `predictor.py`: Used for making predictions with the trained model.
  - **models/**: Contains AI models.
    - `reinforcement_learning.py`: Implements reinforcement learning algorithms.
    - `neural_network.py`: Implements neural network models.

- **simulation/**: Contains simulation tools for circuit behavior and thermal analysis.
  - `circuit_simulator.py`: Simulates the behavior of the circuit.
  - `thermal_simulator.py`: Simulates thermal behavior.
  - `matlab_bridge.py`: Implements a bridge for MATLAB integration.

- **device_models/**: Contains models for specific devices.
  - `sic_mosfet.py`: Defines the SiC MOSFET model.

- **config/**: Contains configuration settings and constants.
  - `settings.py`: Configuration settings for the application.
  - `constants.py`: Defines constants used throughout the application.

- `app.py`: The entry point for the backend application, starting the Flask server.
- `requirements.txt`: Lists the dependencies required for the backend project.
- `README.md`: Documentation for the backend project.

## Getting Started

1. **Clone the Repository**: 
   ```
   git clone <repository-url>
   cd pfc-ai-optimization/backend
   ```

2. **Install Dependencies**: 
   ```
   pip install -r requirements.txt
   ```

3. **Run the Application**: 
   ```
   python app.py
   ```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is open-source and available under the MIT License.