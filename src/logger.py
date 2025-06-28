import logging
import os
from datetime import datetime
from src import exception
import sys

# Create folder for logs
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Generate log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Set up logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Run only when file is executed directly
if __name__ == "__main__":
    logging.info("Logging is started")


    try:
        ans = 2/0
    except Exception as e:
        error=exception.custom_exception(e,sys)
        logging.error(error)

