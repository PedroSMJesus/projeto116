import cv2 

img = cv2.imread("solar-system.jpg")

img2 = cv2.imread("solar-systemNamed.png")

cv2.putText(img, "Sol", (100,80), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 225))

cv2.putText(img, "Mercurio", (110,160), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 225))

cv2.putText(img, "Venus", (200,180), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 225))

cv2.putText(img, "Terra", (285,170), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 225))

cv2.putText(img, "Marte", (385,170), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 225))

cv2.putText(img, "Jupiter", (450,80), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 225))

cv2.putText(img, "Saturno", (650,120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 225))

cv2.putText(img, "Urano", (900,120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 225))

cv2.putText(img, "Urano", (1100,120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 225))

cv2.imshow("resultado", img)

cv2.imwrite("solar-systemNamed.png", img2)

cv2.waitKey(0)

