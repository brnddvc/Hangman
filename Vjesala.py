import turtle
import random

greska = 0
turtle.setup(width=1355, height=768, startx=0, starty=0)


def crtaj_vjesala(i):
    if i == 1:
        turtle.penup()
        turtle.goto(-275, -100)
        turtle.pendown()
        turtle.setheading(0)
        turtle.forward(200)
    if i == 2:
        turtle.penup()  # drugi korak
        turtle.goto(-175, -100)
        turtle.pendown()
        turtle.setheading(90)
        turtle.forward(300)
    if i == 3:
        turtle.penup()
        turtle.goto(-175, 200)
        turtle.pendown()
        turtle.setheading(0)  # treci korak
        turtle.forward(125)
    if i == 4:
        turtle.penup()
        turtle.goto(-50, 200)
        turtle.pendown()
        turtle.setheading(270)  # cetvrti korak
        turtle.forward(50)
    if i == 5:
        turtle.penup()  # peti korak
        turtle.goto(-50, 100)
        turtle.pendown()
        turtle.circle(25)
    if i == 6:
        turtle.penup()  # sesti korak
        turtle.goto(-50, 100)
        turtle.pendown()
        turtle.setheading(270)
        turtle.forward(100)
    if i == 7:
        turtle.penup()  # sedmi korak
        turtle.goto(-50, 63)
        turtle.setheading(135)
        turtle.pendown()
        turtle.forward(50)
    if i == 8:
        turtle.penup()  # osmi korak
        turtle.goto(-50, 63)
        turtle.setheading(45)
        turtle.pendown()
        turtle.forward(50)
    if i == 9:
        turtle.penup()  # deveti korak
        turtle.goto(-50, 0)
        turtle.pendown()
        turtle.setheading(225)
        turtle.forward(50)
    if i == 10:
        turtle.penup()  # deseti korak
        turtle.goto(-50, 0)
        turtle.pendown()
        turtle.setheading(315)
        turtle.forward(50)


def unesena_slova(slovo, broj):
    turtle.penup()
    turtle.goto(30 * broj, -200)
    turtle.pencolor("red")
    turtle.write(slovo + ", ", move=False, align = "center", font = ("Arial", 24, "italic"))


turtle.penup()
turtle.goto(50, 280)
turtle.pendown()
turtle.pencolor("red")
turtle.write(
    """Dobrodosli u Hangman!
    Ponudjene kategorije su: cities, countries, movies, music, singers, sportists.
    """, move=False, align="center", font=("Arial", 16, "italic", "bold"))
x = random.randint(2, 16)
turtle.pencolor("black")
kat = turtle.textinput("Kategorije",
    "Unesite kategoriju")
input_file = open(kat + ".txt", "r")
turtle.bgpic(kat + ".gif")
prazno = ''
linija = ''
linija = input_file.readline()
j = 1
if x > 1:
    while j < x and linija != prazno:
        linija = input_file.readline()
        j = j + 1
j = 0
turtle.pensize(5)  # prvi korak
turtle.penup()
turtle.hideturtle()
turtle.goto(50, -100)
while j < len(linija) - 1:
    turtle.pendown()
    if linija[j] == " ":
        turtle.write(" ", move=False, align="center",
            font=("Arial", 24, "normal"))
    else:
        turtle.write("_", move=False, align="center",
            font=("Arial", 24, "normal"))
    turtle.penup()
    turtle.forward(25)
    j = j + 1

k = 1
j = 0
lista_slova = []
turtle.penup()
while j < len(linija):
    if linija[j] == " ":
        k = k + 1
    j = j + 1
while greska <= 10 and k < len(linija):
    slovo = turtle.textinput("Slovo", "Unesite slovo: ")
    slovo = slovo.upper()
    lista = []
    if slovo in lista_slova:
        continue
    lista_slova.append(slovo)
    unesena_slova(slovo, len(lista_slova))
    turtle.pencolor("black")
    turtle.penup()
    turtle.goto(50, -150)
    turtle.setheading(0)
    turtle.forward(25 * k + 25)
    i = 0
    while i < len(linija):
        if slovo == linija[i]:
            lista.append(i)
        i = i + 1
    for i in lista:
        turtle.penup()
        turtle.goto(50, -95)
        while i > 0:
            i = i - 1
            turtle.forward(25)
        turtle.write(slovo, move=False, align="center",
            font=("Arial", 24, "normal"))
        k = k + 1
        if k == len(linija):
            turtle.penup()
            turtle.goto(150, -250)
            turtle.write("Čestitamo, pobijedili ste!", move=False,
                align="right", font=("Arial", 24, "normal", "bold"))
            break
    if len(lista) == 0:
        greska = greska + 1
        crtaj_vjesala(greska)
        if greska == 10:
            turtle.penup()
            turtle.goto(150, -350)
            turtle.pendown()
            turtle.write("Žao nam je, izgubili ste.\nRiječ je bila:\n" + linija, move=False,
                align="right", font=("Arial", 24, "normal", "bold"))
            break

input_file.close()
turtle.exitonclick()