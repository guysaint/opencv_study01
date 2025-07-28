import cv2
import numpy as np

image = cv2.imread('../image/like_lenna.png') #이미지 가져오기
'''
# 1. 이미지 사이즈 변환
#---------------------------------
image_small = cv2.resize(image,(100,100))
cv2_imshow(image_small)
cv2.waitKey(0)
cv2.destroyAllWindows()
#------------------------------------
'''




'''
# 2.이미지 사이즈 원래대로 돌리기
#-------------------------
new_height = 300
new_width = 300
image = cv2.imread('../image/like_lenna.png') #이미지 가져오기
#dst = np.zeros((new_height, new_width, 3), dtype=np.uint8) #항상 uint8 형식의 이미지만 가능
dst = np.zeros((new_height, new_width, 3), dtype=image.dtype) #이미지 형식이 무엇인지 모를 때 유연하게 원본을 따라가주는 코드
resized = cv2.resize(image, (new_width, new_height))
np.copyto(dst,resized)
cv2.imshow('Image Window', dst)
print(dst.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
#---------------------------
'''

'''
# 3. 배율로 사이즈 전환
#------------------------------------------------------
image_big = cv2.resize(image,dsize=None,fx=2,fy=2,)
cv2.imshow("big image", image_big)

cv2.waitKey(0)
cv2.destroyAllWindows()
#---------------------------------------------------
'''

'''
# 4. 상하 반전
#----------------------------------------------
image_fliped = cv2.flip(image,0)
cv2_imshow("image_fliped", image_fliped)
cv2.waitKey(0)
cv2.destroyAllWindows()
#----------------------------------------------
'''

'''
# 5. 좌우 반전
#-----------------------------------------------
image_fliped = cv2.flip(image,1)
cv2_imshow("image_fliped", image_fliped)
cv2.waitKey(0)
cv2.destroyAllWindows()
#------------------------------------
'''


'''
# 6. 회전 변환
#---------------------------------------
height, width = image.shape
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1) # 90도 30도 등등...
result = cv2.warpAffine(image, matrix, (width, height))
cv2_imshow("rotate",result)
cv2.waitKey(0)
cv2.destroyAllWindows()
#---------------------------------------
'''

'''
# 7. 이미지 자르기 01
#-----------------------
cv2_imshow("cut image",image[:100,:100])
#cv2_imshow(image[50:150,50:150])
cv2.waitKey(0)
cv2.destroyAllWindows()
#------------------------
'''

'''
# 8. 이미지 자르기 02
#-----------------------
croped_image = image[50:150,50:150]
croped_image[:] = 200
cv2_imshow(image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#------------------------
'''

'''
# 9. 이미지 자르기 03
image = cv2.imread('like_lenna.png', cv2.IMREAD_GRAYSCALE)
croped_image = image[50:150,50:150].copy()
croped_image[:] = 200
cv2_imshow("image window", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#------------------------
'''

