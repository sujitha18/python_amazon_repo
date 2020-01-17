import inspect
import logging
def customLogger(loglevel=logging.DEBUG):
    #get the name of the class or method from where these called
    loggerName=inspect.stack()[1][3]
    logger=logging.getLogger(loggerName)
    #by default,log all the messages
    logger.setLevel(logging.DEBUG)
    fileHandler=logging.FileHandler("./resources/reports/log_report/automation.log",mode="a")
    fileHandler.setLevel(loglevel)
    formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s",
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger

