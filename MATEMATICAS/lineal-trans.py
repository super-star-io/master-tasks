import numpy as np 
import cv2 
import sys

imagen=cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
#print("imagen. shape=", imagen. shape)
#invertir la imagen 
imagen=255-imagen
#mostrar la imagen 
cv2.imshow("imagen", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

T=np.array(imagen)

#print ("T=", T)
S,V,D=np.linalg.svd(T)

V=np.diag(V)

print("V=", V)


