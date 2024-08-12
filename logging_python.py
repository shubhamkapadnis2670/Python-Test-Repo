import logging
import os
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_folder = "logs"
log_file = "running_log.log"
os.makedirs(log_folder,exist_ok=True)

logging.basicConfig(

level = logging.INFO,
format = logging_str,
handlers = [logging.FileHandler(log_file)]
)
logger = logging.getLogger()






def add_number(a, b):
    out = a + b
    logger.info('executed successfully')
    return out



num = add_number(3,4)