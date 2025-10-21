import turtle
turtle.Screen().bgcolor("pink")
t = turtle.Turtle()
t.speed(9)
# i made the speed a little bit less because they said it was to slow


t.goto(100, 0)
colors =  ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(350):
    t.color(colors [ i % 6])
    t.forward(90 + i)
    t.left(46)

turtle.exitonclick()

