import logging
from from_root import from_root
from datetime import datetime
import os

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
log_dir = "logs"
logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

os.makedirs(log_dir, exist_ok=True)



logging.basicConfig(
    filename= logs_path,
    format= "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG)