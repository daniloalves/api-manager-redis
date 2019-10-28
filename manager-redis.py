# -*- encoding: utf-8 -*-

from commons import log, redis_conn
from flask import make_response, abort
import json

def add_keys(keys):
    log("Adding Keys..")
    redis = redis_conn()    
    for key in keys:
        name = key['name']
        value = json.dumps(key['value'])
        resp = redis.set(name,value)

        if resp:
            return make_response(
                "Successfully created.",200
            )
        else:
            return abort(
                404, "[ERROR] On created!"
            )

def get_keys(keys):
    log("Getting Keys..")
    redis = redis_conn()
    keys_return = {}
    for key in keys:
        key = key.replace('"','')
        key = key.replace("'","")
        resp = redis.get(key)
        if resp:
            keys_return[key] = resp.decode('utf-8', 'replace')
    return keys_return

def del_keys(keys):
    log("Deleting Keys..")
    redis = redis_conn()
    for key in keys:
        redis.delete(key)
    return

