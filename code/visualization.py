# 1. Start the script.

# 2. Import necessary libraries:
#    a. Import `cv2` for displaying images.
#    b. Import the `os` library for file handling.

# 3. Define the visualization function:
#    a. Accept inference results and the input image path.
#    b. Parse the detections (bounding boxes, class labels, etc.).
#    c. Draw the bounding boxes and labels on the image.
#    d. Save the annotated image.

# 4. Display the annotated image:
#    a. Open a window to show the image with detections.
#    b. Wait for a key press to close the window.

# 5. End the script.

import cv2
import os

# Step 1: Define visualization function
def visualize_results(results, input_image_path, output_image_path="annotated_image.jpg"):
    """
    Visualize the YOLO inference results on the input image.
    Args:
        results: YOLO inference results.
        input_image_path (str): Path to the input image.
        output_image_path (str): Path to save the annotated image.
    """
    try:
        print("Visualizing results...")
        # Load the input image
        image = cv2.imread(input_image_path)

        # Iterate through detections
        for detection in results.xyxy[0]:  # Access bounding boxes
            x1, y1, x2, y2, conf, cls = detection
            label = f"{results.names[int(cls)]} ({conf:.2f})"

            # Draw bounding box and label on the image
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(image, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Save the annotated image
        cv2.imwrite(output_image_path, image)
        print(f"Annotated image saved as {output_image_path}")

        # Display the image
        cv2.imshow("Detections", image)
        cv2.waitKey(0)  # Wait for a key press
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error during visualization: {e}")

# Example usage
if __name__ == "__main__":
    input_image = "path/to/input/image.jpg"  # Replace with the path to your input image
    output_image = "path/to/output/annotated_image.jpg"
    from model_loading import perform_inference  # Import the inference function
    results = perform_inference(input_image)
    if results:
        visualize_results(results, input_image, output_image)
