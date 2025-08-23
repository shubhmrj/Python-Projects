import logging

def setup_logger():
    logger = logging.getLogger("BankApp")
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler("bank_app.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

logger = setup_logger()
