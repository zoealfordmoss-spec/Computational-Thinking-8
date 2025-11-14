# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")

def set_image(sprite, image_filename):
    image_file = f"./Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)

def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x,y)
    window.update()
    return sprite

def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)

def draw_rectangle( color="black",x=0,y=0, width=100, height=100,):
	sprite = turtle.Turtle()
	sprite.speed(0)
	sprite.pencolor(color)
	sprite.color(color)
	sprite.penup()
	sprite.goto(x - (width*0.5), y + (height*0.5))
	sprite.pendown()
	sprite.begin_fill()
	for i in range(2):
		sprite.forward(width)
		sprite.right(90)
		sprite.forward(height)
		sprite.right(90)
	sprite.end_fill()
	sprite.hideturtle()


window = turtle.Screen()
window.tracer(0)


# Section 2: Setup
sprite1 = create_sprite("dino_background", 250, 0)
sprite2 = create_sprite("dino", -300, -20)
sprite3 = create_sprite("cacti",-50, -20)
sprite4 = create_sprite("bacti",-100,-20)
sprite5 = create_sprite("facti",  50, -20 )
sprite6 = create_sprite("sacti",  100, -20 )
sprite7 = create_sprite("dacti",  150, -20 )
sprite8 = create_sprite("acti",  200, -20 )
# TODO - set the starting value for your variable

# Section 3: Controls
def jump():
	sprite2.setheading(90)
	sprite2.forward(200)

window.onkeypress(jump, "space")
# TODO - pick keys for each control
speed = 10
# Section 4: Game Loop
window.listen()
timer = 0
while True:
	time.sleep(0.1)
	timer += 1  

	sprite2.setheading(270)
	if sprite2.ycor()> -30:
		sprite2.forward(10)
	 

 	# TODO - code for automatic actions
	sprite1.setheading(180)
	sprite1.forward(speed)
	if sprite1.xcor()<-400:
		sprite1.goto(400,0)

	sprite3.setheading(180)
	sprite3.forward(speed)
	if sprite3.xcor()<-400:
		sprite3.goto(400,0)

	sprite4.setheading(180)
	sprite4.forward(speed)
	if sprite4.xcor()<-400:
		sprite4.goto(400,0)

	sprite5.setheading(180)
	sprite5.forward(speed)
	if sprite5.xcor()<-400:
		sprite5.goto(400,0)

	sprite6.setheading(180)
	sprite6.forward(speed)
	if sprite6.xcor()<-400:
		sprite6.goto(400,0)

	sprite7.setheading(180)
	sprite7.forward(speed)
	if sprite7.xcor()<-400:
		sprite7.goto(400,0)

	sprite8.setheading(180)
	sprite8.forward(speed)
	if sprite8.xcor()<-400:
		sprite8.goto(400,0)
			
	if timer == 600:
		speed = 20



	if get_distance (sprite2, sprite3)< 50:
		break

	if get_distance (sprite2, sprite4)< 50:
		break
	
	if get_distance (sprite2, sprite5)< 50:
		break

	if get_distance (sprite2, sprite6)< 50:
		break

	if get_distance (sprite2, sprite7)< 50:
		 break
	
	if get_distance (sprite2, sprite8)< 50:
		 break
	



	window.update()

	# if :
	# 	break
	

print("Game Over")