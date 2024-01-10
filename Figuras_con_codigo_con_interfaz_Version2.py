from turtle import *
from colorsys import *
import re
import docx
import math
import tkinter as tk
from tkinter import ttk

def flores_con_tallo():
    data = docx.Document("tulips.docx")   
    coordinates = []   
    colour = []

    for i in data.paragraphs:   
        try :
            patron = r'[-+]?\d*\.\d*(?:[eE][-+]?\d+)?'
            patron_coord = r'\(' + patron + r' ?\, ?' + patron
            patron_color = patron_coord + r' ?\, ?' + patron + r'\)'

            coord_stg_tup = re.findall(patron_coord + r'\)', i.text)
            color_stg_tup = re.findall(patron_color, i.text)

            coord_num_tup = []      
            color_val = re.findall(r'[-+]?\d*\.\d*',color_stg_tup[0])   
            color_val_lst = [float(k) for k in color_val]   
            colour.append(tuple(color_val_lst))   

            for j in coord_stg_tup:   
                coord_pos = re.findall(r'[-+]?\d*\.\d*',j)   
                coord_num_lst = [float(k) for k in coord_pos]   
                coord_num_tup.append(tuple(coord_num_lst))   

            coordinates.append(coord_num_tup)   
        except:   
            pass   

    pen = Turtle()   
    screen = Screen()   

    tracer(2)   
    hideturtle()   
    speed(10)
    screen.getcanvas().winfo_toplevel().attributes("-fullscreen", True)

    for i in range(len(coordinates)):   
        draw = 1   
        path = coordinates[i]   
        col = colour[i]   
        color(col)   
        begin_fill()   
        for order_pair in path:   
            x,y = order_pair   
            y = -1*y   
            if draw:   
                up()   
                goto(x,y)   
                down()   
                draw = 0   
            else:   
                goto(x,y)   
        end_fill()   
        hideturtle()  
    screen.mainloop()

def estrella_ninja_con_arcoiris():
    bgcolor("black")
    tracer(2)
    pensize(2)
    h = 0

    for i in range(180):
        c = hsv_to_rgb(h,1,1)
        h +=0.005
        color(c)
        up()
        goto(-8,25)
        down()
        forward(i)
        right(89)
        fillcolor(c)
        begin_fill()
        circle(90,100)
        end_fill()
        left(179)
        back(i/2)
        left(6)

    done()

def flor_de_muchos_colores():
    bgcolor('black')
    speed(0)

    color=['blue','cyan','lightgreen',
            'yellow','red','violet']

    for i in range(150):
        pencolor(color[i%6])
        circle(190-i/2,90)
        left(90)
        circle(190-i/3,90)
        left(60)

    done()

def flor_arcoiris():
    speed(0)
    bgcolor("black")
    h = 0

    for i in range(16):
        for j in range(18):
            c = hsv_to_rgb(h,0.9,1)
            color(c)
            h += 0.005
            rt(90)
            circle(150-j*6,90)
            lt(90)
            circle(150-j*6,90)
            rt(180)
        circle(40,24)

    done()

def flor_arcoiris_neon():
    bgcolor('black')
    pensize(4)
    tracer(10)
    h=0

    def dibujo(a,n):
        circle(5+n,60), left(a), circle(5+n,60)

    for i in range(360):
        c=hsv_to_rgb(h,1,1)
        h+=0.008
        color(c,'black'), begin_fill()
        dibujo(90,i/2), end_fill()
        dibujo(160,i*1.2), penup()
        dibujo(0,0), dibujo(90,i/2), pendown()

    done()

def flor_arcoiris_de_9_picos_creciente():
    bgcolor("black")
    speed(0)
    h = 0

    for i in range(371):
        c = hsv_to_rgb(h,1,1)
        h += 0.005
        color(c)
        circle(-i*0.68,200)
        right(80)
    done()

def estrella_de_5_picos_que_gira():
    t = Turtle()
    s = Screen()
    s.bgcolor("black")
    t.speed(0)
    n = 50
    h = 0

    for i in range(380):
        c = hsv_to_rgb(h,1,0.8)
        h = h + 1/n
        t.color(c)
        t.forward(i*2)
        t.left(145)
    done()

def estrella_creciente():
    bgcolor("black")
    pensize(2)
    tracer(10)
    h=0

    for i in range(400):
        c=hsv_to_rgb(h,1,1)
        pencolor(c)
        h+=0.005
        right(120)
        circle(-i*0.5,120)
        circle(i*0.5,120)
        circle(i*0.5,60)
    done()

