import tkinter as tk
import tkinter.font as tkFont
import gallery.images as imgsources
import library.imagelibrary as imglib
from PIL import Image, ImageTk
import numpy as np
import imageio

imageA = imgsources.sources[2]
imageB = imgsources.sources[3]

selectedImageA = Image.open(imageA)
selectedImageB = Image.open(imageB)

class App:
    def __init__(self, root):
        #setting title
        root.title("TP2")
        #setting window size
        width=800
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_224=tk.Button(root)
        GButton_224["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_224["font"] = ft
        GButton_224["fg"] = "#000000"
        GButton_224["justify"] = "center"
        GButton_224["text"] = "Cuasi suma RGB"
        GButton_224.place(x=660,y=20,width=115,height=35)
        GButton_224["command"] = self.btnCuasiSumaRGBClick

        GButton_265=tk.Button(root)
        GButton_265["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_265["font"] = ft
        GButton_265["fg"] = "#000000"
        GButton_265["justify"] = "center"
        GButton_265["text"] = "Cuasi resta RGB"
        GButton_265.place(x=660,y=60,width=115,height=34)
        GButton_265["command"] = self.btnCuasiRestaRGBClick

        GButton_265=tk.Button(root)
        GButton_265["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_265["font"] = ft
        GButton_265["fg"] = "#000000"
        GButton_265["justify"] = "center"
        GButton_265["text"] = "Cuasi suma YIQ"
        GButton_265.place(x=660,y=100,width=115,height=34)
        GButton_265["command"] = self.btnCuasiSumaYIQClick

        GButton_265=tk.Button(root)
        GButton_265["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_265["font"] = ft
        GButton_265["fg"] = "#000000"
        GButton_265["justify"] = "center"
        GButton_265["text"] = "Cuasi resta YIQ"
        GButton_265.place(x=660,y=140,width=115,height=34)
        GButton_265["command"] = self.btnCuasiRestaYIQClick

        GButton_265=tk.Button(root)
        GButton_265["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_265["font"] = ft
        GButton_265["fg"] = "#000000"
        GButton_265["justify"] = "center"
        GButton_265["text"] = "Producto YIQ"
        GButton_265.place(x=660,y=180,width=115,height=34)
        GButton_265["command"] = self.btnProdYIQClick
        
        GButton_265=tk.Button(root)
        GButton_265["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_265["font"] = ft
        GButton_265["fg"] = "#000000"
        GButton_265["justify"] = "center"
        GButton_265["text"] = "Cociente YIQ"
        GButton_265.place(x=660,y=220,width=115,height=34)
        GButton_265["command"] = self.btnDivYIQClick

        photoA = ImageTk.PhotoImage(selectedImageA)
        photoB = ImageTk.PhotoImage(selectedImageB)
        
        labelA = tk.Label(root, image=photoA)
        labelA.image = photoA
        labelA.place(x = 0.0,
                 y = 0.0,
                 anchor ="nw")
        labelB = tk.Label(root, image=photoB)
        labelB.image = photoB
        labelB.place(x = 300,
                 y = 0.0,
                 anchor ="nw")

        labelC = tk.Label(root, image=None)
        labelC.image = None
        labelC.place(x = 150,
                 y = 280,
                 anchor ="nw")
        # label.pack()

    def btnCuasiSumaRGBClick(self):
        imA = imglib.getNormRGB(imageA)
        imB = imglib.getNormRGB(imageB)
        imC = imA + imB[:,:,0:3]
        imC = np.clip(imC,0.,1.)
        imglib.plot(imC)
        imD = (imA + imB[:,:,0:3])/2
        imglib.plot(imD)

        photoC = ImageTk.PhotoImage(imageio.imopen(imC))
        labelC = tk.Label(root, image=photoC)
        labelC.image = photoC
        labelC.place(x = 150,
                 y = 280,
                 anchor ="nw")

    def btnCuasiRestaRGBClick(self):
        imA = imglib.getNormRGB(imageA)
        imB = imglib.getNormRGB(imageB)
        imC = imA - imB[:,:,0:3]
        imC = np.clip(imC,0.,1.)
        imglib.plot(imC)
        imD = (imC)/2
        imglib.plot(imD)

        photoC = ImageTk.PhotoImage(imageio.imopen(imC))
        labelC = tk.Label(root, image=photoC)
        labelC.image = photoC
        labelC.place(x = 150,
                 y = 280,
                 anchor ="nw")

    def btnCuasiSumaYIQClick(self):
        imA = imglib.convertToYIQ(imglib.getNormRGB(imageA))
        imB = imglib.convertToYIQ(imglib.getNormRGB(imageB))
        imC = np.copy(imA)
        imC[:,:,0] = imA[:,:,0] + imB[:,:,0]
        imC = imglib.luminancia(1, imC)
        imC[:,:,1] = (imA[:,:,0]*imA[:,:,1]+imB[:,:,0]*imB[:,:,1])/(imA[:,:,0]+imB[:,:,1])
        imC[:,:,2] = (imA[:,:,0]*imA[:,:,2]+imB[:,:,0]*imB[:,:,2])/(imA[:,:,0]+imB[:,:,1])
        imglib.plot(imglib.convertToRGB(imC))

        imC = np.copy(imA)
        imC[:,:,0] = (imA[:,:,0] + imB[:,:,0])/2
        imC[:,:,1] = (imA[:,:,0]*imA[:,:,1]+imB[:,:,0]*imB[:,:,1])/(imA[:,:,0]+imB[:,:,1])
        imC[:,:,2] = (imA[:,:,0]*imA[:,:,2]+imB[:,:,0]*imB[:,:,2])/(imA[:,:,0]+imB[:,:,1])
        imglib.plot(imglib.convertToRGB(imC))

    def btnCuasiRestaYIQClick(self):
        imA = imglib.convertToYIQ(imglib.getNormRGB(imageA))
        imB = imglib.convertToYIQ(imglib.getNormRGB(imageB))
        imC = np.copy(imA)
        imC[:,:,0] = imA[:,:,0] - imB[:,:,0]
        imC = imglib.luminancia(1, imC)
        imC[:,:,1] = (imA[:,:,0]*imA[:,:,1]+imB[:,:,0]*imB[:,:,1])/(imA[:,:,0]+imB[:,:,1])
        imC[:,:,2] = (imA[:,:,0]*imA[:,:,2]+imB[:,:,0]*imB[:,:,2])/(imA[:,:,0]+imB[:,:,1])
        imglib.plot(imglib.convertToRGB(imC))

        imC = np.copy(imA)
        imC[:,:,0] = (imA[:,:,0] - imB[:,:,0])/2
        imC = imglib.luminancia(1, imC)
        imC[:,:,1] = (imA[:,:,0]*imA[:,:,1]+imB[:,:,0]*imB[:,:,1])/(imA[:,:,0]+imB[:,:,1])
        imC[:,:,2] = (imA[:,:,0]*imA[:,:,2]+imB[:,:,0]*imB[:,:,2])/(imA[:,:,0]+imB[:,:,1])
        imglib.plot(imglib.convertToRGB(imC))

    def btnProdYIQClick(self):
        imA = imglib.convertToYIQ(imglib.getNormRGB(imageA))
        imB = imglib.convertToYIQ(imglib.getNormRGB(imageB))
        imC = np.copy(imA)
        imC[:,:,0] = imA[:,:,0] * imB[:,:,0]
        imC = imglib.luminancia(1, imC)
        imC[:,:,1] = (imA[:,:,0]*imA[:,:,1]+imB[:,:,0]*imB[:,:,1])/(imA[:,:,0]+imB[:,:,1])
        imC[:,:,2] = (imA[:,:,0]*imA[:,:,2]+imB[:,:,0]*imB[:,:,2])/(imA[:,:,0]+imB[:,:,1])
        imglib.plot(imglib.convertToRGB(imC))

    def btnDivYIQClick(self):
        imA = imglib.convertToYIQ(imglib.getNormRGB(imageA))
        imB = imglib.convertToYIQ(imglib.getNormRGB(imageB))
        aux = []
        for i in range(len(imB[:,:,0])):
            for j in range(len(imB[:,:,0])):
                if (imB[i,j,0]>0):
                    aux.append(imB[i,j,0])
        minB = np.min(aux)
        imB[:,:,0] = np.clip(imB[:,:,0], minB, 1.)
        imC = np.copy(imA)
        imC[:,:,0] /= imB[:,:,0]
        imC = imglib.luminancia(1, imC)
        imC[:,:,1] = (imA[:,:,0]*imA[:,:,1]+imB[:,:,0]*imB[:,:,1])/(imA[:,:,0]+imB[:,:,1])
        imC[:,:,2] = (imA[:,:,0]*imA[:,:,2]+imB[:,:,0]*imB[:,:,2])/(imA[:,:,0]+imB[:,:,1])
        imglib.plot(imglib.convertToRGB(imC))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
