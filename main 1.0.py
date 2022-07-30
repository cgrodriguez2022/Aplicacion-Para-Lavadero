from importlib.resources import path
import sys
from tkinter import END, Button, Label, PhotoImage, Tk, filedialog
from pathlib import Path
import os
from datetime import datetime
import pandas as pd
from tabula import read_pdf
import tabula

version = 'v 1.0'

def abrirArchivo():

    archivo = filedialog.askopenfilename(title="Seleccionar el pdf", filetypes=(("Archivos pdf","*.pdf"),
    ("Todos los archivos","*.*")))#, initialdir="C:/" x si quiero una ruta especifica
    print(str(archivo))
    rutaArchivo = (str(archivo))

    df = tabula.read_pdf(rutaArchivo, pages='all')[0]
    
    date = datetime.now()
    fecha_hora = (date.strftime("%d %B-%Y-%H%M%S"))
    fecha = (str(fecha_hora))
    nombre_a_salida = ("Archivos/Aconvertido-"+fecha+".csv")
    tabula.convert_into(rutaArchivo, nombre_a_salida, output_format="csv", pages='all')
  
    Label(ventana_registro, text="Archivo convertido con éxito", fg="green", font=("Comic Sans MS", 10, "bold")).pack()



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def Lavadero_Procrear():
    global ventana_registro
    ventana_registro = Tk()

    carpeta_Principal = ("Archivos")
    carpeta_pdf = ("PDF")
    Generar_carpetas = Path(carpeta_Principal)
    Generar_carpetas.mkdir(parents=True,exist_ok=True)
    Generar_carpetas = Path(carpeta_pdf)
    Generar_carpetas.mkdir(parents=True,exist_ok=True)

    path = resource_path('lavadero.png')
    imagen = PhotoImage(file=path)
    background = Label(image = imagen)
    background.pack()
    ventana_registro.title("Convertir a CSV"+"----"+version)
    ventana_registro.geometry("300x350")

    path = resource_path('lavadero.ico')
    ventana_registro.iconbitmap(path)
    colorGris="DarkGrey" #Color para boton

    Label(ventana_registro).pack()
    Button(ventana_registro, text="Cargar PDF", width=30, height=2, bg=colorGris, command = abrirArchivo).pack() #BOTÓN "CargarPdf"

    ventana_registro.mainloop()

Lavadero_Procrear()


 
 
