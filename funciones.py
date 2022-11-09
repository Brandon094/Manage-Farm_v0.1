import tkinter as tk
from tkinter import ttk

def bultosAbono():
    pass

def cantidadFungicida():
    pass

# Ventana Cosecha
def cosecha():
    #Funcion pago
    def pago():
        kilos = caja_kilos.get()
        tarifa = caja_tarifa.get()
        totalPagar = float(kilos)*float(tarifa)

        etiqueta_Total.config(text=f"El total a pagar es: ${totalPagar}")

    # Configuracion ventana
    VentanaCosecha = tk.Toplevel()
    VentanaCosecha.title("Cosecha")
    VentanaCosecha.geometry("400x200+480+250")

    titulo = ttk.Label(VentanaCosecha, text="Calcular pago recolectores")
    titulo.place(relx= 0.35, rely=0.1)

    etiqueta_Kilos = ttk.Label(VentanaCosecha, text="Digite los kilos recolectados:")
    etiqueta_Kilos.place(relx=0.1, rely=0.3)

    caja_kilos = ttk.Entry(VentanaCosecha,justify=tk.CENTER)
    caja_kilos.place(relx=0.6, rely=0.3)

    etiqueta_tarifa = ttk.Label(VentanaCosecha,text="Digite la tarifa:")
    etiqueta_tarifa.place(relx=0.1,rely=0.5)

    caja_tarifa = ttk.Entry(VentanaCosecha,justify=tk.CENTER)
    caja_tarifa.place(relx=0.6, rely=0.5)

    etiqueta_Total = ttk.Label(VentanaCosecha,text="El total a pagar es: $ 0.00")
    etiqueta_Total.place(relx= 0.1, rely= 0.7)
    
    boton_calcular = ttk.Button(VentanaCosecha,text="Calcular", command=pago)
    boton_calcular.place(relx = 0.6, rely = 0.7)

    VentanaCosecha.resizable(0,0)
    VentanaCosecha.focus()
    VentanaCosecha.grab_set()

# Ventana Limpia
def limpia():
    #Funcion pago
    def pago():
        dias = caja_dias.get()
        tarifa = caja_tarifa.get()
        totalPagar = float(dias)*float(tarifa)

        etiqueta_Total.config(text=f"El total a pagar es: ${totalPagar}")

    VentanaLimpia = tk.Toplevel()
    VentanaLimpia.title("Limpia")
    VentanaLimpia.geometry("400x200+480+250")

    titulo = ttk.Label(VentanaLimpia, text="Calcular pago limpia")
    titulo.place(relx=0.35, rely=0.1)

    etiqueta_Dias = ttk.Label(VentanaLimpia, text="Digite el total de dias trabajados:")
    etiqueta_Dias.place(relx=0.1, rely=0.3)

    caja_dias = ttk.Entry(VentanaLimpia,justify=tk.CENTER)
    caja_dias.place(relx=0.6, rely=0.3)

    etiqueta_tarifa = ttk.Label(VentanaLimpia, text="Digite la tarifa:")
    etiqueta_tarifa.place(relx=0.1, rely=0.5)

    caja_tarifa = ttk.Entry(VentanaLimpia,justify=tk.CENTER)
    caja_tarifa.place(relx=0.6, rely=0.5)

    etiqueta_Total = ttk.Label(VentanaLimpia,text="El total a pagar es: $ 0.00")
    etiqueta_Total.place(relx= 0.1, rely= 0.7)

    boton_calcular = ttk.Button(VentanaLimpia, text="Calcular", command=pago)
    boton_calcular.place(relx=0.6,rely = 0.7)

    VentanaLimpia.resizable(0,0)
    VentanaLimpia.focus()
    VentanaLimpia.grab_set()

# Ventana Fungicida
def fungicida():
    VentanaFungicida = tk.Toplevel()
    VentanaFungicida.title("Fungicida")
    VentanaFungicida.geometry("400x200+480+250")

# Ventana Abono
def abono():
    VentanaAbono = tk.Toplevel()
    VentanaAbono.title("Abono")
    VentanaAbono.geometry("400x200+480+250")