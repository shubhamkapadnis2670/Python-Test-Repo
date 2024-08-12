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

def division(a,b):
    try:
        return a/b
    except Exception as err:
        logger.error(f'Error occurred {str(err)}')

    finally:
        logger.info('function executed successfully')
    return True

result = division(10,0)
print(result)