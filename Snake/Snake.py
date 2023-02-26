import random
from turtle import Screen, Turtle

# side length of squares (used for monsters and snakes)
Dimension = 20

margin = 80
width = 500
upperHeight = 80
lowerHeight = 500
totalHeight = upperHeight + lowerHeight


# use turtle named "turtle" to draw the border of the game display
def window_setup():
    screen.setup(margin*2 + width, margin*2 + totalHeight)

    turtle = Turtle(visible=False)
    turtle.speed(0)  # Max speed
    turtle.pensize(2)
    turtle.penup()
    turtle.goto((width/2, totalHeight/2))
    turtle.pendown()
    turtle.setheading(180)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(totalHeight)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(totalHeight)

    turtle.penup()
    turtle.back(upperHeight)
    turtle.left(90)
    turtle.forward(1)
    turtle.pendown()
    turtle.pensize(4)
    turtle.forward(width - 2)


# random_location used for food items
def random_location():
    x = random.randint(-12, 12)*Dimension
    y = random.randint(-12, 12)*Dimension - upperHeight/2
    return x, y


# set up for the shape color and location of "snake" turtle
def snake_setup():
    snake.speed(0)
    snake.shape("square")
    snake.color("red")
    snake.penup()
    
    snake.goto(0, -upperHeight/2)
    snake.showturtle()


# set the shape and color of the "snakeBody" turtle
def body_setup():
    snakeBody.speed(0)
    snakeBody.shape("square")
    snakeBody.color("blue", "black")
    snakeBody.penup()
    snakeBody.goto(snake.position())


# set the shape and color of the "monster" turtle
# check if the random position is too close to the snake
def monster_setup():
    monster.speed(0)
    monster.shape("square")
    monster.color("green")
    monster.penup()

    while True:
        x = random.randint(-12, 11)*Dimension + Dimension/2
        y = random.randint(-12, 11)*Dimension - upperHeight/2 + Dimension/2
        if abs(x) > Dimension*3 or abs(y + upperHeight/2) > Dimension*3:
            break

    monster.goto(x, y)
    monster.showturtle()


# set up the location of each Turtle
# write corresponding number n in each place
# check if the random position is already contain food or snake
def food_setup(food, n):
    food.speed(0)
    food.penup()

    while True:
        x, y = random_location()
        order = 0
        for i in place:
            if i[0] != x or i[1] != y:
                order += 1
        if order == len(place):
            break

    food.goto(x, y)
    food.write(n,
               align="center", font=("Arial", 12, "normal"))
    place.append(food.position())


# set up to write the contact number
def contact_setup():
    statusContact.clear()
    statusContact.speed(0)
    statusContact.penup()

    statusContact.goto(-width/2 + margin/2,
                       (totalHeight - upperHeight)/2)
    statusContact.write("Contact: %d" % contactNumber,
                        align="left", font=("Arial", 14, "normal"))


# set up to write the time
def time_setup():
    statusTime.clear()
    statusTime.speed(0)
    statusTime.penup()

    statusTime.goto(0, (totalHeight - upperHeight)/2)
    statusTime.write("Time: %d" % time,
                     align="center", font=("Arial", 14, "normal"))


# set up to write the motion
# update variable lastMotion
def motion_setup(motion):
    global lastMotion
    if lastMotion == motion:
        pass
    else:
        statusMotion.clear()
        statusMotion.speed(0)
        statusMotion.penup()

        statusMotion.goto(width/2 - margin/2,
                          (totalHeight - upperHeight)/2)
        statusMotion.write("Motion: %s" % motion,
                           align="right", font=("Arial", 14, "normal"))
        lastMotion = motion


# set up the start notice of the game
def notice_setup():
    notice.speed(0)
    notice.penup()

    notice.goto(-width/2 + Dimension*3,
                totalHeight/2 - upperHeight - Dimension*2)
    notice.write("Welcome to Yuwei's version of snake...",
                 align="left", font=("Arial", 12, "normal"))
    
    notice.goto(-width/2 + Dimension*3,
                totalHeight/2 - upperHeight - Dimension*6)
    notice.write("You are going to use the 4 arrow key to move the snake"
                 "\n('w' for up, 's' for down, 'a' for left, 'd' for right)"
                 "\naround the screen, trying to consume all the food items"
                 "\nbefore the monster catches you...",
                 align="left", font=("Arial", 12, "normal"))

    notice.goto(-width/2 + Dimension*3,
                totalHeight/2 - upperHeight - Dimension*8)
    notice.write("Click anywhere on the screen to start the game, have fun!!",
                 align="left", font=("Arial", 12, "normal"))


