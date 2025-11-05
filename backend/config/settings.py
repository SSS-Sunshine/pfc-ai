# settings.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    DEBUG = os.environ.get('DEBUG', 'False').lower() in ['true', '1']
    HOST =  '0.0.0.0'
    PORT = 3001
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///site.db'
    AI_MODEL_PATH = os.environ.get('AI_MODEL_PATH') or 'backend/ai/models/'
    SIMULATION_RESULTS_PATH = os.environ.get('SIMULATION_RESULTS_PATH') or 'data/simulation_results/'
    TRAINING_DATA_PATH = os.environ.get('TRAINING_DATA_PATH') or 'data/training/'

# You can add more configuration options as needed.