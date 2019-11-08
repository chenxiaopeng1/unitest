import logging
import threading
import time

def get_logger():
    logger=logging.getLogger("threading_eg")
    logger.setLevel(logging.DEBUG)
    fh=logging.FileHandler("E:\\threading.log")
    fmt = '%(asctime)s - %(name)s - %(processName)s - %(threadName)s - %(levelname)s - %(message)s'
    formater=logging.Formatter(fmt)
    fh.setFormatter(formater)
    logger.addHandler(fh)
    return logger

def doubler(number,logger):
    logger.debug("XXX")
    logger.info("aaa")
    logger.warning("bbb")
    logger.error("ccc")

    result=number*2
    time.sleep(5)
    logger.debug("yyyy:{}".format(result))


logger=get_logger()
thread_names=["Mike","George","Wanda","Dingbat","Nina"]

for i in range(5):
    my_thread=threading.Thread(target=doubler,name=thread_names[i],args=(i,logger))
    my_thread.start()