def espiral_arcoiris():
    speed(15)
    bgcolor("black")
    r, g, b = 255, 0 , 0

    for i in range(255*2):
        colormode(255)

        if i<(255*1)//3:
            g +=3
        elif i<(255*2)//3:
            r-=3
        elif i<(255*3)//3:
            b+=3
        elif i<(255*4)//3:
            g-=3
        elif i<(255*5)//3:
            r+=3

        forward(50+i)
        right(91)
        pencolor(r,g,b)

    done()

def girasol():
    speed(0.25)
    bgcolor("black")

    # Genera los petalos
    goto(0, -40)
    h = 0

    for i in range(16):
        for j in range(18):
            c= hsv_to_rgb(0.125 , 1, 1)
            color(c)
            rt(90)
            circle(150-j*6, 90)
            lt(90)
            circle(150-j*6, 90)
            rt(180)
        circle(40, 24)

    # Genera la parte centrall de la flor
    color("black") 
    shape("turtle")
    fillcolor("brown")
    phi = 137.508 * (math.pi/ 180.0)

    for i in range (200):
        r = 4 * math.sqrt(i)
        theta = i*phi
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        penup()
        goto(x, y)
        setheading(i * 137.508)
        pendown()
        stamp()

    #Dibujar el tallo verde del girasol
    penup()
    goto(0,-100)
    pendown()
    color("green")
    begin_fill()
    rt(90)
    fd(400)
    lt(90)
    fd(20)
    lt(90)
    fd(400)
    lt(90)
    fd(20)
    end_fill()

    done()

def flor_con_diamantes():
    # Configuration
    bgcolor("black")
    shape("turtle")
    speed(0)
    fillcolor("brown")

    # Draw
    penup()
    goto(0, -200)
    pendown()
    setheading(90)
    fillcolor("green")  # Cambia el color del tallo a verde
    begin_fill()
    forward(200)
    left(90)
    forward(20)
    left(90)
    forward(200)
    end_fill()

    # Colour
    penup()
    goto(0, -180)
    fillcolor("#8B4513")  # Café más claro
    begin_fill()
    circle(0)
    end_fill()

    # Códe
    phi = 137.508 * (math.pi / 180.0)
    for i in range(160 + 40):
        r = 4 * math.sqrt(i)
        theta = i * phi
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        penup()
        goto(x, y)
        setheading(i * 137.508)
        pendown()
        if i < 160:
            stamp()
        else:
            fillcolor("yellow")
            begin_fill()
            right(20)
            forward(70)
            left(40)
            forward(70)
            left(140)
            forward(70)
            left(40)
            forward(70)
            end_fill()
            
    # hide curs
    hideturtle()

    # close window
    exitonclick()

def girasol_con_tallo():
    speed(0.25)
    bgcolor("black")

    # Genera los petalos
    goto(0, -40)
    h = 0

    for i in range(16):
        for j in range(18):
            c= hsv_to_rgb(0.125 , 1, 1)
            color(c)
            rt(90)
            circle(150-j*6, 90)
            lt(90)
            circle(150-j*6, 90)
            rt(180)
        circle(40, 24)

    # Genera la parte centrall de la flor
    color("black") 
    shape("turtle")
    fillcolor("brown")
    phi = 137.508 * (math.pi/ 180.0)

    for i in range (200):
        r = 4 * math.sqrt(i)
        theta = i*phi
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        penup()
        goto(x, y)
        setheading(i * 137.508)
        pendown()
        stamp()

    done()

def flor_roja():
    penup()
    left(90)
    fd(200)
    pendown()
    right(90)

    fillcolor("red")
    begin_fill()
    circle(10, 180)
    circle(25, 110)
    left(50)
    circle(60, 45)
    circle(20, 170)
    right(24)
    fd(30)
    left(10)
    circle(30, 110)
    fd(20)
    left(40)
    circle(90, 70)
    circle(30, 150)
    right(30)
    fd(15)
    circle(80, 90)
    left(15)
    fd(45)
    right(165)
    fd(20)
    left(155)
    circle(150, 80)
    left(50)
    circle(150, 90)
    end_fill()

    left(150)
    circle(-90, 70)
    left(20)
    circle(75, 105)
    setheading(60)
    circle(80, 90)
    circle(-90, 40)

    left(180)
    circle(90, 40)
    circle(-80, 98)
    setheading(-83)

    fd(30)
    left(90)
    fd(25)
    left(45)
    fillcolor("dark green")
    begin_fill()
    circle(-80, 90)
    right(90)
    circle(-80, 90)
    end_fill()
    right(135)
    fd(60)
    left(180)
    fd(85)
    left(90)
    fd(80)

    right(90)
    right(45)
    fillcolor("dark green")
    begin_fill()
    circle(80, 90)
    left(90)
    circle(80, 90)
    end_fill()
    left(135)
    fd(60)
    left(180)
    fd(60)
    right(90)
    circle(200, 60)

