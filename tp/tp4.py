from cProfile import label
from email.mime import application
import tkinter
from tkinter import ttk
import tkinter.font as tkFont
import gallery.images as imgsources
import library.imagelibrary as imglib
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt

imageA = imgsources.sources[4]
selectedImageA = Image.open(imageA)
values = [
    "Plano",
    "Bartlett 3x3",
    "Bartlett 5x5",
    "Bartlett 7x7",
    "Gussiano 5x5",
    "Gussiano 7x7",
    "Laplaciano v4",
    "Laplaciano v8",
    "Sobel Norte",
    "Sobel Noreste",
    "Sobel Este",
    "Sobel Sudeste",
    "Sobel Sur",
    "Sobel Suroeste",
    "Sobel Oeste",
    "Sobel Noroeste",
    "Pasabanda",
    "Pasaaltos 0,2",
    "Pasaaltos 0,4"
]

def displayImgB(img):
    labelClam =ttk.Label(root, text="Imagen procesada")
    labelClam.place(x=500, y= 0, anchor="nw")
    rgb = imglib.convertToRGB(img)
    photo = ImageTk.PhotoImage(Image.fromarray((rgb*255).astype(np.uint8)))

    labelB = ttk.Label(root, image=photo)
    labelB.image = photo
    labelB.place(x = 500,
                y = 20,
                anchor ="nw")
    return 

def intializeImage ():
    im = imglib.getNormRGB(imageA)
    return imglib.convertToYIQ(im)

def applyFilter(im, kernel, factor): 
    size = np.shape(im)
    n = size[0]
    m = size[1]
    kernelSize = np.shape(kernel)
    kn = kernelSize[0]
    semikn = int(kn/2)
    km = kernelSize[1]
    semikm = int(km/2)

    aux = im
    aux = np.vstack([aux[0:semikn,:], aux])
    aux = np.hstack([aux[:,m-semikm:m],aux])
    aux = np.vstack([aux[n-semikn:n,:], aux])
    aux = np.hstack([aux[:,0:semikm],aux])

    size = np.shape(aux)
    n = size[0]
    m = size[1]

    result = im
    for i in range(1+semikn, n-semikn+1):
        for j in range(1+semikm, m-semikm+1):
            result[i-semikn-1,j-semikm-1,0] = getKernelValue(aux[i-semikn-1:i+semikn, j-semikm-1:j+semikm,0], kernel, factor)
    return result

def getKernelValue(subm, kernel, factor):
    size = np.shape(kernel)
    n = size[0]
    m = size[1]
    res = 0
    for i in range(n):
        for j in range(m):
                res += (subm[i,j]*kernel[i,j])/factor
    
    return np.clip(res,0.,1.)


