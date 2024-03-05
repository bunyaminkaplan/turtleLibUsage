import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Turtle Test")


turtle_instance = turtle.Turtle()

# turtle_instance.forward(100)
# turtle_instance.left(90)
# turtle_instance.forward(100)
# turtle_instance.left(90)
# turtle_instance.forward(100)
# turtle_instance.left(90)
# turtle_instance.forward(100)


turtle_colors = ["yellow" , "purple" , "red" , "blue" , "cyan" , "green"]

def make_a_shape(shape_sides):

    if shape_sides == "star":

       for i in range(5):

           # drawing_board.bgcolor(turtle_colors[i % 6]) -> it changes bgcolor while turtle move
            turtle_instance.forward(100)
            angle = 144
            turtle_instance.left(angle)

    elif shape_sides / 1 > 0:
        for i in range(shape_sides):
            #drawing_board.bgcolor(turtle_colors[i % 6])  -> it changes bgcolor while turtle move
            turtle_instance.forward(100)
            angle = 360.0 / shape_sides
            turtle_instance.left(angle)

    else:
        print("write an integer or star")




def make_a_shrinking_shape(shape_name , tour_number):

    if shape_name == "square":

        forward_distance = 300
        for i in range(tour_number):

            turtle_instance.forward(forward_distance)
            turtle_instance.left(90)
            forward_distance -= 10

    if shape_name == "circle":

        turtle_instance.speed(0)

        forward_distance = 0
        for i in range(tour_number * 360):
            turtle_instance.forward(forward_distance)
            turtle_instance.left(1)
            forward_distance += 0.005


#make_a_shrinking_shape("circle" , 10)








make_a_shape(5)
#make_a_shape("star")







turtle.done()
