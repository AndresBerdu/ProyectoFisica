import tkinter as tk
from tkinter import ttk, Toplevel
from tkinter import messagebox as MessageBox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import math

ventana = tk.Tk()
vectores = []

def crearVentana():
    ventana.title("Aplicacion Vectores")
    ventana.state('zoomed')
    ventana.configure(bg='white')

crearVentana()

def ():
    componenteX1 = 0
    componenteY1 = 0
    componenteX2 = 0
    componenteY2 = 0

    modalventana = tk.Tk()
    modalventana.title('Producto Punto')
    modalventana.geometry('500x350+800+200')

    vector1 = tk.Label(modalventana, text='Ingrese el Id del Vector 1:')
    vector2 = tk.Label(modalventana, text='Ingrese el Id del Vector 2:')

    vector1.place(x=50, y=50),
    vector2.place(x=50, y=80)

    idVector1 = tk.Entry(modalventana, validate='key', bg='light grey', bd=0)
    idVector2 = tk.Entry(modalventana, validate='key', bg='light grey', bd=0)

    idVector1.place(x=200, y=50, width=100, height=20)
    idVector2.place(x=200, y=80, width=100, height=20)

    vector1 = int(idVector1.get())
    vector2 = int(idVector1.get())

    for vector in vectores:
        if vector1 == vector['id']:
            componenteX1 = vector['componenteX']
            componenteY1 = vector['componenteY']

    for vector in vectores:
        if vector2 == vector['id']:
            componenteX2 = vector['componenteX']
            componenteY2 = vector['componenteY']
        
    productoPunto = (componenteX1 * componenteX2) + (componenteY1 * componenteY2)

    botonProductoPunto = tk.BuWtton(
        modalventana,
        text='Producto Punto',
        bg='blue',
        fg='white',
        command= lambda: MessageBox.showinfo('OK', f'el producto punto es: {productoPunto}')
    )

    botonProductoPunto.place(x=50, y=120)

def producto_punto(): 


def etiquetas():
    tituloVector = tk.Label(ventana, text='Añadir Vector', font=('Helvetica', 16, 'bold'))
    componenteXVector1 = tk.Label(ventana, text='Componente X del vector:')
    componenteYVector1 = tk.Label(ventana, text='Componente Y del vector:')

    tituloVector.configure(bg='white')
    componenteXVector1.configure(bg='white')
    componenteYVector1.configure(bg='white')

    tituloVector.place(x=30, y=10)
    componenteXVector1.place(x=50, y=50)
    componenteYVector1.place(x=300, y=50)

def entradas():
    global componenteIVector1, componenteJVector1, idVector1, idVector2

    componenteIVector1 = tk.Entry(ventana, validate='key', bg='light grey', bd=0)
    componenteJVector1 = tk.Entry(ventana, validate='key', bg='light grey', bd=0)

    componenteIVector1.place(x=50, y=80, width=200, height=30)
    componenteJVector1.place(x=300, y=80, width=200, height=30)

def magnitud(x, y):
    return math.sqrt(x**2 + y**2)

def angulo(x, y):
    return math.degrees(math.atan2(y, x))

def agregarVector():
    try:
        x = float(componenteIVector1.get())
        y = float(componenteJVector1.get())
        vector_id = len(vectores) + 1
        vector_magnitud = magnitud(x, y)
        vector_angulo = round(angulo(x, y), 2)
        vector = {
            "id": vector_id,
            "componenteX": x,
            "componenteY": y,
            "magnitud": vector_magnitud,
            "angulo": vector_angulo
        }
        vectores.append(vector)
        actualizarGrafico()
        actualizarTabla()
        print(vector)
        componenteIVector1.delete(0, tk.END)
        componenteJVector1.delete(0, tk.END)
    except ValueError:
        MessageBox.showinfo('Error', 'Caracter Invalido')

