import cv2
import numpy as np

'''
# 1. 도형 그리기 01 - 선, 원
#---------------------------------
space = np.zeros((500, 1000), dtype=np.uint8)
line_color = 255
color = 255
space1 = cv2.line(space,(100,100), (800,400), line_color, 3, 1)
space2 = cv2.circle(space,(600,200), 100, color, 4, 1)
cv2.imshow("line window", space1)
cv2.imshow("circle window", space2)
cv2.waitKey(0)
cv2.destroyAllWindows()
#------------------------------------
'''
'''
# 2. 도형 그리기 02 - 네모, 곡선
#-------------------------------
space = np.zeros((500, 1000), dtype=np.uint8)
line_color = 255
color = 255
space3 = cv2.rectangle(space,(500,200), (800,400), color, 5, 1)
space4 = cv2.ellipse(space,(500,300), (300,200), 0, 45, 250, color, 4)
cv2.imshow("rectangle window", space3)
cv2.imshow("ellipse window", space4)
cv2.waitKey(0)
cv2.destroyAllWindows()
#----------------------------------
'''

'''
# 3. 색채우기
#-----------------------------------------
space = np.zeros((1000, 1000), dtype=np.uint8)
line_color = 255
color = 255
obj1 = np.array([[300,500], [500,500], [400,600], [200,600]])
obj2 = np.array([[600,500], [800,500], [700,200]])
cv2.polylines(space, [obj1], True, color, 3)
cv2.fillPoly(space, [obj2], color, 1)
cv2.imshow("ellipse window", space)
cv2.waitKey(0)
cv2.destroyAllWindows()
#-----------------------------------------
'''
space = np.zeros((1000, 1000), dtype=np.uint8)
line_color = 255
color = 255
obj1 = np.array([[300,500], [500,500], [400,600], [200,600]])
obj2 = np.array([[600,500], [800,500], [700,200]])
cv2.polylines(space, [obj1], True, color, 3)
cv2.fillPoly(space, [obj2], color, 1)
cv2.imshow("ellipse window", space)
cv2.waitKey(0)
cv2.destroyAllWindows()