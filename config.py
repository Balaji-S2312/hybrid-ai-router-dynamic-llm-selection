import os
from dotenv import load_dotenv

load_dotenv()

# Router Thresholds
LOCAL_THRESHOLD = 30
REMOTE_THRESHOLD = 70

# Confidence Threshold
CONFIDENCE_THRESHOLD = 0.60

# Models
LOCAL_MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"
REMOTE_MODEL_NAME = "fireworks"

# Logging
LOG_FILE = "router_logs.jsonl"

# Token Limits
MAX_LOCAL_INPUT_TOKENS = 256
MAX_LOCAL_OUTPUT_TOKENS = 512

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama-3.1-8b-instant"
# Fireworks Configuration
FIREWORKS_API_KEY = os.getenv("FIREWORKS_API_KEY")
FIREWORKS_MODEL = "accounts/fireworks/models/qwen3-8b"