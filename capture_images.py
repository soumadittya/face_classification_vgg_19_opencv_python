import cv2
import os
import numpy as np

def capture():
    path = str(input('Enter the path : ')) + '/'
    id = str(input('Enter id for dataset : ')) + '/'
    size = int(input('Enter the size of dataset : '))

    exists = os.path.isdir(path + id)
    if exists == False:
        try:
            os.mkdir(path + id)
            print('new id folder exists....')
        except:
            print('error : cannot create folder....')
    else:
        print('id folder already exists....')
    # making object for video capturing
    vid = cv2.VideoCapture(0)
    
    # making object for haarcascade face detection 
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # variable for number of rounds in the while loop
    # variable for specifying the number of images to be captured for each face
    count = 1
    
        
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
            print('No face found....')
            try:
                font = cv2.FONT_HERSHEY_SIMPLEX
                org = (25, 25)
                fontScale = 0.5
                color = (255, 0, 0)
                thickness = 1
                frame = cv2.putText(frame, 'No face found....', org, font,
                                    fontScale, color, thickness, cv2.LINE_AA)
            except:
                print('error : cannot display text on frame....')
        else:
            print('valid face detected....')
            x = faces_dimensions[-1][1][0]
            y = faces_dimensions[-1][1][1]
            w = faces_dimensions[-1][1][2]
            h = faces_dimensions[-1][1][3]
            try:
                frame_cropped = frame[y : y + h, x : x + w]
            except:
                print('cannot crop frame....')

            try:
                cv2.imwrite(path + id + str(count) + ".jpg", frame_cropped)
            except:
                print('Some error occured....')
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)

            # putting text on frmae
            try:
                font = cv2.FONT_HERSHEY_SIMPLEX
                org = (25, 25)
                fontScale = 0.5
                color = (255, 0, 0)
                thickness = 1
                frame = cv2.putText(frame, 'Capturing for : ' + id[:-1] + ' || ' + 'Total frames captured : ' + str(count), org, font,
                                    fontScale, color, thickness, cv2.LINE_AA)
            except:
                print('error : cannot display text on frame....')

            count = count + 1

        # displaying frame
        cv2.imshow('frame', frame)
        
        if (cv2.waitKey(1) & 0xFF == ord('q')) or count == size:
                break


    vid.release()
    cv2.destroyAllWindows()

capture()