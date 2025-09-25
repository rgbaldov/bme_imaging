import cv2
import math

img = cv2.imread("xray.jpeg")
clone = img.copy()

points = []

def click_event(event, x, y, flags, param):
    global points, img
    
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))

        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        
        if len(points) == 2:
            cv2.line(img, points[0], points[1], (0, 255, 0), 2)
            
            length = math.dist(points[0], points[1])
            
            cv2.putText(img, f"{length:.2f} px",
                        (points[0][0], points[0][1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (255, 255, 255), 2)
            
            points = []
        
        cv2.imshow("Measure", img)

cv2.imshow("Measure", img)
cv2.setMouseCallback("Measure", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
