from gevent import monkey; monkey.patch_all()

import json
from bottle import Bottle, run, request, response, get, post
import time
import gevent

app = Bottle()

@app.get("/test")
def test():
    t1 = time.time()
    #gevent.sleep(5)
    time.sleep(5)
    t2 = time.time()
    return {"t1": t1, "t2": t2}


run(app, host='0.0.0.0', port=8000, server='gevent')
