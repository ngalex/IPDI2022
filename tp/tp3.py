from cProfile import label
from email.mime import application
import tkinter
from tkinter import ttk
import tkinter.font as tkFont
import gallery.images as imgsources
import library.imagelibrary as imglib
from PIL import Image, ImageTk
import numpy as np

imageA = imgsources.sources[2]
selectedImageA = Image.open(imageA)

values = ["raiz", "cuadrado", "lineal a trozos"]

def displayImgA(img):
    labelClam =ttk.Label(root, text="Imagen procesada")
    labelClam.place(x=320, y= 0, anchor="nw")
    rgb = imglib.convertToRGB(img)
    photo = ImageTk.PhotoImage(Image.fromarray((rgb*255).astype(np.uint8)))

    labelC = ttk.Label(root, image=photo)
    labelC.image = photo
    labelC.place(x = 320,
                y = 20,
                anchor ="nw")
    return 

def intializeImage ():
    im = imglib.getNormRGB(imageA)
    return imglib.convertToYIQ(im)

def aplicarRaiz():
    imA = imglib.getNormRGB(imageA)
    imA = imglib.convertToYIQ(imA)
    imFiltrado = imA
    imFiltrado[:,:,0] = np.sqrt(imA[:,:,0])
    return imFiltrado

def aplicarCuadrado():
    imA = imglib.getNormRGB(imageA)
    imA = imglib.convertToYIQ(imA)
    imFiltrado = imA
    imFiltrado[:,:,0] = np.square(imA[:,:,0])
    return imFiltrado

def aplicarLinealTrozos():
    imA = imglib.getNormRGB(imageA)
    imA = imglib.convertToYIQ(imA)
    imFiltrado = imA

    xp = [0.2, 0.8]
    yp = [0, 1]
    for i in range(imA[:,:,0].shape[0]):
        for j in range(imA[:,:,0].shape[1]):
            if (imA[i,j,0] > 0.8):
                imFiltrado[i,j,0] = 1.
                continue
            if (imA[i,j,0] < 0.2):
                imFiltrado[i,j,0] = 0.
                continue
            imFiltrado[i,j,0] = np.interp(imA[i,j,0], xp, yp)
                
    return imFiltrado

def aplicarLimite(x): 
    if (x > 0.8):
        return 1.
    if (x < 0.2):
        return 0.
    return x

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

        labelProm =ttk.Label(root, text="Filtros")
        labelProm.place(x=650, y= 0, anchor="nw")
        self.combo = ttk.Combobox(root, values=values)
        self.combo.place(x=650,y=20)
        button = ttk.Button(root, text='Aplicar')
        button.place(x=650, y=50)
        button['command'] = self.btnFiltrarImagen

        labelPhotoA =ttk.Label(root, text="Imagen original")
        labelPhotoA.place(x=0, y= 0, anchor="nw")
        photoA = ImageTk.PhotoImage(selectedImageA)
        labelA = ttk.Label(root, image=photoA)
        labelA.image = photoA
        labelA.place(x = 0.0,
                 y = 20,
                 anchor ="nw")
        labelC = ttk.Label(root, image=None)
        labelC.image = None
        labelC.place(x = 0,
                 y = 280,
                 anchor ="nw")
        displayImgA(intializeImage())


    def btnFiltrarImagen(self, event=None):
        content = self.combo.current()
        if (content == 0):
            im = aplicarRaiz()
            displayImgA(im)
        if (content == 1):
            im = aplicarCuadrado()
            displayImgA(im)
        if (content == 2):
            im = aplicarLinealTrozos()
            displayImgA(im)
        return



if __name__ == "__main__":
    root = tkinter.Tk()
    app = App(root)
    root.mainloop()