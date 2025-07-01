import cv2
import numpy as np

drawing = False
last_point = None
brush_color = (0, 0, 255) 
brush_size = 5

def draw(event, x, y, flags, param):
    global drawing, last_point
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        last_point = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        cv2.line(canvas, last_point, (x, y), brush_color, brush_size)
        last_point = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

cap = cv2.VideoCapture(0)
cv2.namedWindow('PaintCam')
ret, frame = cap.read()
canvas = np.zeros_like(frame)

cv2.setMouseCallback('PaintCam', draw)

print("Draw with mouse! Press 'c' to clear, 'q' to quit.")

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) 
    display = cv2.addWeighted(frame, 0.7, canvas, 1, 0)
    cv2.imshow('PaintCam', display)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        canvas[:] = 0  

cap.release()
cv2.destroyAllWindows()
