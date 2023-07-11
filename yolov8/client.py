import cv2
import requests
import base64
import json, time

ti = time.time()

# Read img
image = cv2.imread("test.jpg")

# Convert to base64
_, buffer = cv2.imencode('.jpg', image)
image_base64 = base64.b64encode(buffer).decode('utf-8')

# Payload creation
payload = {
    'image': image_base64
}

# Send POST request to endpoint
url = 'http://localhost:5000/predict'
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(payload), headers=headers)

# Show response
print(response.json())
print(time.time() - ti)