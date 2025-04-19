import os
import sys
import logging

# Define the logging format correctly
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define log directory and file path
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure logging with correct argument names
logging.basicConfig(
    level=logging.INFO,  # ✅ Correct spelling
    format=logging_str,

    handlers=[  # ✅ Correct spelling
        logging.FileHandler(log_filepath),  # Log to file
        logging.StreamHandler(sys.stdout)  # Log to console
    ]
)

# Create logger
logger = logging.getLogger("textSummarizerLogger")

# Example log message to verify it's working
logger.info("Logger is successfully configured!")