def eliminarVectores():
    if(len(vectores) == 0):
        MessageBox.showinfo('Error', 'No hay ningún vector creado :(')
    else:
        vectores.clear()
        actualizarGrafico()
        MessageBox.showinfo('OK', 'Vectores Eliminados')


def actualizarGrafico():
    global ax, canvas, fig

    #Origen y lipiar grafica
    ax.clear()
    origen = [0, 0]

    #limites de acuerdo al Vector con mayor magnitud
    max_x = max([vector["componenteX"] for vector in vectores], default=0)
    min_x = min([vector["componenteX"] for vector in vectores], default=0)
    max_y = max([vector["componenteY"] for vector in vectores], default=0)
    min_y = min([vector["componenteY"] for vector in vectores], default=0)

    #Ciclo para poner el Id al Vector dentro de la grafica
    for vector in vectores:
        x, y = vector["componenteX"] , vector["componenteY"]
        ax.quiver(*origen, x, y, angles='xy', scale_units='xy', scale=1)
        ax.annotate(f'V{vector["id"]}', (x, y), textcoords="offset points", xytext=(2,10), ha='center')

    #Limites de la grafica
    ax.set_xlim(min_x - 1, max_x + 1)
    ax.set_ylim(min_y - 1, max_y + 1)

    #Lineas grafica
    ax.axhline(0, color='grey', lw=0.5)
    ax.axvline(0, color='grey', lw=0.5)

    #Ejes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    #Dibujar Grafica
    ax.grid()
    canvas.draw()

def tabla():
    global tabla
    tabla = ttk.Treeview(ventana, columns=('col1', 'col2', 'col3', 'col4'))

    tabla.column('#0', width=80, anchor='center')
    tabla.column('col1', width=80, anchor='center')
    tabla.column('col2', width=80, anchor='center')
    tabla.column('col3', width=80, anchor='center')
    tabla.column('col4', width=80, anchor='center')

    tabla.heading('#0', text='id', anchor='center')
    tabla.heading('col1', text='X', anchor='center')
    tabla.heading('col2', text='Y', anchor='center')
    tabla.heading('col3', text='Magnitud', anchor='center')
    tabla.heading('col4', text='Angulo', anchor='center')

    tabla.place(x=100, y=200, width=520, height=370)

def actualizarTabla():
    for item in tabla.get_children():
        tabla.delete(item)
    for vector in vectores:
        _id = vector["id"]
        X = vector["componenteX"]
        Y = vector["componenteY"]
        magnitud = vector["magnitud"]
        angulo = vector["angulo"]

        tabla.insert("", 'end', text=_id, values=(X, Y, magnitud, angulo))

def botones():
    botonAnadir = tk.Button(
        ventana, 
        text='Añadir Vector', 
        command=agregarVector
    )
    botonEliminarVectores = tk.Button(
        ventana,
        text='Eliminar Vectores',
        bg='red',
        fg='white',
        command=eliminarVectores
    )
    botonProductoPuntoVectores = tk.Button(
        ventana,
        text='Producto Punto',
        bg='green',
        fg='white',
        command=productoPunto
    )
    botonProductoCruz = tk.Button(
        ventana,
        text='Producto Cruz',
        bg='blue',
        fg='white',
        command=eliminarVectores
    )
    botonAnguloEntreVectores = tk.Button(
        ventana,
        text='Angulo Entre Vectores',
        bg='pink',
        fg='white',
        command=eliminarVectores
    )

    botonAnadir.place(x=600, y=80)
    botonEliminarVectores.place(x=760, y=25)
    botonProductoPuntoVectores.place(x=880, y=25)
    botonProductoCruz.place(x=990, y=25)
    botonAnguloEntreVectores.place(x=1100, y=25)

etiquetas()
entradas()
botones()
tabla()

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Crear un canvas de Tkinter para el gráfico de matplotlib
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.draw()
canvas.get_tk_widget().place(x=700, y=50)

def cerrarVentana():
    ventana.quit()
    ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", cerrarVentana)
ventana.mainloop()