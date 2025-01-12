import cv2   # type: ignore



# Read the input image
image = cv2.imread("assignment-001-given.jpg")

# Draw a green rectangle around the license plate
# Rectangle coordinates: top-left (50, 200), bottom-right (500, 350) - adjust as per requirement
cv2.rectangle(image, (250, 200), (1000, 930), (0, 255, 0), 10)


cv2.putText(image, 'RAH972U', (887, 180), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)

# Save the annotated image
cv2.imwrite("assignment-001-correction-image.jpg", image)

# Display the image for verification (optional)
cv2.imshow('Annotated Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


