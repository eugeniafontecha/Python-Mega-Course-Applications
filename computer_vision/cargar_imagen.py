import cv2

img=cv2.imread("galaxy.jpg",0) #-1 o 1significa imagen a color; 0 escala de grises

print(img)
print(img.shape)
print(img.ndim)

resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[1]/2)))
cv2.imshow("Galaxy",resized_image)
cv2.imwrite("Galaxy_resized.jpg",resized_image)

cv2.waitKey(0) #espera hasta que se presione cualquier tecla. Si se pone otro número espera ese tiempo (ms)
cv2.destroyAllWindows()