import cv2 # type: ignore

img = cv2.imread('images/image.jpeg', 1)
img = cv2.resize(img, (300, 400))
cv2.imshow('Image', img)

def nothing(x):
    pass
#Defines a dummy callback function.
# Trackbars in OpenCV require a callback function even if you don’t want to do anything when the slider moves.

cv2.createTrackbar('BLUE', 'Image', 0, 255, nothing)
#Creates a trackbar (slider) named B in the window "Image".
# Initial value = 0, max value = 255. 
# Calls nothing whenever the slider changes (but it does nothing).
cv2.createTrackbar('GREEN', 'Image', 0, 255, nothing)
cv2.createTrackbar('RED', 'Image', 0, 255, nothing)

while True:
    cv2.imshow('Image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        #If the pressed key is 27, that’s ESC, so it breaks the loop and exits.
        break
    b = cv2.getTrackbarPos('BLUE', 'Image')
    #Reads the current slider value of trackbar B (0–255).
    g = cv2.getTrackbarPos('GREEN', 'Image')    
    r = cv2.getTrackbarPos('RED', 'Image')
    cv2.circle(img, (150, 200), 50, (b, g, r), -1)
    #Draws a filled circle on the image.
    # Center = (150, 200) (x, y).
    # Radius = 50.
    # Color = (b, g, r) (OpenCV uses BGR, not RGB).
    # Thickness = -1 means filled circle.
cv2.destroyAllWindows()