class App:
    def __init__(self, root):
        #setting title
        root.title("TP3")
        #setting window size
        width=800
        height=300
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        labelPhotoA =ttk.Label(root, text="Imagen original")
        labelPhotoA.place(x=0, y= 0, anchor="nw")
        photoA = ImageTk.PhotoImage(selectedImageA)
        labelA = ttk.Label(root, image=photoA)
        labelA.image = photoA
        labelA.place(x = 0.0,
                 y = 20,
                 anchor ="nw")

        labelProm =ttk.Label(root, text="Filtros")
        labelProm.place(x=320, y= 100, anchor="nw")
        self.combo = ttk.Combobox(root, values=values)
        self.combo.place(x=320,y= 120)
        button = ttk.Button(root, text='Aplicar')
        button.place(x=320, y=150)
        button['command'] = self.btnFiltrarImagen


        labelB = ttk.Label(root, image=None)
        labelB.image = None
        labelB.place(x = 0,
                 y = 280,
                 anchor ="nw")
        displayImgB(intializeImage())
        


    def btnFiltrarImagen(self, event=None):
        content = self.combo.current()
        if (content == 0):
            kernel = np.matrix([[1,1,1],[1,1,1],[1,1,1]])
            factor = np.sum(kernel)
            im = intializeImage()
            im = displayImgB(applyFilter(im, kernel, factor))
            return
        if (content == 1):
            kernel = np.matrix([[1,2,1],[2,4,2],[1,2,1]])
            factor = np.sum(kernel)
            im = intializeImage()
            im = displayImgB(applyFilter(im, kernel, factor))
            return
        if (content == 2):
            kernel = np.matrix([[1,2,3,2,1],[2,3,4,3,2],[3,4,5,3,2],[2,3,4,3,2],[1,2,3,2,1]])
            factor = np.sum(kernel)
            im = intializeImage()
            im = displayImgB(applyFilter(im, kernel, factor))
            return
        if (content == 3):
            kernel = np.matrix([[1,2,3,4,3,2,1],[2,3,4,5,4,3,2],[3,4,5,6,5,4,3],[4,5,6,7,6,5,4],[3,4,5,6,5,4,3],[2,3,4,5,4,3,2],[1,2,3,4,3,2,1]])
            factor = np.sum(kernel)
            im = intializeImage()
            im = displayImgB(applyFilter(im, kernel, factor))
            return
        if (content == 4):
            kernel = np.matrix([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,4,1]])
            factor = np.sum(kernel)
            im = intializeImage()
            im = displayImgB(applyFilter(im, kernel, factor))
            return
        if (content == 5):
            kernel = np.matrix([[1,6,15,20,15,6,1],[6,36,90,120,90,36,6],[15,90,225,300,225,90,15],[20,120,300,400,300,120,20],[15,90,225,300,225,90,15],[6,36,90,120,90,36,6],[1,6,15,20,15,6,1]])
            factor = np.sum(kernel)
            im = intializeImage()
            im = displayImgB(applyFilter(im, kernel, factor))
            return
        if (content == 6):
            kernel = np.matrix([[0,-1,0],[-1,4,-1],[0,-1,0]])
            im = intializeImage()
            im = displayImgB(applyFilter(im, kernel,1))
            return
        if (content == 7):
            kernel = np.matrix([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
            im = intializeImage()
            im = displayImgB(applyFilter(im, kernel,1))
            return
        if (content == 8):
            kernel = np.matrix([[-1,-2,-1],[0,0,0],[1,2,1]])
            im = intializeImage()
            im = displayImgB(applyFilter(im, kernel,1))
            return
        if (content == 9):
            kernel = np.matrix([[0,-1,-2],[1,0,-1],[2,1,0]])
            im = intializeImage()
            im = displayImgB(applyFilter(im, kernel,1))
            return
        if (content == 10):
            kernel = np.matrix([[1,0,-1],[2,0,-2],[1,0,-1]])
            im = intializeImage()
            im = displayImgB(applyFilter(im, kernel,1))
            return
        if (content == 11):
            kernel = np.matrix([[2,1,0],[1,0,-1],[0,-1,-2]])
            im = intializeImage()
            im = displayImgB(applyFilter(im, kernel,1))
            return
        if (content == 12):
            kernel = np.matrix([[1,2,1],[0,0,0],[-1,-2,-1]])
            im = intializeImage()
            im = displayImgB(applyFilter(im, kernel,1))
            return
        if (content == 13):
            kernel = np.matrix([[0,1,2],[-1,0,1],[-2,-1,0]])
            im = intializeImage()
            im = displayImgB(applyFilter(im, kernel,1))
            return
        if (content == 14):
            kernel = np.matrix([[-1,0,1],[-2,0,2],[-1,0,1]])
            im = intializeImage()
            im = displayImgB(applyFilter(im, kernel,1))
            return
        if (content == 15):
            kernel = np.matrix([[-2,-1,0],[-1,0,1],[0,1,2]])
            im = intializeImage()
            im = displayImgB(applyFilter(im, kernel,1))
            return
        if (content == 16):
            gauss5 = np.matrix([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,4,1]])
            gauss7 = np.matrix([[1,6,15,20,15,6,1],[6,36,90,120,90,36,6],[15,90,225,300,225,90,15],[20,120,300,400,300,120,20],[15,90,225,300,225,90,15],[6,36,90,120,90,36,6],[1,6,15,20,15,6,1]])
            dif_gauss = gauss5 - gauss7[1:6, 1:6]
            factor = np.sum(dif_gauss)
            im = intializeImage()
            im = displayImgB(applyFilter(im, dif_gauss,factor))
            return
        if (content == 17):
            vec8 = [[-1.0,-1.0,-1.0],[-1.0,8.0,-1.0],[-1.0,-1.0,-1.0]]
            kernel = [[0.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,0.0]]+(vec8*np.full((3,3),0.2))
            im = intializeImage()
            im = displayImgB(applyFilter(im, kernel,1))
            return
        if (content == 168):
            vec8 = [[-1.0,-1.0,-1.0],[-1.0,8.0,-1.0],[-1.0,-1.0,-1.0]]
            kernel = [[0.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,0.0]]+(vec8*np.full((3,3),0.4))
            im = intializeImage()
            im = displayImgB(applyFilter(im, kernel,1))
            return
        return


if __name__ == "__main__":
    root = tkinter.Tk()
    app = App(root)
    root.mainloop()