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

def crearVentanaProductoPunto():
    global  idVector1punto, idVector2punto, modalventana

    modalventana = tk.Tk()
    modalventana.title('Producto Punto')
    modalventana.geometry('350x155+800+200')

    vector1 = tk.Label(modalventana, text='Ingrese el Id del Vector 1:')
    vector2 = tk.Label(modalventana, text='Ingrese el Id del Vector 2:')

    vector1.place(x=50, y=20),
    vector2.place(x=50, y=60)

    idVector1punto = tk.Entry(modalventana, validate='key', bg='light grey', bd=0)
    idVector2punto = tk.Entry(modalventana, validate='key', bg='light grey', bd=0)

    idVector1punto.place(x=200, y=20, width=100, height=20)
    idVector2punto.place(x=200, y=60, width=100, height=20)

    botonProductoPunto = tk.Button(
        modalventana,
        text='Producto Punto',
        bg='blue',
        fg='white',
        command=productoPunto
    )

    botonProductoPunto.place(x=50, y=100)

def productoPunto():
    if len(vectores) == 0 or 1:
        MessageBox.showinfo('Error', 'No hay ningún vector creado o solo hay un vector :(')
        modalventana.destroy()
    else:
        try:
            vector1 = int(idVector1punto.get())
            vector2 = int(idVector2punto.get())

            for vector_1 in vectores:
                if vector1 == vector_1['id']:
                    componenteX1 = vector_1['componenteX']
                    componenteY1 = vector_1['componenteY']

            for vector_2 in vectores:
                if vector2 == vector_2['id']:
                    componenteX2 = vector_2['componenteX']
                    componenteY2 = vector_2['componenteY']

            punto = (componenteX1 * componenteX2) + (componenteY1 * componenteY2)
            MessageBox.showinfo('OK', f'el producto punto es: {punto} unidades')
            modalventana.destroy()
        except ValueError:
            MessageBox.showinfo('ERROR', 'Hubo algún error')
   
def crearVentanaProductoCruz():
    global  idVector1cruz, idVector2cruz, modalventanaCruz

    modalventanaCruz = tk.Tk()
    modalventanaCruz.title('Producto Cruz')
    modalventanaCruz.geometry('350x155+800+200')

    vector1 = tk.Label(modalventanaCruz, text='Ingrese el Id del Vector 1:')
    vector2 = tk.Label(modalventanaCruz, text='Ingrese el Id del Vector 2:')

    vector1.place(x=50, y=20),
    vector2.place(x=50, y=60)

    idVector1cruz = tk.Entry(modalventanaCruz, validate='key', bg='light grey', bd=0)
    idVector2cruz = tk.Entry(modalventanaCruz, validate='key', bg='light grey', bd=0)

    idVector1cruz.place(x=200, y=20, width=100, height=20)
    idVector2cruz.place(x=200, y=60, width=100, height=20)

    botonProductoCruz = tk.Button(
        modalventanaCruz,
        text='Producto Cruz',
        bg='blue',
        fg='white',
        command=productoCruz
    )

    botonProductoCruz.place(x=50, y=100)

def productoCruz():
    if len(vectores) == 0 or 1:
        MessageBox.showinfo('Error', 'No hay ningún vector creado o solo hay un vector :(')
        modalventanaCruz.destroy()
    else:
        try:
            vector1 = int(idVector1cruz.get())
            vector2 = int(idVector2cruz.get())

            for vector_1 in vectores:
                if vector1 == vector_1['id']:
                    componenteX1 = vector_1['componenteX']
                    componenteY1 = vector_1['componenteY']

            for vector_2 in vectores:
                if vector2 == vector_2['id']:
                    componenteX2 = vector_2['componenteX']
                    componenteY2 = vector_2['componenteY']

            productoCruz = (componenteX1 * componenteY2) + (componenteX2 * componenteY1)
            MessageBox.showinfo('OK', f'el producto cruz es: {productoCruz}')
            modalventanaCruz.destroy()
        except ValueError:
            MessageBox.showinfo('ERROR', 'Hubo algún error')


def crearVentanaAnguloVectores():
    global  idVector1angulo, idVector2angulo, modalventanaAngulo

    modalventanaAngulo = tk.Tk()
    modalventanaAngulo.title('Angulo Entre Vectores')
    modalventanaAngulo.geometry('350x155+800+200')

    vector1 = tk.Label(modalventanaAngulo, text='Ingrese el Id del Vector 1:')
    vector2 = tk.Label(modalventanaAngulo, text='Ingrese el Id del Vector 2:')

    vector1.place(x=50, y=20),
    vector2.place(x=50, y=60)

    idVector1angulo = tk.Entry(modalventanaAngulo, validate='key', bg='light grey', bd=0)
    idVector2angulo = tk.Entry(modalventanaAngulo, validate='key', bg='light grey', bd=0)

    idVector1angulo.place(x=200, y=20, width=100, height=20)
    idVector2angulo.place(x=200, y=60, width=100, height=20)

    botonProductoCruz = tk.Button(
        modalventanaAngulo,
        text='Angulo Entre Vectores',
        bg='blue',
        fg='white',
        command=AnguloVectores
    )

    botonProductoCruz.place(x=50, y=100)

