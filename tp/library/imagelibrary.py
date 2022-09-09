from multiprocessing.dummy import Array
import sys 
import numpy as np 
import imageio.v2 as imageio
import matplotlib.pyplot as plt

def getNormRGB(path):
    im = imageio.imread(path)
    im = np.clip(im/255.,0.,1)
    return im

# image: RGB normalizado 
def convertToYIQ(image):
    red = image[:,:,0]
    green = image[:,:,1]
    blue = image[:,:,2]
    y = np.array(0.299*red + 0.587*green + 0.114*blue).clip(0.,1.)
    i = np.array(0.595716*red - 0.274453*green - 0.321263*blue).clip(-0.5957, 0.5957)
    q = np.array(0.211456*red - 0.522591*green + 0.311135*blue).clip( -0.5226, 0.5226)
    return np.dstack((y,i,q))

def luminancia(a, yiq):
    yiq[:,:,0] = yiq[:,:,0]*a
    yiq = np.clip(yiq, 0.,1.)
    return yiq

def saturacion(b, yiq):
    yiq[:,:,1] = yiq[:,:,0]*b
    yiq[:,:,1] = np.clip(yiq[:,:,1], -0.5957, 0.5957)
    yiq[:,:,2] = yiq[:,:,2]*b
    yiq[:,:,2] = np.clip(yiq[:,:,2], -0.5226, 0.5226)
    return yiq

def convertToRGB(yiq):
    y = yiq[:,:,0]
    i = yiq[:,:,1]
    q = yiq[:,:,2]

    red = (y + 0.9663*i + 0.6210*q)
    blue = (y -0.2721*i -0.6474*q)
    green = (y -1.1070*i + 1.7046*q)

    return np.dstack((red,blue,green)).clip(0.,1.)

def plot(img):
    plt.imshow(img)
    plt.show()