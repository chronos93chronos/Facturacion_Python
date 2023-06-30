from tkinter import *


ventana = Tk()
ventana.title("CARRITO COMPRA")
ventana.geometry("400x500")
ventana.resizable(False, False)
ventana.config(bg="#C4F2FF")
#____________________________________________
#                    FUNCIONES





#____________________________________________
carrito = Label(ventana, text="TOTAL CARRITO $")
carrito.place(x=10, y = 10, width = 100, height= 25)
monto_carro = Entry(ventana)
monto_carro.place(x=140, y = 10, width = 100, height= 25)

total_productos_carro = Label(ventana, text="UNIDADES")
total_productos_carro.place(x=10, y = 40, width = 100, height= 25)
unidades = Entry(ventana)
unidades.place(x=140, y = 40, width = 100, height= 25)

total_neto = Label(ventana, text="TOTAL NETO")
total_neto.place(x=10, y = 80, width = 100, height= 25)
neto_moneda = Entry(ventana)
neto_moneda.place(x=140, y = 80, width = 100, height= 25)

iva = Label(ventana, text="IVA 19%")
iva.place(x=10, y = 110, width = 100, height= 25)
iva_moneda = Entry(ventana)
iva_moneda.place(x=140, y = 110, width = 100, height= 25)

total_pagar = Label(ventana, text="TOTAL PAGAR")
total_pagar.place(x=10, y = 140, width = 100, height= 25)
total_pagar_moneda = Entry(ventana)
total_pagar_moneda.place(x=140, y = 140, width = 100, height= 25)

#____________________________________________
#                     BOTONES

agregar = Button(ventana, text = "AGREGAR PRODUCTOS" )
agregar.place(x=20, y=200, width=130, height=30)

terminar = Button(ventana, text = "TERMINAR COMPRA" )
terminar.place(x=170, y=200, width=130, height=30)












ventana.mainloop()