def AnguloVectores():
    if len(vectores) == 0 or 1:
        MessageBox.showinfo('Error', 'No hay ningún vector creado o solo hay un vector :(')
        modalventanaAngulo.destroy()
    else:
        try:
            vector1 = int(idVector1angulo.get())
            vector2 = int(idVector2angulo.get())

            for vector_1 in vectores:
                if vector1 == vector_1['id']:
                    componenteX1 = vector_1['componenteX']
                    componenteY1 = vector_1['componenteY']
                    magnitud1 = vector_1['magnitud']

            for vector_2 in vectores:
                if vector2 == vector_2['id']:
                    componenteX2 = vector_2['componenteX']
                    componenteY2 = vector_2['componenteY']
                    magnitud2 = vector_2['magnitud']

            punto = (componenteX1 * componenteX2) + (componenteY1 * componenteY2)
            magnitudes = magnitud1 * magnitud2
            division = round(punto / magnitudes, 2)

            if division == 1:
                MessageBox.showinfo('OK', f'el angulo entre los vectores es: 0°')
            else: 
                angulo = round((math.acos(division) * 180/math.pi), 2)
                MessageBox.showinfo('OK', f'el angulo entre los vectores es: {angulo}°')
            modalventanaAngulo.destroy()
        except ValueError:
            MessageBox.showinfo('ERROR', 'Hubo algún error')


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
    return round(math.sqrt(x**2 + y**2), 2)

def angulo(x, y):
    return math.degrees(math.atan2(y, x))

def agregarVector():
    try:
        if componenteIVector1.get() and componenteJVector1.get() == '0':
            MessageBox.showinfo('ERROR', f'no puedes agregar un vector con componentes 0')
            componenteIVector1.delete(0, tk.END)
            componenteJVector1.delete(0, tk.END)
        else:
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

def crearVentanaEliminarVector():
    global  idVector1Elimnar, modalEliminarVector

    modalEliminarVector = tk.Tk()
    modalEliminarVector.title('Producto Cruz')
    modalEliminarVector.geometry('350x90+800+200')

    vector1 = tk.Label(modalEliminarVector, text='Ingrese el Id del Vector:')
    vector1.place(x=50, y=20),

    idVector1Elimnar = tk.Entry(modalEliminarVector, validate='key', bg='light grey', bd=0)
    idVector1Elimnar.place(x=200, y=20, width=100, height=20)

    botonEliminarVector = tk.Button(
        modalEliminarVector,
        text='Eliminar Vector',
        bg='red',
        fg='white',
        command=eliminarVector
    )

    botonEliminarVector.place(x=50, y=50)

def eliminarVector():
    if len(vectores) == 0:
        MessageBox.showinfo('Error', 'No hay ningún vector creado :(')
        modalEliminarVector.destroy()
    else:
        for vector_1 in vectores:
            vector1 = int(idVector1Elimnar.get())

            if vector1 == vector_1['id']:
                vectores.remove(vector_1)
                MessageBox.showinfo('OK', 'Vectore Eliminado')
                actualizarGrafico()
                actualizarTabla()
                modalEliminarVector.destroy()
            else:
                MessageBox.showinfo('Error', 'No hay ningún vector con ese id :(')
                modalEliminarVector.destroy()


def eliminarVectores():
    if(len(vectores) == 0):
        MessageBox.showinfo('Error', 'No hay ningún vector creado :(')
    else:
        vectores.clear()
        actualizarGrafico()
        actualizarTabla()
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
    ax.set_xlim( -5 + min_x - 1, 5 + max_x + 1)
    ax.set_ylim( -5 + min_y - 1, 5 + max_y + 1)

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
        bg='#029df0',
        fg='white',
        text='Añadir Vector', 
        command=agregarVector
    )
    botonEliminarVector = tk.Button(
        ventana, 
        bg='red',
        fg='white',
        text='Eliminar Vector', 
        command=crearVentanaEliminarVector
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
        command=crearVentanaProductoPunto
    )
    botonProductoCruz = tk.Button(
        ventana,
        text='Producto Cruz',
        bg='blue',
        fg='white',
        command=crearVentanaProductoCruz
    )
    botonAnguloEntreVectores = tk.Button(
        ventana,
        text='Angulo Entre Vectores',
        bg='gray',
        fg='white',
        command=crearVentanaAnguloVectores
    )

    botonAnadir.place(x=600, y=80)
    botonEliminarVector.place(x=600, y=120)
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