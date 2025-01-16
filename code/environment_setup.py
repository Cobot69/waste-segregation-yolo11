# 1. Start the script.

# 2. Install necessary Python libraries:
#    a. Install `ultralytics` (for YOLOv11).
#    b. Install `torch` (PyTorch library for deep learning).
#    c. Install `onnxruntime` (for model optimization and ONNX inference).

# 3. Verify installations:
#    a. Check if the libraries were installed successfully.
#    b. Print the versions of installed libraries for confirmation.

# 4. End the script.


# Install necessary Python libraries 
try:
    print("Installing required libraries...")
    import os
    os.system("pip install ultralytics")  # Install YOLOv11 package
    os.system("pip install torch")        # Install PyTorch
    os.system("pip install onnxruntime") # Install ONNX runtime for inference

    # Verify installations
    import ultralytics
    import torch
    import onnxruntime
    print(f"Ultralytics version: {ultralytics.__version__}")
    print(f"PyTorch version: {torch.__version__}")
    print(f"ONNX Runtime version: {onnxruntime.__version__}")

    print("Environment setup completed successfully!")
except Exception as e:
    print(f"Error during setup: {e}")
