import cv2

def draw_rectangle(img, cnt_point, thickness=3):
    
    output = img.copy()

    p1 = (cnt_point[0]-50, cnt_point[1]-50)
    p2 = (cnt_point[0]+50, cnt_point[1]+50)

    output = cv2.rectangle(output, p1, p2, (0, 255, 0), thickness)

    return output


def draw_circle(img, pnt, radius=50, thickness=3):

    output = img.copy()

    output = cv2.circle(output, pnt, radius, (0,0,255), thickness)

    return output

    
