import imageio.v2 as imageio
import numpy as np 
import matplotlib.pyplot as plt

# Paso 2
def convertToYIQ(image):
    red = image[:,:,0]
    green = image[:,:,1]
    blue = image[:,:,2]
    y = (0.299*red + 0.587*green + 0.114*blue)
    i = (0.595716*red - 0.274453*green - 0.321263*blue)
    q = (0.211456*red - 0.522591*green + 0.311135*blue)
    return np.dstack((y,i,q))

# Paso 3 y 5
def luminancia(a, yiq):
    yiq[:,:,0] = yiq[:,:,0]*a
    yiq = np.clip(yiq, 0.,1.)
    return yiq

# Paso 4 y 6
def saturacion(b, yiq):
    yiq[:,:,1] = yiq[:,:,0]*b
    yiq[:,:,1] = np.clip(yiq[:,:,1], -0.5957, 0.5957)
    yiq[:,:,2] = yiq[:,:,2]*b
    yiq[:,:,2] = np.clip(yiq[:,:,2], -0.5226, 0.5226)
    return yiq

# Paso 7
def convertToRGB(yiq):
    y = yiq[:,:,0]
    i = yiq[:,:,1]
    q = yiq[:,:,2]

    red = (y + 0.9663*i + 0.6210*q)
    blue = (y -0.2721*i -0.6474*q)
    green = (y -1.1070*i + 1.7046*q)

    return np.dstack((red,blue,green))

# Paso 8
def plot(img):
    plt.imshow(img)
    plt.show()





# Principal. Aplicando la actividad con ejemplos para Luminancia 0.4, saturacion de 0
# y la combinacion de ambos

im = imageio.imread('./tp1/lena128C.png')
# Paso 1 normalize rgb
im = np.clip(im/255.,0.,1.)

yiq = convertToYIQ(im)

# Luminancia
yiqLum = yiq
yiqLum = luminancia(0.4, yiqLum)
rgb = convertToRGB(yiqLum)
plot(rgb)

# Saturacion
yiqSat = yiq
yiqSat = saturacion(0, yiqSat)
rgb = convertToRGB(yiqSat)
plot(rgb)

# Hibrido
comb = yiq
comb = luminancia(0.7, comb)
comb = saturacion(1.5, comb)
rgb = convertToRGB(comb)
plot(rgb)