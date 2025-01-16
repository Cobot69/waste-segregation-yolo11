# 1. Start the script.

# 2. Install the required library:
#    a. Install the `roboflow` library for accessing the dataset.

# 3. Import necessary modules:
#    a. Import the `roboflow` module.

# 4. Authenticate with the Roboflow API:
#    a. Use the API key provided by Roboflow.

# 5. Access the project:
#    a. Specify the workspace and project name in Roboflow.
#    b. Retrieve the specific version of the dataset.

# 6. Download the dataset:
#    a. Choose the format (e.g., YOLOv8 or YOLOv11 format).
#    b. Save the dataset in the specified directory.

# 7. Print confirmation:
#    a. Confirm the successful download of the dataset.

# 8. End the script.


# Install required library
try:
    import os
    print("Installing Roboflow...")
    os.system("pip install roboflow --quiet")  # Install roboflow package
except Exception as e:
    print(f"Error installing Roboflow: {e}")
    exit()

# Import the roboflow module
try:
    from roboflow import Roboflow
except ImportError:
    print("Roboflow installation failed. Please try again.")
    exit()

# Authenticate with Roboflow API
try:
    print("Authenticating with Roboflow API...")
    rf = Roboflow(api_key="your_api_key")  # Replace 'your_api_key' with your actual API key
except Exception as e:
    print(f"Error authenticating with Roboflow: {e}")
    exit()

# Access the project and download the dataset
try:
    print("Accessing project and downloading dataset...")
    # Replace 'workspace_name' and 'project_name' with your Roboflow workspace and project name
    project = rf.workspace("workspace_name").project("project_name")
    
    # Replace 'version_number' with the version of the dataset you want to download
    dataset = project.version(version_number).download("yolov8")
    print("Dataset downloaded successfully!")
except Exception as e:
    print(f"Error downloading dataset: {e}")



# Replace:

# your_api_key with your Roboflow API Key.
# workspace_name with the name of your Roboflow workspace.
# project_name with the name of your project.
# version_number with the version number of the dataset.
# Save this as dataset_download.py in the code folder.