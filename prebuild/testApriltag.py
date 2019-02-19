import cv2
import apriltag

img = cv2.imread("test.pnm");
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("test",gray_img)
cv2.waitKey(0)
detector = apriltag.Detector()
result = detector.detect(gray_img)
print("april complete")
print(result)
