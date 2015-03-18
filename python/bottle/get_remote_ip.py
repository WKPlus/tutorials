
import json
from bottle import Bottle, run, request, get

app = Bottle()

@app.get("/ip")
def get_remote_ip():
    ip = request.environ.get('REMOTE_ADDR')
    return json.dumps({"ip": ip})


run(app, host='0.0.0.0', port=8000)
