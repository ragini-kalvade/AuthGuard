import cv2 
import numpy as np

def camera():
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('frame',frame)
    
        # save the image
        cv2.imwrite("frame.png", frame)
        
        if cv2.waitKey(10000) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()