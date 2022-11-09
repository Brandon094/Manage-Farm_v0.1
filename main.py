import tkinter as tk 
from tkinter import ttk
from funciones import cosecha,limpia,fungicida,abono
from PIL import ImageTk, Image

# confuguracion de la ventana
root = tk.Tk()
root.title("Manage Farm")
root.config(width=1340, height=740)

# estilos 
styloButton = ttk.Style()
styloButton.configure("TButton", foreground="black",background="red",width="15", height="5")

# Imagen de fondo
img_Fondo = ImageTk.PhotoImage(Image.open("img/Backgound.jpg"))
img_lbl = ttk.Label(root, image=img_Fondo)
img_lbl.pack()

# etiquetas de titulo
etiqueta_Titulo = ttk.Label(text="Manage Farm")
etiqueta_Titulo.place(relx = 0.47, rely = 0.05)

#etiqueta de info funciones
etiqute_InfoF = ttk.Label(text="Selecione la funcion que desea realizar.\nFunciones:")
etiqute_InfoF.place(relx = 0.02, rely = 0.1)

# botonoes de funciones
b1_Cosecha = ttk.Button(text="Cosecha",command=cosecha)
b1_Cosecha.place(relx = 0.02, rely = 0.2)

b2_Limpia = ttk.Button(text="Limpia", command=limpia)
b2_Limpia.place(relx = 0.02, rely = 0.24)

b3_Fungicida = ttk.Button(text="Fungicida", command=fungicida)
b3_Fungicida.place(relx = 0.02, rely = 0.28)

b4_Abono = ttk.Button(text="Abono", command=abono)
b4_Abono.place(relx = 0.02, rely =0.32)

# etiqueta de info base datos
etiqute_dataBase = ttk.Label(text="Selecione la base de datos que desea revizar.\nBases de datos:")
etiqute_dataBase.place(relx = 0.80, rely = 0.1)

# Botones de bases de datos
b5_BaseGastos = ttk.Button(text="Gastos")
b5_BaseGastos.place(relx = 0.80, rely = 0.2)

b6_BaseProduccion = ttk.Button(text="Ganancias")
b6_BaseProduccion.place(relx = 0.80, rely = 0.24)

# etiqueta Copyrigth
etiqueta_Copyright = ttk.Label(text="CopyRight 2022 By Brandon Daza")
etiqueta_Copyright.place(relx = 0.43, rely = 0.95)
root.state('zoomed')
root.mainloop()