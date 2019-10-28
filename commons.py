# -*- encoding: utf-8 -*-

import logging
import redis
import configparser
from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

config = configparser.ConfigParser()
config.read('conf/config.ini')
logging.basicConfig(format='[%(asctime)s] [%(levelname)s] %(message)s', level=logging.INFO)
def log(msg,level="info"):
    if level == "info":
        logging.info(msg)
    elif level == "error":
        logging.error(msg)
    elif level == "debug":
        logging.debug(msg)
    elif level == "warn":
        logging.warning(msg)
    elif level == "critical":
        logging.critical(msg)

def redis_conn():
    if "redis" not in config.sections():
        msg = "Redis configure not found."
        log(msg)
        return msg
    redis_conn = ""
    try:
        #
        host = str(config['redis']['host'])
        port = int(config['redis']['port'])
        db = int(config['redis']['db'])
        redis_conn = redis.StrictRedis(host=host, port=port, db=db)
    except Exception as e:
        msg = f"Redis not connected! Config not found: {e}"
        log(msg,'error')
    return redis_conn