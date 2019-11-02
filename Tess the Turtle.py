import turtle
window = turtle.Screen()
backcolor = str(input("Please choose your background color: "))
window.bgcolor(backcolor)
window.title("Hello Tess the Turtle!")

tess = turtle.Turtle()
tesscolor = str(input("Please choose Tess' colour: "))
tess.color(tesscolor)
tess.pensize(3)

tess.forward(150)
tess.left(90)
tess.forward(150)
tess.left(90)
tess.forward(150)
tess.left(90)
tess.forward(150)
tess.left(90)

window.mainloop()
