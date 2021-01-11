Human Dectection and Counting System

This is a Python program that detects and recognizes humans in picture, video and live video feed through webcam and gives the total count. The program displays the image or video with the people marked with a rectangle.

The program has a GUI that asks the user for the type of input file to detect the humans in. The GUI provides three options for Image, Video and Camera. The 'Image' and 'Video' options ask for the path of the image and video file. A file selection window opens and asks the user for the specific file type to be chosen. The 'Camera' option turns on the webcam and uses the live video feed as the input. 

The program makes use of the libraries OpenCV, NumPy, Imutils and Tkinter.
  OpenCV - For real-time computer vision. 
  NumPy - Support for multidimentional arrays and matrices, and function to operate on them.
  Imutils - Resizing image
  Tkinter - To design a GUI
  
  This program makes use of Histogram of Oriented Gradient Descriptor. It is a feature descriptor for the use object detection. OpenCV has efficiently implemented HOG Descriptor algorithm with Support Vector Machine or SVM. HOGDescriptor_getDefaultPeopleDetector() is a pre-trained model for human detection of OpenCV and then the support vector machine is fed into it.

The detect() function detects the humans in the frame and displays the frame with the people highlighted. 
