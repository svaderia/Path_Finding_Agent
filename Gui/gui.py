# Shyamal Vaderia : 2015A7PS0048P

from turtle import *
import random


def Screen_init():
    """This function initialize the window and returns required arguments."""
    percentage = input("Enter the percentage of dirt: ")
    matsize = 10
    screen = Screen()
    screen.title("\t"*9 + "Vacuum Cleaner Intelligent Agent")
    screen_width = float(window_width())
    screen_height = float(window_height())
    ht()
    t = Turtle()
    t.ht()
    t.speed(0)
    draw_partition(t, screen_width, screen_height)
    xcord = write_text(screen, t)

    cwidth = ((screen_width/3)-1)/10
    cheight = ((screen_height/2)-1)/10

    grid_1 = [(screen_width/3) - (screen_width/2) + 1, (screen_height/2) - 1]
    grid_2 = [(screen_width/2) - (screen_width/3) + 1, (screen_height/2) - 1]

    draw_grid(t, grid_1, cwidth, cheight)
    draw_grid(t, grid_2, cwidth, cheight)

    dirt_list = generate_reandom_dirt(t, matsize, [grid_1, grid_2], percentage, cwidth, cheight)
    
    return screen, t, grid_1, grid_2, screen_width, screen_height, xcord, dirt_list

def draw_partition(t, width, height):
    """Pratition the window into 5 parts"""
    t.penup()
    t.goto(width/3 - width/2, 0)
    t.pendown()
    # t.fd(height/30) 
    t.penup()
    t.setpos((width/3)-(width/2), (-1 * height)/2)
    t.pendown()
    t.left(90)
    t.pensize(2)
    t.color("red")
    t.fd(height)
    t.color("black")
    t.penup()
    t.penup()
    t.setpos((width/3)-(width/2), 0)
    t.right(90)
    t.pendown()
    t.color("red")
    t.fd(2*width/3)
    t.penup()
    t.setpos((width/2)-(width/3), -1 * (height/2))
    t.left(90)
    t.pendown()
    t.fd(height)
    t.color("black")
    t.penup()

def writer(num,stri,screen,t,for_text_xcor,which_one):
    color = ["IndianRed1", "dodger blue", "spring green"][which_one]
    t.pen(pencolor=color)
    width= float(screen.window_width())
    height= float(screen.window_height())
    t.penup()
    t.goto(for_text_xcor,height/2-20-(num-1)*height/11)
    string=""+stri#+" nodes"
    t.write(string, True,font=("Arial", 12, "normal"))
    return

def write_text(screen,t):
    width= float(screen.window_width())
    height= float(screen.window_height())
    t.penup()
    portion=height/11
    for i in range(11):
        t.goto(-width/2,height/2-20-(i*portion))
        string=" R"+str(i+1)+" : "
        t.write(string, True,font=("Arial", 12, "normal"))
    return t.xcor()

def draw_grid(t, grid, cell_width, cell_height):
    height = float(window_height())
    width = float(window_width())

    t.penup()
    t.setpos(grid[0], grid[1])
    t.right(90)

    for i in range(11):
        t.pendown()
        t.fd((width/3) - 1)
        t.penup()
        t.setpos(grid[0], grid[1] - i*cell_height)

    t.right(90)
    t.penup()
    t.setpos(grid[0], grid[1])

    for i in range(11):
        t.pendown()
        t.fd((height/2) - 1)
        t.penup()
        t.setpos(grid[0] + i*cell_width, grid[1])

    t.penup()
    t.right(180)

