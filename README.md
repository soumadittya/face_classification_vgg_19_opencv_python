# face_classification_vgg_19_opencv_python
Face classification has been done using VGG19  architecture and OpenCV in Python.

Description of different files in the project:

1. face_classifier_trainer_VGG19_1.ipynb :
    VGG19 architecture has been used by directly importing from the keras pre built models.
    Convolutional layers have not been trained instead of that 'imagenet' weights have been imported directly.
    Classification layers of VGG19 model have been replaced with custom layers which contains:
      1 Flatten layer
      3 Dense layers with 100 neurons each with relu activation function
      1 output layer with softmax activation function
      
     At last the model has been saved.

2. capture_images.py:
    It helps in creating a custom dataset.
    
    Way of using:
    Run the file
    It will ask for path.
    Enter the path.
    Then it will ask for class name.
    Enter the class name.
    Then it will ask for the number of images which have to be captured for the class specified in the previous line.
    
    Working:
    OpenCV haarcascade classifier has been used to detect the facial area.
    Only the facial area is cropped out from the whole frame.
    Facial area is cropped if the multiplication of width and height of the facial area is more than 50000.
    If it detects multiple faces in a single frame then it will accept the face which covers more area (width * height) in the frame.
    It has been done to make a organized dataset.
    If there is no face detected by haarcascade classifier of OpenCV or the multiplication of width and height of the facial area is less than 50000 then
    'no face found' will be shown on the frame and there will be no image file written to the specified dataset folder.
    Image is resized to (224, 224) as required by VGG19 model.
    
3. face_detector.py:
   This file is used for detecting and classify different faces.
   OpenCV haarcascade classifier has been used to detect the facial area.
   Only the facial area is cropped out from the whole frame.
   Facial area is cropped if the multiplication of width and height of the facial area is more than 50000.
   If it detects multiple faces in a single frame then it will accept the face which covers more area (width * height) in the frame.
   It has been done to make a organized dataset.
   If there is no face detected by haarcascade classifier of OpenCV or the multiplication of width and height of the facial area is less than 50000 then
   'no face found' will be shown on the frame.
    
   If a face is detected then it will be resized to (224, 224) as required by the VGG19 model.
   Then the result will be displayed on the frame.
    
   
    
    


   
