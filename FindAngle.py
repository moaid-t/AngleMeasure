import cv2
import math

img = cv2.imread('images/angles.jpg')
points = []


def calculate_slope(p1, p2):  # y2-y1/x2-x1
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def calculate_angle():  # tan^-1((m2-m1)/(1+m2*m1))
    m1 = calculate_slope(points[0], points[1])
    m2 = calculate_slope(points[0], points[2])
    radian = math.atan((m2 - m1) / 1 + (m1 * m2))
    return abs(int(math.degrees(radian)))


def get_point(event, x, y, _, __):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 4, (0, 255, 0), cv2.FILLED)
        points.append((x, y))
        size = len(points)
        if size == 2:
            cv2.line(img, points[0], points[1], (0, 255, 0), 4)
        elif size == 3:
            cv2.line(img, points[0], points[2], (0, 255, 0), 4)
            # cv2.line(img, points[2], points[1], (0, 255, 0), 4)
        if size == 3:
            angle = calculate_angle()
            cv2.putText(img, str(angle), (points[0][0] - 20, points[0][1] - 20), cv2.FONT_ITALIC, 0.8, (0, 0, 255), 2)
            points.clear()


while True:
    cv2.imshow('frame', img)
    cv2.setMouseCallback('frame', get_point)

    if cv2.waitKey(1) == ord('q'):
        break
