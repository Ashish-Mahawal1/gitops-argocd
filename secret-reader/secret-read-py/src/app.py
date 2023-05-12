from kubernetes import config,client
import base64
from flask import Flask

app = Flask(__name__)

def loadk8config():
    try:
        # Load config this way ,while in cluster
        config.load_incluster_config()
    except Exception as e:
        print(
            f"[loadk8config] Exception while loading config as in cluster {e}"
        )
        print("[loadk8config] Trying to load config for local")
        # Load config this way while running tests from local env
        config.load_kube_config()

def readSecret(secretName,namespace):

    loadk8config()
    v1 = client.CoreV1Api()
    sec = v1.read_namespaced_secret(secretName, namespace).data
    secretData = base64.b64decode(sec["password"]).decode("utf-8") 
    print(f'Secret Read successfully : {secretData}')

    return secretData

@app.route('/')
def hello_world():
    res = readSecret("mysecret","default")
    return res

@app.route('/test')
def test_route():
    return "Testing Endpoint only"

app.run(debug=True,host="localhost",port=5000)


    