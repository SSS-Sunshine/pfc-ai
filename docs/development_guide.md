# Development Guide for PFC AI Optimization Project

## Introduction
This document serves as a development guide for the PFC AI Optimization project, which aims to enhance the design and performance of PFC circuits and interleaved parallel Buck circuits using artificial intelligence techniques. The project includes a frontend interface for user interaction and a backend for processing and model training.

## Project Structure
The project is organized into several key directories:

- **frontend**: Contains the user interface components and pages.
- **backend**: Contains the server-side logic, including API routes, models, and AI algorithms.
- **data**: Holds training data and simulation results.
- **notebooks**: Contains Jupyter notebooks for model exploration and simulation analysis.
- **docs**: Includes documentation files such as API docs, user guides, and this development guide.

## Development Environment Setup

### Prerequisites
- Python 3.x
- Node.js and npm
- Virtual environment (recommended for Python)

### Backend Setup
1. Navigate to the `backend` directory.
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Frontend Setup
1. Navigate to the `frontend` directory.
2. Install the necessary dependencies:
   ```
   npm install
   ```

## Running the Project

### Backend
To start the backend server, run:
```
python app.py
```
The server will be accessible at `http://localhost:5000`.

### Frontend
To start the frontend application, run:
```
npm start
```
The application will be accessible at `http://localhost:3000`.

## AI Algorithm Development
The AI components are located in the `backend/ai` directory. Key files include:
- **training/data_preparation.py**: For preparing training data.
- **training/model_training.py**: For training the AI models.
- **inference/predictor.py**: For making predictions using the trained models.

### Adding New Features
1. Identify the feature to be added.
2. Create a new Python file in the appropriate directory (e.g., `training`, `inference`).
3. Implement the feature and ensure it adheres to the existing code style.
4. Write unit tests to validate the new functionality.

## Contribution Guidelines
- Fork the repository and create a new branch for your feature.
- Ensure your code is well-documented and follows the project's coding standards.
- Submit a pull request for review.

## Conclusion
This development guide provides an overview of the PFC AI Optimization project and instructions for setting up the development environment, running the project, and contributing to its development. For further assistance, please refer to the user guide or contact the project maintainers.