# main function - start new game
def main(a, b):
    screen.onclick(None)
    notice.clear()
    
    global place
    place = [(0, 0)]

    monster_setup()

    global snakeBodyStamp
    snakeBodyStamp = list()

    global snakeBodyPlace
    snakeBodyPlace = list()

    food_setup(food1, 1)
    food_setup(food2, 2)
    food_setup(food3, 3)
    food_setup(food4, 4)
    food_setup(food5, 5)
    food_setup(food6, 6)
    food_setup(food7, 7)
    food_setup(food8, 8)
    food_setup(food9, 9)

    body_setup()

    global eatCount
    eatCount = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    global bodyNumber
    bodyNumber = 5

    screen.onkey(up, "w")
    screen.onkey(down, "s")
    screen.onkey(left, "a")
    screen.onkey(right, "d")
    screen.onkey(pause, "space")

    global running
    running = True

    global time
    time = 0

    snake_running()
    monster_running()
    time_count()

    screen.listen()


# set to change the motion_setup and lastMotion "Up"
def up():
    motion_setup("Up")


# set to change the motion_setup and lastMotion "Down"
def down():
    motion_setup("Down")


# set to change the motion_setup and lastMotion "Left"
def left():
    motion_setup("Left")


# set to change the motion_setup and lastMotion "Right"
def right():
    motion_setup("Right")


# set to change the motion_setup and lastMotion "Paused"
def pause():
    motion_setup("Paused")


# use to make the snake move
# use lastMotion to determine the direction of moving
# set different time differentiate the time of producing or not
def snake_running():
    if running:
        if lastMotion == "Up":
            go_up()
        elif lastMotion == "Down":
            go_down()
        elif lastMotion == "Left":
            go_left()
        elif lastMotion == "Right":
            go_right()
        else:
            pass
        if bodyNumber > 0:
            screen.ontimer(snake_running, 500)
        else:
            screen.ontimer(snake_running, 300)


# use to timing
def time_count():
    if running:
        global time
        time += 1
        time_setup()
        screen.ontimer(time_count, 1000)


# use to make the monster move
# the move rate will be variable and random
def monster_running():
    if running:
        move_monster()
        check_snake()
        choice = [200, 300, 400, 500, 600, 700, 800]
        screen.ontimer(monster_running, choice[random.randint(0, 6)])


# check the situation of snake, body, monster, food
def check_snake():
    global bodyNumber
    global contactNumber
    x, y = snake.position()
    x = round(x)
    y = round(y)
    
    a, b = monster.position()
    a = round(a)
    b = round(b)

    # check whether their is contact of snake body and monster
    for i in range(len(snakeBodyPlace) - 1):
        if (abs(round(snakeBodyPlace[i][0]) - a) == Dimension/2
                and abs(round(snakeBodyPlace[i][1]) - b) == Dimension/2):
            contactNumber += 1
            contact_setup()
            break

    # check whether the snake eat the food item
    if place[1][0] == x and place[1][1] == y:
        try:
            del eatCount[eatCount.index(1)]
            food1.clear()
            bodyNumber += 1
        except ValueError:
            pass
    if place[2][0] == x and place[2][1] == y:
        try:
            del eatCount[eatCount.index(2)]
            food2.clear()
            bodyNumber += 2
        except ValueError:
            pass
    if place[3][0] == x and place[3][1] == y:
        try:
            del eatCount[eatCount.index(3)]
            food3.clear()
            bodyNumber += 3
        except ValueError:
            pass
    if place[4][0] == x and place[4][1] == y:
        try:
            del eatCount[eatCount.index(4)]
            food4.clear()
            bodyNumber += 4
        except ValueError:
            pass
    if place[5][0] == x and place[5][1] == y:
        try:
            del eatCount[eatCount.index(5)]
            food5.clear()
            bodyNumber += 5
        except ValueError:
            pass
    if place[6][0] == x and place[6][1] == y:
        try:
            del eatCount[eatCount.index(6)]
            food6.clear()
            bodyNumber += 6
        except ValueError:
            pass
    if place[7][0] == x and place[7][1] == y:
        try:
            del eatCount[eatCount.index(7)]
            food7.clear()
            bodyNumber += 7
        except ValueError:
            pass
    if place[8][0] == x and place[8][1] == y:
        try:
            del eatCount[eatCount.index(8)]
            food8.clear()
            bodyNumber += 8
        except ValueError:
            pass
    if place[9][0] == x and place[9][1] == y:
        try:
            del eatCount[eatCount.index(9)]
            food9.clear()
            bodyNumber += 9
        except ValueError:
            pass

    # check whether the snake catch by monster
    if abs(x-a) == Dimension/2 and abs(y-b) == Dimension/2:
        final_setup("Game over!")

    # check whether snake eat all food items and win
    if len(eatCount) == 0:
        final_setup("Winner!!")


