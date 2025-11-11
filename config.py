import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./assistant_swimmer.db')
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
DEBUG = ENVIRONMENT == 'development'

MAX_VIDEO_SIZE_MB = 100
SUPPORTED_VIDEO_FORMATS = ['mp4', 'mov', 'avi', 'mkv']
MAX_VIDEO_DURATION_SECONDS = 300
ANALYSIS_COST_RUB = 300
ANALYSIS_CONFIDENCE_THRESHOLD = 0.7
MEDIAPIPE_MODEL_COMPLEXITY = 1
MIN_DETECTION_CONFIDENCE = 0.7
MIN_TRACKING_CONFIDENCE = 0.7
LOG_LEVEL = 'DEBUG' if DEBUG else 'INFO'
APP_NAME = "Assistant Swimmer Bot"
APP_VERSION = "1.0.0-beta"
