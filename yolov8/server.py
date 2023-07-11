import cv2, base64
import numpy as np
from prediction import get_torch_version, predict
from flask import Flask, request, Response, jsonify
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bienvenido al contenedor de inferencia con GPU!"

@app.route("/version", methods=["POST"])
def get_version():
    return f"{get_torch_version()}"

@app.route("/predict", methods = ["POST"])
def predict_image():
    data = request.get_json()
    image_base64 = data['image']
    image_bytes = base64.b64decode(image_base64)
    image_np = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    boxes = predict(image)
    data = {
        "success": True,
        "boxes": boxes
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
