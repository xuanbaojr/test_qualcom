from ultralytics import YOLO
import cv2

yolo = YOLO("yolov8m-face.pt")
results = yolo("./im.png")
print("results:", results)