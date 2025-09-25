import cv2
import math

img = cv2.imread("brain.jpg")
clone = img.copy()

points = []

pixels_per_cm = 15.45   # divide px/skull size (depends on your image/dpi)

def click_event(event, x, y, flags, param):
    global points, img
    
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        
        if len(points) == 2:
            cv2.line(img, points[0], points[1], (0, 255, 0), 2)
            
            length_px = math.dist(points[0], points[1])
            
            length_cm = length_px / pixels_per_cm
            
            cv2.putText(img, f"{length_cm:.2f} cm",
                        (points[0][0], points[0][1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (255, 255, 255), 2)
            
            points = []
        
        cv2.imshow("Measure", img)

cv2.imshow("Measure", img)
cv2.setMouseCallback("Measure", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
