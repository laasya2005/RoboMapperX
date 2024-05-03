### Object Detection using Deep Learning
In this project, I utilized the YOLO algorithm for object detection, specifically targeting the object 'husky.' I implemented the YOLOv3 convolutional neural network using ImageAI to achieve this task. Training was conducted on Google Colab with a K80 GPU, leveraging manually generated images of the 'husky' object along with background noise objects simulated in the pybullet simulator.

### Training Images
The training dataset was meticulously prepared using the pybullet simulator, encompassing various orientations, environments, and distances for the 'husky' object. The inclusion of diverse background objects as noise facilitated the model's ability to distinguish 'husky' from other objects.

### Labeling of Images
For YOLOv3 object detection, bounding boxes were annotated around the 'husky' object in each image. The LabelImg tool, available at GitHub - LabelImg, was utilized for this task. Approximately 1300+ images were annotated in the PascalVOC format using this tool.

### Model Training
Employing the ImageAI library, which offers powerful Computer Vision capabilities through deep learning, I trained the YOLOv3 Object Detection algorithm. Before training, anchor boxes were generated with an IoU (Intersection Over Union) of 0.9. Transfer learning yielded superior results compared to training from scratch, so I fine-tuned the pre-trained model to detect 'husky.' The model was trained over 5 epochs with a batch size of 4, taking approximately 3 hours. Evaluation of the model resulted in an mAP (Mean Average Precision) of 0.9668.

The ImageAI GitHub repository can be found at GitHub - ImageAI. The detection_config.json file containing anchor boxes is provided in the repository. However, due to size constraints on GitHub, the model .h5 file is hosted separately at Google Drive - Model and Data Files. Please ensure to download the model file (detection_model-ex-005--loss-0004.657.h5) from the models folder on Google Drive before running the main script. Note that tensorflow-gpu==1.13.1 and the latest version of ImageAI are required for model training.