def generate_reandom_dirt(t, matsize, grid_coordinates, percentage, cwidth, cheight):
    coord = [[i,j] for i in range(matsize) for j in range(matsize)]
    coord.remove([0,0])
    coord.remove([0,9])
    coord.remove([9,0])
    coord.remove([9,9])
    num = matsize**2*percentage//100
    lst = random.sample(coord, num)
    for dirt in [[0,0],[9,0], [0,9], [9,9]]:
        dirt_coordinate = get_coordinates(grid_coordinates[0], dirt, cwidth, cheight)
        fill_color(t, dirt_coordinate[0], dirt_coordinate[1], "cyan", cwidth, cheight)
        dirt_coordinate = get_coordinates(grid_coordinates[1], dirt, cwidth, cheight)
        fill_color(t, dirt_coordinate[0], dirt_coordinate[1], "cyan", cwidth, cheight)
    for dirt in lst:
		dirt_coordinate = get_coordinates(grid_coordinates[0], dirt, cwidth, cheight)
		fill_color(t, dirt_coordinate[0], dirt_coordinate[1], "gray", cwidth, cheight)
    for dirt in lst:
		dirt_coordinate = get_coordinates(grid_coordinates[1], dirt, cwidth, cheight)
		fill_color(t, dirt_coordinate[0], dirt_coordinate[1], "gray", cwidth, cheight)
    
    return lst
    
def fill_color(dt, start_x, start_y, color, cell_width, cell_height):
	dt.penup()
	dt.setpos(start_x, start_y)
	# Assuming that the turtle is pointing vertically upwards when the function is called.
	dt.fillcolor(color)
	dt.begin_fill()
	dt.pendown()
	dt.right(90)
	dt.fd(cell_width)
	dt.right(90)
	dt.fd(cell_height)
	dt.right(90)
	dt.fd(cell_width)
	dt.right(90)
	dt.fd(cell_height)
	dt.right(90)
	dt.end_fill()
	dt.penup()
	dt.left(90)

def get_coordinates(coordinates, dirt, cell_width, cell_height):
	temp = []
	temp.append(coordinates[0] + dirt[0]*cell_width)
	temp.append(coordinates[1] - dirt[1]*cell_height)
	return temp

def trace_path(action_list, coordinates, width, height, which_one):

    cell_width = ((width/3)-1)/10
    cell_height = ((height/2)-1)/10

    pt = Turtle()
    ft = Turtle()
    f_color = ["IndianRed1", "dodger blue", "spring green"][which_one]
    pen_color = ["orange", "purple", "SpringGreen4"][which_one]
    ft.pen(fillcolor=f_color,pencolor=pen_color,pensize=2)
    pt.pen(fillcolor=f_color,pencolor=pen_color,pensize=2)
    pt_coord = [0, 0]

    pt.speed(5)
    pt.penup()
    pt.setpos((coordinates[0] + cell_width/2, coordinates[1] - cell_height/2))
    pt.pensize(2)
    pt.pendown()

    ft.penup()
    ft.left(90)
    ft.pendown()
    ft.ht()
    ft.speed(0)
    
    for action in action_list:
        if action == "up":
            pt.setheading(90)
            pt.fd(cell_height)
            pt_coord[0] -= 1
        elif action == "right":
            pt.setheading(0)
            pt.fd(cell_width)
            pt_coord[1] += 1
        elif action == "down":
            pt.setheading(270)
            pt.fd(cell_height)
            pt_coord[0] += 1
        elif action == "left":
            pt.setheading(180)
            pt.fd(cell_width)
            pt_coord[1] -= 1
        elif action == "suck":
            fill_color(ft, coordinates[0] + cell_width*pt_coord[1], coordinates[1] - cell_height*pt_coord[0] - (cell_height/2 if which_one ==2 else 0), f_color, cell_width, cell_height/(2 if which_one > 0 else 1))
            


def main():
    Screen_init()
    a = ['right', 'down', 'suck', 'right', 'suck', 'down', 'suck', 'right', 'down', 'suck', 'left', 'down', 'suck', 'right', 'right', 'right', 'down', 'suck', 'up', 'up', 'up', 'right', 'right', 'right', 'suck', 'right','down', 'suck', 'down', 'down', 'down', 'down', 'down', 'down']
    exitonclick()
if __name__ == "__main__":
    main()
