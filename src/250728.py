import cv2
import numpy as np
import random

def draw_cloud(img, x, y):
    # 중심 원
    r1 = random.randint(25, 35)
    cv2.circle(img, (x, y), r1, (255, 255, 255), -1)

    # 오른쪽 원
    r2 = random.randint(25, 35)
    offset_x2 = random.randint(25, 35)
    cv2.circle(img, (x + offset_x2, y), r2, (255, 255, 255), -1)

    # 위쪽 중간 원
    r3 = random.randint(25, 35)
    offset_x3 = random.randint(10, 20)
    offset_y3 = random.randint(15, 25)
    cv2.circle(img, (x + offset_x3, y - offset_y3), r3, (255, 255, 255), -1)

def draw_rainbow(base_img, center, radius, thickness=15, alpha=0.3):
    rainbow_colors = [
        (147, 20, 255),   # Violet
        (255, 0, 0),      # Blue
        (255, 127, 0),    # Green
        (0, 255, 0),      # Yellow
        (0, 255, 255),    # Orange
        (0, 165, 255),    # Red
    ]

    overlay = base_img.copy()

    for i, color in enumerate(rainbow_colors):
        cv2.ellipse(
            overlay,
            center=center,
            axes=(radius - i * thickness, radius - i * thickness // 2),
            angle=0,             
            startAngle=180,       
            endAngle=360,
            color=color,
            thickness=thickness
        )

    cv2.addWeighted(overlay, alpha, base_img, 1 - alpha, 0, base_img)



    # 알파 블렌딩 (반투명하게)
    cv2.addWeighted(overlay, alpha, base_img, 1 - alpha, 0, base_img)

def draw_transparent_cloud(img, x, y, alpha=0.4):
    overlay = img.copy()
    draw_cloud(overlay, x, y)
    cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)

# 이미지 불러오기 및 리사이즈
img = cv2.imread('../image/like_lenna.png')
img = cv2.resize(img, (720, 872))

# 구름 위치
cloud_positions = [(80, 100), (230, 80), (370, 130), (520, 90), (620, 120)]
for pos in cloud_positions:
    draw_cloud(img, pos[0], pos[1])

# 무지개 그리기
draw_rainbow(
    base_img=img,
    center=(300, 400),  # 무지개 중심
    radius=500,
    thickness=12,
    alpha=0.5
)
for _ in range(7):
    x = random.randint(50, 650)        # 좌우 여유
    y = random.randint(200, 400)       # 무지개 아래쪽 y 범위
    alpha = random.uniform(0.3, 0.6)
    draw_transparent_cloud(img, x, y, alpha)

# 출력
cv2.imshow("Decorated with Random Clouds and Rainbow", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