# clear the use of onkey
# set the finalNoticeWord
def final_setup(word):
    x, y = snake.position()
    global running
    running = False
    screen.onkey(None, "w")
    screen.onkey(None, "s")
    screen.onkey(None, "a")
    screen.onkey(None, "d")
    screen.onkey(None, "space")
    finalNoticeWord.penup()
    finalNoticeWord.goto(x, y + Dimension)
    finalNoticeWord.color("purple")
    finalNoticeWord.write(word,
                          font=("Arial", 12, "normal"))


# use to move monster toward the snake
def move_monster():
    x, y = snake.position()
    a, b = monster.position()
    if abs(round(x) - round(a)) == Dimension/2:
        if b < y:
            monster.setheading(90)
            monster.forward(Dimension)
        else:
            monster.setheading(270)
            monster.forward(Dimension)
    elif abs(round(y) - round(b)) == Dimension/2:
        if a < x:
            monster.setheading(0)
            monster.forward(Dimension)
        else:
            monster.setheading(180)
            monster.forward(Dimension)
    else:
        choice = ["horizontal", "vertical"][random.randint(0, 1)]
        if choice == "horizontal":
            if a < x:
                monster.setheading(0)
                monster.forward(Dimension)
            else:
                monster.setheading(180)
                monster.forward(Dimension)
        else:
            if b < y:
                monster.setheading(90)
                monster.forward(Dimension)
            else:
                monster.setheading(270)
                monster.forward(Dimension)


# produce stamp at the position of previous snake position
# add new stampid and position into list
def move_body():
    snakeBodyStamp.append(snakeBody.stamp())
    snakeBodyPlace.append(snake.position())
    snakeBody.goto(snake.position())


# move snake up
def go_up():
    global bodyNumber
    x, y = snake.position()
    if round(y) == totalHeight/2 - upperHeight - Dimension/2:
        pass
    else:
        snake.setheading(90)
        snake.forward(Dimension)
        move_body()
        if bodyNumber > 0:
            bodyNumber -= 1
        else:
            snakeBody.clearstamp(snakeBodyStamp[0])
            del snakeBodyStamp[0]
            del snakeBodyPlace[0]
    check_snake()


# move snake down
def go_down():
    global bodyNumber
    x, y = snake.position()
    if round(y) == -totalHeight/2 + Dimension/2:
        pass
    else:
        snake.setheading(270)
        snake.forward(Dimension)
        move_body()
        if bodyNumber > 0:
            bodyNumber -= 1
        else:
            snakeBody.clearstamp(snakeBodyStamp[0])
            del snakeBodyStamp[0]
            del snakeBodyPlace[0]
    check_snake()


# move snake left
def go_left():
    global bodyNumber
    x, y = snake.position()
    if round(x) == -width/2 + Dimension/2:
        pass
    else:
        snake.setheading(180)
        snake.forward(Dimension)
        move_body()
        if bodyNumber > 0:
            bodyNumber -= 1
        else:
            snakeBody.clearstamp(snakeBodyStamp[0])
            del snakeBodyStamp[0]
            del snakeBodyPlace[0]
    check_snake()


# move snake right
def go_right():
    global bodyNumber
    x, y = snake.position()
    if round(x) == width/2 - Dimension/2:
        pass
    else:
        snake.setheading(0)
        snake.forward(Dimension)
        move_body()
        if bodyNumber > 0:
            bodyNumber -= 1
        else:
            snakeBody.clearstamp(snakeBodyStamp[0])
            del snakeBodyStamp[0]
            del snakeBodyPlace[0]
    check_snake()


screen = Screen()
window_setup()

contactNumber = 0

statusContact = Turtle(visible=False)
statusTime = Turtle(visible=False)
statusMotion = Turtle(visible=False)
contact_setup()

time = 0
time_setup()

lastMotion = ""
motion_setup("Paused")

notice = Turtle(visible=False)
notice_setup()

monster = Turtle(visible=False)
snake = Turtle(visible=False)

snake_setup()
monster_setup()

food1 = Turtle(visible=False)
food2 = Turtle(visible=False)
food3 = Turtle(visible=False)
food4 = Turtle(visible=False)
food5 = Turtle(visible=False)
food6 = Turtle(visible=False)
food7 = Turtle(visible=False)
food8 = Turtle(visible=False)
food9 = Turtle(visible=False)

finalNoticeWord = Turtle(visible=False)
snakeBody = Turtle(visible=False)

screen.onclick(main)

screen.mainloop()