def flor_amarilla():
    penup()
    left(90)
    fd(200)
    pendown()
    right(90)

    fillcolor("red")
    begin_fill()
    circle(10, 180)
    circle(25, 110)
    left(50)
    circle(60, 45)
    circle(20, 170)
    right(24)
    fd(30)
    left(10)
    circle(30, 110)
    fd(20)
    left(40)
    circle(90, 70)
    circle(30, 150)
    right(30)
    fd(15)
    circle(80, 90)
    left(15)
    fd(45)
    right(165)
    fd(20)
    left(155)
    circle(150, 80)
    left(50)
    circle(150, 90)
    end_fill()

    left(150)
    circle(-90, 70)
    left(20)
    circle(75, 105)
    setheading(60)
    circle(80, 90)
    circle(-90, 40)

    left(180)
    circle(90, 40)
    circle(-80, 98)
    setheading(-83)

    fd(30)
    left(90)
    fd(25)
    left(45)
    fillcolor("dark green")
    begin_fill()
    circle(-80, 90)
    right(90)
    circle(-80, 90)
    end_fill()
    right(135)
    fd(60)
    left(180)
    fd(85)
    left(90)
    fd(80)

    right(90)
    right(45)
    fillcolor("dark green")
    begin_fill()
    circle(80, 90)
    left(90)
    circle(80, 90)
    end_fill()
    left(135)
    fd(60)
    left(180)
    fd(60)
    right(90)
    circle(200, 60)

# Diccionario con la relación entre el número y la función correspondiente
opciones_dict = {
    1: flores_con_tallo,
    2: estrella_ninja_con_arcoiris,
    3: flor_de_muchos_colores,
    4: flor_arcoiris,
    5: flor_arcoiris_neon,
    6: flor_arcoiris_de_9_picos_creciente,
    7: estrella_de_5_picos_que_gira,
    8: estrella_creciente,
    9: espiral_arcoiris,
    10: flor_roja,
    11: flor_con_diamantes,
    12: girasol,
    13: flor_amarilla,
    14: girasol_con_tallo
}

# Función que se ejecuta al seleccionar una opción en el menú
def seleccionar_opcion():
    opcion_str = opc_var.get()
    opcion_numero_str = opcion_str.split(".")[0]
    
    try:
        opcion = int(opcion_numero_str)
    except ValueError:
        print("Opción no válida")
        return

    if opcion == 0:
        ventana.destroy()  # Cerrar la ventana si se selecciona la opción 0
    else:
        ventana.iconify()  # Minimizar la ventana antes de ejecutar la opción
        ejecutar_opcion(opcion)
        ventana.deiconify()  # Restaurar la ventana después de ejecutar la opción

# Función que ejecuta la opción seleccionada
def ejecutar_opcion(opcion):
    if opcion in opciones_dict:
        opcion_func = opciones_dict[opcion]
        print(f"Ejecutando: {opcion_func.__name__}")
        opcion_func()
    else:
        print("Opción no válida")

# Crear la interfaz gráfica
ventana = tk.Tk()
ventana.title("Menú de Turtle")

# Crear variable para la opción seleccionada
opc_var = tk.StringVar(ventana)

# Crear opciones del menú con nombres de funciones
opciones = [f"{i}. {opciones_dict[i].__name__}" for i in opciones_dict]
opciones_combo = ttk.Combobox(ventana, textvariable=opc_var, values=opciones)
opciones_combo.set("Selecciona una opción")
opciones_combo.grid(column=0, row=0, padx=10, pady=10)

# Botón para ejecutar la opción seleccionada
boton_ejecutar = tk.Button(ventana, text="Ejecutar", command=seleccionar_opcion)
boton_ejecutar.grid(column=1, row=0, padx=10, pady=10)

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()