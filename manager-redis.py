# -*- encoding: utf-8 -*-

from commons import log, redis_conn
import json

def add_keys(keys):
    log("Adding Keys..")

    redis = redis_conn()
    for k,v in keys.items():
        redis.set(k,v)

def get_keys(keys):
    log("Getting Keys..")
    log(f"Keys: {keys}",'debug')
    log(type(keys),'debug')
    redis = redis_conn()
    keys_return = {}
    for key in keys:
        key = key.replace('"','')
        key = key.replace("'","")
        log(f"Keys: {key}")
        resp = redis.get(key)
        log(f"resp: {resp}")
        if resp:
            keys_return[key] = resp.decode('utf-8', 'replace')
    return keys_return

def del_keys(keys):
    log("Deleting Keys..")
    redis = redis_conn()
    for key in keys:
        redis.delete(key)
    return

