import cv2   # type: ignore



# Read the input image
image = cv2.imread("assignment-001-given.jpg")

overlay = image.copy()

text = "RAH972U"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2
font_thickness = 3
text_color = (0, 255, 0)  
bg_color = (0, 0, 0)     
opacity = 0.6             

# Text position
text_x, text_y = 887, 170

# Get the size of the text
(text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, font_thickness)

# Coordinates for the rectangle (background)
rect_top_left = (text_x - 10, text_y - text_height - 10)  
rect_bottom_right = (text_x + text_width + 10, text_y + baseline)

# Draw the filled rectangle on the overlay
cv2.rectangle(overlay, rect_top_left, rect_bottom_right, bg_color, -1)

# Blend the overlay with the original image
cv2.addWeighted(overlay, opacity, image, 1 - opacity, 0, image)

# Draw the text on the image (after blending)
cv2.putText(image, text, (text_x, text_y), font, font_scale, text_color, font_thickness)

# Save the annotated image
cv2.imwrite("assignment-001-correction-image.jpg", image)


# Draw a green rectangle around the license plate
# Rectangle coordinates: top-left (50, 200), bottom-right (500, 350) - adjust as per requirement
cv2.rectangle(image, (250, 200), (1000, 930), (0, 255, 0), 10)


# Save the annotated image
cv2.imwrite("assignment-001-correction-image.jpg", image)

# Display the image for verification (optional)
cv2.imshow('Annotated Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


