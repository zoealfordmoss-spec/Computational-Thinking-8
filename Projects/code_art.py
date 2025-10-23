import turtle
turtle.Screen().bgcolor("pink")
t = turtle.Turtle()
t.speed(9)
# i made the speed a little bit less because they said it was to fast


t.goto(100, 0)
colors =  ["red", "orange", "yellow", "green", "blue", "purple"]
# i did the rainbow because it looks pretty against pink
for i in range(350):
    t.color(colors [ i % 6])
    t.forward(90 + i)
    t.left(46)

turtle.exitonclick()
# i made it at the side becaue i think it looks cooler than in the middle

