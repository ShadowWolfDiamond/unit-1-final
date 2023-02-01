import turtle
t = turtle.Turtle()
s = turtle.Screen()
k = 1

#Body
t.color("#361356")
t.begin_fill()
t.forward(200)
t.right(90)
t.forward(100)
t.right(90)
t.forward(200)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()

#Head
t.color("#361356")
t.begin_fill()
t.forward(60)
t.left(90)
t.forward(80)
t.left(90)
t.forward(90)
t.left(90)
t.forward(80)
t.left(90)
t.forward(230)
t.left(90)
t.end_fill()

#Tail
t.color("#361356")
t.begin_fill()
t.right(120)
t.forward(250)
t.right(160)
t.forward(230)
t.end_fill()

#Legs
t.color("black", "#361356")
t.begin_fill()
t.left(60)
t.forward(100)
t.left(130)
t.right(90)
t.forward(30)
t.right(90)
t.forward(60)
t.forward(30)
t.right(90)
t.forward(30)
t.right(90)
t.forward(60)
t.left(90)
t.forward(65)
t.end_fill()

#Wings
t.color("#8C2F5E")
t.begin_fill()
t.left(120)
t.forward(70)
t.left(30)
t.forward(20)
t.right(90)
t.forward(26)
t.right(90)
t.forward(26)
t.right(30)
t.forward(250)

#spikes
t.right(180)
t.forward(30)
t.right(180)
t.end_fill()

t.color("#8C2F5E")
t.begin_fill()
while k <= 6:
    k += 1
    t.right(20)
    t.forward(40)
    t.right(120)
    t.forward(30)
    t.left(120)
    t.forward(40)
t.end_fill()


s.exitonclick()
