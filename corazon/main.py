
import turtle
import math
import random

# Ventana
pantalla = turtle.Screen()
pantalla.setup(800, 700)
pantalla.bgcolor("#080014")
pantalla.title("❤️ Corazón Neón")
pantalla.tracer(0)

# Tortuga de dibujo
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# Estrellas decorativas
estrellas = turtle.Turtle()
estrellas.hideturtle()
estrellas.speed(0)
estrellas.penup()

colores = ["#ff00ff", "#00ffff", "#ffffff", "#ff1493"]

for _ in range(65):
    x = random.randint(-370, 370)
    y = random.randint(-310, 310)
    estrellas.goto(x, y)
    estrellas.dot(random.randint(2, 5), random.choice(colores))

# Fórmula matemática del corazón
puntos = []

for i in range(361):
    angulo = math.radians(i)

    x = 16 * math.sin(angulo) ** 3
    y = (13 * math.cos(angulo)
         - 5 * math.cos(2 * angulo)
         - 2 * math.cos(3 * angulo)
         - math.cos(4 * angulo))

    puntos.append((x * 14, y * 14))

# Dibujar el contorno con efecto neón
for grosor, color in [
    (18, "#590078"),
    (12, "#b000ff"),
    (7, "#ff008c"),
    (3, "#ffffff")
]:
    t.penup()
    t.goto(puntos[0])
    t.pensize(grosor)
    t.pencolor(color)
    t.pendown()

    for punto in puntos[1:]:
        t.goto(punto)

    t.goto(puntos[0])

# Corazón relleno
t.penup()
t.goto(puntos[0])
t.pensize(2)
t.pencolor("#ff55aa")
t.fillcolor("#ed0055")
t.begin_fill()
t.pendown()

for punto in puntos[1:]:
    t.goto(punto)

t.goto(puntos[0])
t.end_fill()
t.penup()

# Mensaje
t.goto(0, -275)
t.color("#ff8de1")
t.write(
    "HECHO CON AMOR",
    align="center",
    font=("Arial", 22, "bold")
)

t.goto(0, -305)
t.color("#00ffff")
t.write(
    "Python Turtle",
    align="center",
    font=("Arial", 13, "normal")
)

pantalla.update()
turtle.done()