# Assignment Project-1
## Hand Detection for Safety in Machine Operation

## **1. System Architecture:**
### **Hardware:**
- Nvidia Jetson nano, as mentioned in the project document
- A capable machine to install the above device in, with at least 16GB of ram for seamless training of the model and a 6/8 core CPU with an SSD.
- A Camera which will be used to capture the images or videos of the operation area
- A display to monitor and view the captured images/video and to provide real-time feedback
- Sensors such as ultrasonic or motion detectors to trigger the detection system
### **Software:**
- OS (Operating system) such as Linux/Windows, Linux preferred
- A stable python installation
- Libraries such as TensorFlow, Numpy, PyTorch
- OpenCV for the image processing part.
- A User Interface, to monitor and configure the program.

The Nvidia Jetson Nano will be used at the heart of the computer vision system. It will do all the heavy lifting, which is image processing and deep learning. It is a single board computer designed specifically for AI/ML/DL applications. It's fast, efficient and has high capabilities in the field. 

## **2. Image Processing and Hand Detection:**
### **Steps:**
- Image preprocessing; images may need to be resized, cropped, normalized, denoised, upscaled or even downscaled depending on the requirement and the condition.
- Feature extraction can involve techniques like Histogram of Oriented Gradients (HOG) or deep learning-based feature extraction methods.
### **Region of Interest (ROI):**
- We need to make it so that, the ROI is narrowed down to the crucial parts/sections of the machine.
- This will further help with the efficiency as the region needs to be checked is reduced, hence increasing the potency and reducing the overall load on the system.
### **Hand Detection Algorithm:**
- A CNN based algorithm, such as YOLO(You Only Look Once), could be used for the same due to its superior speeds and high accuracy when compared to other algorithms.
![](https://pjreddie.com/media/image/map50blue.png)
<sub>Source: https://pjreddie.com/darknet/yolo/</sub>

- YOLO is used for real-time object detection and provides faster outputs and results, albeit the training time may differ.

## **3. AI Training and Development:**
### **Data Collection:**
- For this project, we need to collect a vast number of images/videos of hands near the machine parts, which will be used to train the model.
- We need to ensure diversity in the data to cover a wide range of cases and machineries depending on the requirement.
### **Annotation:**
- The annotation process is where we will add bounding boxes to the hands in the images or frames in a video, using an annotation tool such as VIA(VGG Image Annotator) or labelbox.
- Doing this process manually would be preferred as we are dealing with safety here first and foremost.
- Labelling the annotation boxes with the label, "Hand\s"
- Making sure all the data is annotated and labelled correctly before training the model.
### **AI Training Pipeline:**
- Choosing the DL framework; in our case, I have selected tensorflow as my approach to this project.
- Selecting the model, here as stated above, YOLO might be a good pick due to its fast and reliable dectection.
- Data preparation and preprocessing; we preprocess our annotated data before we train the model.
### **Training and Fine-Tuning the Model:**
- We split the dataset into 3 sets, training, validation and testing.
- The training process is where we will try to adjust the weights and such to get the highest accuracy.
- The hyperparameter may be adjusted too, for the learning rate, batch sizes, etc. to help with the fine-tuning.
- We can also adjust the number of epochs to see which gives us the lowest rate of error.
- The model can then be evaluated and checked for metrics such as mAP (Mean Average Precision) to monitor the speed and accuracy according to our requirements.

## **4. Deployment Planning:**
### **Deployment Strategy:**
- This is to be deployed on the Nvidia Jetson Nano for the real-time processing.
- We need to integrate our system with the sensors to trigger the system when necessary.
- Alert the operator or person near the machinery with an alarm and on the display as an extra measure.
- Integrate with the machine control system for automatic safety measures.
### **Real-time Performance Considerations:**
- Optimize model inference for real-time performance, possibly using TensorRT for Jetson Nano.
- Implement multi-threading or asynchronous processing for efficient data handling.
- Monitoring the system in real time for resource usage and optimizing as needed wherever possible.
### **Challenges and Limitations:**
- Reflections, lightning, position can pose as challenges in the system, as theyre never constant, this could be counteracted by adding an additional check during training for reflective surfaces or training the model on a dataset which contains them.
- Human hands can vary in size, colour, shape, etc, can prove to be a limitation.
- Real-world deployment may face challenges like dust, vibrations, or extreme temperatures, which could affect the hardware and/or the sensors.


