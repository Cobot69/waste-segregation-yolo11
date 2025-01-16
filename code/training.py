# 1. Start the script.

# 2. Import the required library:
#    a. Import the YOLO module from the `ultralytics` package.

# 3. Define the dataset and model:
#    a. Specify the path to the dataset configuration file (`data.yaml`).
#    b. Load the YOLOv11 model.

# 4. Configure training parameters:
#    a. Set the number of epochs for training.
#    b. Define the image size for the model.
#    c. Specify additional parameters as needed (e.g., batch size, learning rate).

# 5. Train the model:
#    a. Use the YOLO training method with the dataset and parameters.

# 6. Save the trained model:
#    a. Export the trained model to the desired location.

# 7. Print training summary:
#    a. Display key metrics, such as loss and accuracy, after training.

# 8. End the script.



# Import the required library
from ultralytics import YOLO

# Step 1: Define the dataset and model
dataset_path = "/path/to/your/dataset/data.yaml"  # Replace with the path to your dataset YAML file
pretrained_model = "yolov11.pt"  # YOLOv11 pretrained model file

# Step 2: Load the YOLOv11 model
model = YOLO(pretrained_model)

# Step 3: Configure training parameters
epochs = 50  # Number of training epochs
image_size = 640  # Image size (e.g., 640x640 pixels)

# Step 4: Train the model
try:
    print("Starting training...")
    model.train(
        data=dataset_path,      # Path to the dataset configuration file
        epochs=epochs,          # Number of epochs for training
        imgsz=image_size,       # Image size
        batch=16,               # Batch size (optional)
        lr0=0.001               # Initial learning rate (optional)
    )
    print("Training completed successfully!")
except Exception as e:
    print(f"Error during training: {e}")

# Step 5: Save the trained model
try:
    trained_model_path = "runs/train/yolov11/weights/best.pt"  # Update with actual location if needed
    print(f"Trained model saved at: {trained_model_path}")
except Exception as e:
    print(f"Error saving the trained model: {e}")






# Replace the following placeholders:

# /path/to/your/dataset/data.yaml: The path to your dataset's YAML configuration file.
# yolov11.pt: Path to the YOLOv11 pretrained weights.
# epochs: The desired number of training epochs.
# Customize optional parameters:

# Batch size (batch) and learning rate (lr0) can be adjusted based on your setup.
# Save this as training.py in the code folder