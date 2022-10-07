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
    "Erosión 3x3",
    "Dilatación 3x3",
    "Apertura",
    "Cierre",
    "Borde morfológico",
    "Mediana"
]

def intializeImage ():
    im = imglib.getNormRGB(imageA)
    return imglib.convertToYIQ(im)

target_im = intializeImage()

def displayImgB(img):
    labelClam =ttk.Label(root, text="Imagen procesada")
    labelClam.place(x=500, y= 0, anchor="nw")
    rgb = imglib.convertToRGB(img)[:,:,]
    photo = ImageTk.PhotoImage(Image.fromarray((rgb*255).astype(np.uint8)))

    labelB = ttk.Label(root, image=photo)
    labelB.image = photo
    labelB.place(x = 500,
                y = 20,
                anchor ="nw")
    return 

def applyWindowValue(im, value): 
    size = np.shape(im)
    n = size[0]-2
    m = size[1]-2
    result = im
    print(n,m)
    for i in range (1, n):
        for j in (1, m):
            if (np.array(im[i-1:i+2,j-1:j+2,0]).any() != np.full((3,3), value).any()):
                result[i,j,0] = value
                # print("original:",np.shape(result[i-1:i+2,j-1:j+2,0]))
                # result[i-1:i+2,j-1:j+2,0] = np.full((3,3), value)
                # print("procesado:",np.shape(result[i-1:i+2,j-1:j+2,0]))

    return result

class App:
    def __init__(self, root):
        #setting title
        root.title("TP4")
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
        button['command'] = self.btnProcesarImagen

        labelB = ttk.Label(root, image=None)
        labelB.image = None
        labelB.place(x = 0,
                 y = 280,
                 anchor ="nw")
        displayImgB(intializeImage())

    def btnProcesarImagen(self, event=None):
        content = self.combo.current()
        if (content == 0):
            im = intializeImage()
            im = applyWindowValue(im, 0.)
            im = displayImgB(im)

        if (content == 1):
            im = intializeImage()
            im = applyWindowValue(im, 1.)
            im = displayImgB(im)
            return

if __name__ == "__main__":
    root = tkinter.Tk()
    app = App(root)
    root.mainloop()