# Waste Segregation Using YOLOv11

## Introduction
This project utilizes YOLOv11, a state-of-the-art object detection model, to classify and segregate waste items into various categories. Waste segregation is crucial for efficient recycling and environmental sustainability.

## YOLOv11 Exploration
YOLOv11 (You Only Look Once version 11) is chosen for its real-time object detection capabilities and high accuracy. It excels in scenarios where quick inference and precise localization of objects are essential, making it ideal for waste segregation tasks.

## Dataset
The dataset used in this project consists of over 9,500+ images with 21 distinct classes. Each class represents a specific waste item commonly encountered in recycling processes. The classes are mapped as follows:
![Image](https://github.com/user-attachments/assets/24697760-2079-4970-81b5-8a109473f636)


CLASS_MAPPING = {
    0: 'battery',
    1: 'can',
    2: 'cardboard_bowl',
    3: 'cardboard_box',
    4: 'chemical_plastic_gallon',
    5: 'chemical_spray_can',
    6: 'light_bulb',
    7: 'paint_bucket',
    8: 'plastic_bag',
    9: 'plastic_bottle',
    10: 'plastic_bottle_cap',
    11: 'plastic_box',
    12: 'plastic_cup',
    13: 'plastic_cup_lid',
    14: 'plastic_spoon',
    15: 'scrap_paper',
    16: 'scrap_plastic',
    17: 'snack_bag',
    18: 'stick',
    19: 'straw',
    20: 'toilet_cleaner'
}
![Image](https://github.com/user-attachments/assets/1d32d135-4059-458b-ae21-0175c3f22731)


images/Screenshot 2025-01-16 190442.png

## How to Run
(all the code given is sudo code)
Environment Setup: Execute environment_setup.py to set up the necessary dependencies.
Dataset Download: Use dataset_download.py to acquire the dataset required for training and testing.
Model Training: Train the YOLOv11 model using training.py to optimize it for waste segregation.
Inference and Visualization: Employ model_loading.py and visualization.py to perform inference on new data and visualize the results.

## Real-time Testing
The model has been rigorously tested in real-time environments to ensure its accuracy and efficiency in waste item detection and classification. Real-time testing validates the model's performance under various conditions and environments, enhancing its reliability for practical applications.

## Conclusion
This project aims to contribute to sustainable waste management practices by automating the segregation process using advanced computer vision techniques. YOLOv11, with its robust performance and real-time capabilities, ensures accurate identification and classification of waste items, thereby facilitating efficient recycling initiatives.

