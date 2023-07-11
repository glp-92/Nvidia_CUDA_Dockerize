from prediction import get_torch_version
from flask import Flask
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Welcome to Cuda Pytorch container!"

@app.route("/version", methods=["POST"])
def get_version():
    return f"{get_torch_version()}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
