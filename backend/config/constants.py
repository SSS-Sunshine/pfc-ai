# Constants for PFC AI Optimization

# Define constants for the PFC AI optimization project
# These constants can be used throughout the backend application to maintain consistency

# AI model parameters
AI_MODEL_PATH = "backend/ai/models/"
AI_TRAINING_EPOCHS = 100
AI_BATCH_SIZE = 32
AI_LEARNING_RATE = 0.001

# Simulation parameters
SIMULATION_TIME_STEP = 0.01  # seconds
SIMULATION_MAX_TIME = 10.0  # seconds

# PFC circuit parameters
PFC_VOLTAGE = 400  # Volts
PFC_CURRENT = 10  # Amperes
PFC_FREQUENCY = 100e3  # Hz

# Buck circuit parameters
BUCK_VOLTAGE = 24  # Volts
BUCK_CURRENT = 5  # Amperes
BUCK_FREQUENCY = 50e3  # Hz

# Logging configuration
LOGGING_LEVEL = "DEBUG"
LOGGING_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

# Other constants
MAX_LOAD = 1.5  # Maximum load factor
MIN_LOAD = 0.1  # Minimum load factor
