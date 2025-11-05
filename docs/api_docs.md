# API Documentation for PFC AI Optimization Project

## Overview

This document provides an overview of the API endpoints available in the PFC AI Optimization project. The API is designed to facilitate communication between the frontend and backend components of the application, enabling efficient data exchange and control of the PFC and Buck circuit models.

## Base URL

The base URL for the API is:

```
http://localhost:5000/api
```

## Endpoints

### 1. Get PFC Model Parameters

- **Endpoint:** `/pfc/parameters`
- **Method:** `GET`
- **Description:** Retrieves the current parameters of the PFC model.
- **Response:**
  - **200 OK**
    ```json
    {
      "parameters": {
        "input_voltage": 400,
        "output_voltage": 200,
        "switching_frequency": 100000,
        "efficiency": 95
      }
    }
    ```

### 2. Update PFC Model Parameters

- **Endpoint:** `/pfc/parameters`
- **Method:** `POST`
- **Description:** Updates the parameters of the PFC model.
- **Request Body:**
  ```json
  {
    "input_voltage": 400,
    "output_voltage": 200,
    "switching_frequency": 100000
  }
  ```
- **Response:**
  - **200 OK**
    ```json
    {
      "message": "Parameters updated successfully."
    }
    ```

### 3. Run Simulation

- **Endpoint:** `/simulation/run`
- **Method:** `POST`
- **Description:** Initiates a simulation based on the current model parameters.
- **Request Body:**
  ```json
  {
    "simulation_type": "transient",
    "duration": 10
  }
  ```
- **Response:**
  - **202 Accepted**
    ```json
    {
      "message": "Simulation is running."
    }
    ```

### 4. Get Simulation Results

- **Endpoint:** `/simulation/results`
- **Method:** `GET`
- **Description:** Retrieves the results of the last simulation run.
- **Response:**
  - **200 OK**
    ```json
    {
      "results": {
        "time": [0, 1, 2, 3, 4, 5],
        "voltage": [0, 50, 100, 150, 200, 200],
        "current": [0, 10, 20, 30, 40, 50]
      }
    }
    ```

### 5. Fault Injection

- **Endpoint:** `/fault/inject`
- **Method:** `POST`
- **Description:** Simulates a fault condition in the circuit.
- **Request Body:**
  ```json
  {
    "fault_type": "over_voltage",
    "duration": 5
  }
  ```
- **Response:**
  - **200 OK**
    ```json
    {
      "message": "Fault injected successfully."
    }
    ```

## Conclusion

This API documentation outlines the key endpoints available for interacting with the PFC AI Optimization project. For further details on usage and examples, please refer to the user guide.