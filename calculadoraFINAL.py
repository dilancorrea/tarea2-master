import turtle


def posicionar(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.seth(0)
    turtle.pendown()


# Crea la ventana
turtle.reset()
turtle.setup(600, 350)
turtle.speed(0)


# Dibuja el display
def display():
    turtle.penup()
    turtle.goto(-275, 150)
    turtle.seth(0)
    turtle.fillcolor("#2db300")
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(550)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(550)
    turtle.right(90)
    turtle.forward(50)
    turtle.end_fill()


display()


def dibujarBoton(x, y, color):
    """
        Descripcion: Esta es un codigo el cual nos ayudara a dibujar un boton de la calculadora.
        Entradas: x es un entero el cual representa la coordenada en x de la parte superior izquierda.
                  y es un entero el cual representa la coordenada en y de la parte superior izquierda.
        Salida: Movimiento de la tortuga.
        """
    turtle.seth(0)
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(125)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(125)
    turtle.right(90)
    turtle.forward(50)
    turtle.end_fill()


# Dibuja el boton 1
dibujarBoton(-275, 90, "#ff6600")

# Dibuja el boton 2
dibujarBoton(-140, 90, "#ff6600")

# Dibuja el boton 3
dibujarBoton(-5, 90, "#ff6600")

# Dibuja el boton +
dibujarBoton(150, 90, "#66a3ff")

# Dibuja el boton 4
dibujarBoton(-275, 30, "#ff6600")

# Dibuja el boton 5
dibujarBoton(-140, 30, "#ff6600")

# Dibuja el boton 6
dibujarBoton(-5, 30, "#ff6600")

# Dibuja el boton -
dibujarBoton(150, 30, "#66a3ff")

# Dibuja el boton 7
dibujarBoton(-275, -30, "#ff6600")

# Dibuja el boton 8
dibujarBoton(-140, -30, "#ff6600")

# Dibuja el boton 9
dibujarBoton(-5, -30, "#ff6600")

# Dibuja el boton x
dibujarBoton(150, -30, "#66a3ff")

# Dibuja el boton AC
dibujarBoton(-275, -90, "#66a3ff")

# Dibuja el boton 0
dibujarBoton(-140, -90, "#ff6600")

# Dibuja el boton =
dibujarBoton(-5, -90, "#66a3ff")

# Dibuja el boton /
dibujarBoton(150, -90, "#66a3ff")


# Dibuja el label de los botones

def dibujaLabel(x, y, valor):
    """
        Descripcion: Esta es un codigo el cual nos ayudara a dibujar el numero de los botones.
        Entradas: x es un entero el cual representa la coordenada en x de la parte superior izquierda.
                  y es un entero el cual representa la coordenada en y de la parte superior izquierda.
                  valor es un string que determina el numero del boton.
        Salida: Movimiento de la tortuga.
        """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor("white")
    turtle.write(valor, align='center', font=('Arial', 24, 'bold'))


dibujaLabel(-213, 45, "1")
dibujaLabel(-78, 45, "2")
dibujaLabel(57, 45, "3")
dibujaLabel(212, 45, "+")
dibujaLabel(-213, -15, "4")
dibujaLabel(-78, -15, "5")
dibujaLabel(57, -15, "6")
dibujaLabel(212, -15, "-")
dibujaLabel(-213, -75, "7")
dibujaLabel(-78, -75, "8")
dibujaLabel(57, -75, "9")
dibujaLabel(212, -75, "x")
dibujaLabel(-213, -135, "AC")
dibujaLabel(-78, -135, "0")
dibujaLabel(57, -135, "=")
dibujaLabel(212, -135, "/")

numero = 0
numDigitos = 0
numero2 = 0
total = 0
numero1 = 0
op = 0


def Hacernum(valor):
    """
        Descripcion: Este es un codigo que sirve para mostrar los numeros en el display.
        Entradas:valor es un entero que determina el numero que se va a generar en el display.
        Salida: El numero en el display.
        """
    global numDigitos, numero
    numDigitos = numDigitos + 1
    numero = (numero * 10) + valor
    display()
    turtle.penup()
    turtle.goto(270 - (numDigitos * 9), 110)
    turtle.pendown()
    turtle.pencolor("white")
    turtle.write(str(numero), align='center', font=('Arial', 24, 'bold'))


def totalx():
    """
        Descripcion: Este es un codigo que sirve para mostrar el resultado de la operacion realizada en el display.
        Salida: El numero total de la operacion en el display.
        """
    global total, numDigitos
    display()
    turtle.penup()
    turtle.goto(270, 110)
    turtle.pendown()
    turtle.pencolor("white")
    turtle.write(str(total), align='right', font=('Arial', 24, 'bold'))


def numerox():
    """
        Descripcion: Este es un codigo que sirve para guardar el numero uno digitado.
        """
    global numero, numero1, numDigitos
    numero1 = numero
    display()
    turtle.penup()
    turtle.goto(260, 110)
    turtle.pendown()
    turtle.pencolor("white")
    turtle.write("0", align='center', font=('Arial', 24, 'bold'))
    numero = 0
    numDigitos = 0


# Definicion de la funcion que determina que boton se pulso
def deteccionClick(x, y):
    global numero, numDigitos, numero2, numero1, total, op
    if (x > -275 and x < -150 and y > 40 and y < 90):
        Hacernum(1)
    if (x > -140 and x < -15 and y > 40 and y < 90):
        Hacernum(2)
    if (x > -5 and x < 120 and y > 40 and y < 90):
        Hacernum(3)
    if (x > 150 and x < 275 and y > 40 and y < 90):
        numerox()
        op = 1
    if (x > -275 and x < -150 and y > -20 and y < 30):
        Hacernum(4)
    if (x > -140 and x < -15 and y > -20 and y < 30):
        Hacernum(5)
    if (x > -5 and x < 120 and y > -20 and y < 30):
        Hacernum(6)
    if (x > 150 and x < 275 and y > -20 and y < 30):
        numerox()
        op = 2
    if (x > -275 and x < -150 and y > -80 and y < -30):
        Hacernum(7)
    if (x > -140 and x < -15 and y > -80 and y < -30):
        Hacernum(8)
    if (x > -5 and x < 120 and y > -80 and y < -30):
        Hacernum(9)
    if (x > 150 and x < 275 and y > -80 and y < -30):
        numerox()
        op = 3
    if (x > -140 and x < -15 and y > -140 and y < -90):
        Hacernum(0)
    if (x > 150 and x < 275 and y > -140 and y < -90):
        numerox()
        op = 4
    if (x > -275 and x < -150 and y > -140 and y < -90):
        numero = 0
        numDigitos = 0
        numero2 = 0
        total = 0
        display()
    if (numDigitos > 30):
        display()
        turtle.penup()
        turtle.seth(0)
        turtle.goto(-70, 110)
        turtle.pendown()
        turtle.write("Error: se supero la cantidad maxima de 30 digitos", align='center', font=('Arial', 12, 'bold'))
        numDigitos = 0
        numero = 0
        numero2 = 0
    if (x > -5 and x < 120 and y > -140 and y < -90):
        if (op == 1):
            numero2 = numero
            total = numero1 + numero2
            totalx()
            numero = total
        if (op == 2):
            numero2 = numero
            total = numero1 - numero2
            totalx()
            numero = total
        if (op == 3):
            numero2 = numero
            total = numero1 * numero2
            totalx()
            numero = total
        if (op == 4):
            numero2 = numero
            if (numero2 == 0):
                display()
                turtle.penup()
                turtle.goto(-40, 110)
                turtle.pendown()
                turtle.pencolor("white")
                turtle.write("La division por cero no esta definida", align='center', font=('Arial', 18, 'bold'))
                numDigitos = 0
            if (numero2 > 0):
                total = numero1 / numero2
                totalx()
                numero = total


# Detecta el click del mouse
turtle.onscreenclick(deteccionClick)

# Esconde la tortuga
turtle.hideturtle()

