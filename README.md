# Assignment Project-1
## Hand Detection for Safety in Machine Operation

## **System Architecture:**
### **Hardware:**
- Nvidia Jetson nano, as mentioned in the project document
- A capable machine to install the above device in, with at least 16GB of ram for seamless training of the model and a 6/8 core CPU with an SSD.
- A Camera which will be used to capture the images or videos of the operation area
- A display to monitor and view the captured images/video and to provide real-time feedback
- Sensors such as ultrasonic or motion detectors to trigger the detection system
### **Software:**
- OS (Operating system) such as Linux/Windows, Linux preferred
- A stable python installation
- python libraries such as TensorFlow, Numpy, PyTorch,
- OpenCV for the image processing part
- A User Interface, to monitor and configure the program

The Nvidia Jetson Nano will be used at the heart of the computer vision system. It will do all the heavy lifting, which is image processing and deep learning. It is a single board computer designed specifically for AI/ML/DL applications. It's fast, efficient and has high capabilities in the field. 

## **Image Processing and Hand Detection:**
### **Steps:**
- Image preprocessing; images may need to be resized, cropped, normalized, denoised, upscaled or even downscaled depending on the requirement and the condition.
- Feature extraction can involve techniques like Histogram of Oriented Gradients (HOG) or deep learning-based feature extraction methods.
### **Region of Interest (ROI):**
- We need to make it so that, the ROI is narrowed down to the crucial parts/sections of the machine.
- This will further help with the efficiency as the region needs to be checked is reduced, hence increasing the potency and reducing the overall load on the system.
### **Hand Detection Algorithm:**
- 
