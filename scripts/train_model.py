from ultralytics import YOLO

# Load pre-trained model (YOLOv8n = nano, fastest)
model = YOLO('yolov8n.pt')

# Train the model
model.train(
    data='./dataset/data.yaml',  # Correct path to the data.yaml file
    epochs=15,  # Number of epochs
    imgsz=320,  # Image size
    batch=4    # Batch size
)
