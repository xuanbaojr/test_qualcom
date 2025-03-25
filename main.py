from ultralytics import YOLO
import cv2

yolo = YOLO("yolov8n.pt")
results = yolo("./im.png")
print("results:", results)