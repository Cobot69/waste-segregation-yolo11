# 1. Start the script.

# 2. Import necessary libraries:
#    a. Import the YOLO module from `ultralytics`.
#    b. Import additional libraries like `os` and `cv2` for file handling and image processing.

# 3. Load the trained YOLO model:
#    a. Specify the path to the trained model file (`best.pt`).
#    b. Load the model using the YOLO library.

# 4. Define the inference function:
#    a. Accept input image or video file.
#    b. Perform inference using the YOLO model.
#    c. Return the results (detections).

# 5. Print confirmation:
#    a. Confirm successful model loading and inference readiness.

# 6. End the script.


# Import necessary libraries
from ultralytics import YOLO
import cv2

# Step 1: Load the trained YOLO model
model_path = "runs/train/yolov11/weights/best.pt"  # Path to the trained model
try:
    print("Loading the trained YOLO model...")
    model = YOLO(model_path)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading the model: {e}")
    exit()

# Step 2: Define inference function
def perform_inference(image_path):
    """
    Perform inference using the trained YOLO model.
    Args:
        image_path (str): Path to the input image.
    Returns:
        results: YOLO inference results.
    """
    try:
        print(f"Performing inference on {image_path}...")
        results = model(image_path)  # Perform inference
        return results
    except Exception as e:
        print(f"Error during inference: {e}")
        return None

# Example usage
if __name__ == "__main__":
    input_image = "path/to/input/image.jpg"  # Replace with the path to your input image
    results = perform_inference(input_image)
    if results:
        print("Inference completed!")
