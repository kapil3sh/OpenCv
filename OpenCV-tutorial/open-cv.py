import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("watch_.jpg",cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1
#cv2.imshow("img",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#plt.imshow(img, cmap='gray', interpolation = 'bicubic')
#plt.plot([200,100], [200,100], 'c', linewidth=5)
#plt.show()

cap = cv2.VideoCapture(0)

while True :
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

cap.release()
#cv2.waitKey(0)
#cv2.waitKey(5000) # 5 sec delay before image window closes
cv2.destroyAllWindows()