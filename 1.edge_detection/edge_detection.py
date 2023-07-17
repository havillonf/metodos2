import numpy
import imageio.v2 as imageio

img_path = "./kitten.jpg"
img_file = imageio.imread(img_path)

img = numpy.asarray(img_file)
img_h = len(img)
img_w = len(img[0])

#aplicar filtro gaussiano

#aplicar filtro convolucional de gradiente

#matriz A = filtro de sobel para direcao x

#matriz B = filtro de sobel para direcao y

#matriz C = sqrt(A^2+B^2) 

#escolher um valor para o treshold e aplicar