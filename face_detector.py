import cv2
from tensorflow import keras as kf
import numpy as np

# loading the trained model
filepath = './model_trained/resnet_model_10.h5'
full_model = kf.models.load_model(filepath)

# making the opencv video capturing object
vid = cv2.VideoCapture(0)

# object for opencv haarcascade face classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while(True):
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray)
    faces_dimensions = {}

    for i in faces:
        faces_dimensions[i[2] * i[3]] = i
    faces_dimensions = sorted(faces_dimensions.items())
    print('Dimensions : ', faces_dimensions)

    if len(faces) == 0 or faces_dimensions[-1][0] < 50000:
        # putting text on frame
        try:
            font = cv2.FONT_HERSHEY_SIMPLEX
            org = (25, 25)
            fontScale = 0.5
            color = (0, 0, 255)
            thickness = 1
            name = ''
            frame = cv2.putText(frame, 'No face found....', org, font,
                                fontScale, color, thickness, cv2.LINE_AA)
            print('No face found....')
            print('====================================================================')
        except:
            print('error : cannot display text on frame....')
    else:
        x = faces_dimensions[-1][1][0]
        y = faces_dimensions[-1][1][1]
        w = faces_dimensions[-1][1][2]
        h = faces_dimensions[-1][1][3]


        try:
            # cropping the face area using the coordinated returned by haarcascade face classifier
            frame_cropped = frame[y: y + h, x: x + w]
            print('face area cropping done....')
        except:
            print('cannot crop face area....')

        try:
            # resizing the image using opencv to size (224, 224) as required by vgg19 model
            frame_cropped = cv2.resize(frame_cropped, (224, 224), interpolation = cv2.INTER_AREA)
            print('face area resizing done....')
        except:
            print('cannot resize face area....')

        try:
            # reshaping the face area image to (1, 224, 224, 3) as required by the input layer
            frame_cropped = frame_cropped.reshape(1, 224, 224, 3)
            print('image array reshaping done....')
        except:
            print('error : cannot reshape array image....')

        try:
            # predicting
            pred = full_model.predict(frame_cropped)
            if pred[0][0] > 0.5:
                name = 'Som'
            elif pred[0][1] > 0.5:
                name = 'Sudipta'
            elif pred[0][2] > 0.5:
                name = 'Uttam'
            else:
                name = 'No name matched'
            print('Predicted face : ', name)
            print('prediction done....')
        except:
            print('error : cannot predict....')


        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)

        # putting text on frame
        try:
            font = cv2.FONT_HERSHEY_SIMPLEX
            org = (25, 25)
            fontScale = 0.5
            color = (255, 0, 0)
            thickness = 1
            frame = cv2.putText(frame, 'Name : ' + name, org, font,
                                fontScale, color, thickness, cv2.LINE_AA)
        except:
            print('error : cannot display text on frame....')

        print('====================================================================')

    # displaying frame
    cv2.imshow('frame', frame)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

vid.release()
cv2.destroyAllWindows()