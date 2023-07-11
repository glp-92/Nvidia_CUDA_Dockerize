import torch
from ultralytics import YOLO
import cv2, time, os
import numpy as np

model = YOLO("yolov8m.pt", task = "detect")

def get_torch_version():
    return f"Pytorch version: {torch.__version__}. Cuda: {torch.cuda.is_available()}. GPU device: {torch.cuda.current_device()}. GPU name: {torch.cuda.get_device_name(0)}"

def predict(im):
    results = model(source=im, save=False, boxes=False, verbose=False, show=False)[0]
    boxes = []
    for box in results.boxes.xyxy:
        box_data = {
            'x1': int(box[0]),
            'y1': int(box[1]),
            'x2': int(box[2]),
            'y2': int(box[3])
        }
        boxes.append(box_data)
    return boxes