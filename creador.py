import tkinter
import sys
import os
from tkinter import *

def writeFile():
    file = open('nombre.txt','a+')
    file.write(metinF.get() + '\n')
    file.close()

    file = open('urls.txt','a+')
    file.write(metinFu.get() + '\n')
    file.close()  

    butonWrite.config(text = 'Agregado!')

def run():
    for i in range(20):
      exec(open("py.py").read())
    buttonRun.config(text = 'Generando archivos!')

gui = Tk()
gui.title("Creador de HTML")

titulo_nombres = Label(text = 'Ingresar los nombres de los juegos').grid(row=0, column=0)
metinF = Entry(gui, width=60)
metinF.grid(row=1, column=0, padx=10, pady=10, columnspan=1, sticky=S+E+W)

titulo_urls = Label(text = 'Ingresar las URLS de los juegos').grid(row=2, column=0)
metinFu = Entry(gui, width=60)
metinFu.grid(row=3, column=0, padx=10, pady=10, columnspan=1, sticky=S+E+W)

butonWrite = Button(gui)
butonWrite.config(text = 'Agregar al documento', command = writeFile)
butonWrite.grid(row=4, column=0)

buttonRun = Button(gui)
buttonRun.config(text = 'Crear los archivos', command = run)
buttonRun.grid(row=5, column=0,  padx=10, pady=10)

gui.mainloop()
