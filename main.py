# Imagine a real application here with database, caching etc... 
# this is just a placeholder

from flask import Flask
from flask_healthz import healthz
from flask_healthz import HealthError
import os
app = Flask(__name__)
app.register_blueprint(healthz, url_prefix="/status")

def printok():
    print("Everything is fine")

def liveness():
    pass

def readiness():
    try:
        printok()
    except Exception:
        raise HealthError("Can't connect to the file")

app.config.update(
    HEALTHZ = {
        "live": app.name + ".liveness",
        "ready": app.name + ".readiness",
    }
)


@app.route("/")
def hello_world():
    return "<p>Hello, World BetVictor!</p>"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 32762))
    app.run(debug=True, host='0.0.0.0', port=port)
