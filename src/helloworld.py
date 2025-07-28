import cv2
#이미지 출력
image = cv2.imread('../image/like_lenna.png')
cv2.imshow('Image Window', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
