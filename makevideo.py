import cv2

fps = 5
fourcc = cv2.cv.CV_FOURCC('D', 'I', 'V', 'X')  
videoWriter = cv2.VideoWriter('lresults.avi', fourcc, fps, (1280,720))
for i in range(200):

    img = cv2.imread('lresults/frame'+str(i+1)+'.jpg')
 
    videoWriter.write(img)
#videoWriter.release()