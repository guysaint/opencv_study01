import cv2
import numpy as np

new_height = 300
new_width = 300

#이미지 출력
image = cv2.imread('../image/like_lenna.png') #이미지 가져오기
#dst = np.zeros((new_height, new_width, 3), dtype=np.uint8) #항상 uint8 형식의 이미지만 가능
dst = np.zeros((new_height, new_width, 3), dtype=image.dtype) #이미지 형식이 무엇인지 모를 때 유연하게 원본을 따라가주는 코드
resized = cv2.resize(image, (new_width, new_height))
np.copyto(dst,resized)

#cv2.imshow('Image Window', image) #이미지를 보여주는 명령어
cv2.imshow('Image Window', dst)
#cv2.imshow('Image Window', image_small)
print(image.shape)
print(dst.shape)
#print(image_small.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
