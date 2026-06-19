import turtle
screen = turtle.Screen()
turtle.speed(0)

def something():
    turtle.pensize("2")
    turtle.color("white")
    turtle.bgcolor("black")
    i = 0
    while i < 4:
        turtle.forward(100)
        turtle.left(90)
        i += 1
   
y = -150
d = 0
while d < 3:
    turtle.penup()
    turtle.goto(x= -150,y=y)
    turtle.pendown()
    a = 0
    while a < 3:
        something()
        turtle.forward(100)
        a += 1
    y += 100
    d += 1
    
    
list_of_y = [150,50,-50,]  
list_of_x = [-150,-50,50,]
list_of_x_y = [[-150,150],[-50,150],[50,150],[-150,50],[-50,50],[50,50],[-150,-50],[-50,-50],[50,-50]]
list_of_zero = [0,0,0,0,0,0,0,0,0,]
turn = 1

game_over = False
list_victory = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]


   
def found_cr(x, y):
    global turn
    if game_over == False:
        for element_1 in list_of_y:
            if element_1 > y and element_1 - 100 < y:
                for element_2 in list_of_x:
                    if  element_2 < x and element_2 + 100 > x:
                        print(element_1)
                        print(element_2)
                        print(x,y)
                        count = 0
                        for element_3 in list_of_x_y:
                            if element_3[0] == element_2:
                                if element_3 [1] == element_1:
                                    if list_of_zero[count] == 0:
                                        if turn == 1:      
                                            criss(element_2, element_1)
                                            list_of_zero[count] = 1
                                            check_victory()
                                            turn = 2
                                        elif turn == 2:
                                            circle(element_2, element_1)
                                            list_of_zero[count] = 2
                                            check_victory()
                                            turn = 1
                            count += 1            

 
    
def criss(x: float,y: float):
    turtle.color("Plum1")
    turtle.pensize("3")
    turtle.penup()
    turtle.goto(x=x,y=y)
    turtle.pendown()
    turtle.goto(x=x+100,y=y-100)
    turtle.penup()
    turtle.goto(x=x+100,y=y)
    turtle.pendown()
    turtle.goto(x=x,y=y-100)
    
def circle(x: float, y: float):
    turtle.color("Magenta")
    turtle.pensize("3")
    turtle.penup()
    turtle.goto(x=x+50,y=y-100)
    turtle.pendown()
    turtle.circle(50)
 
 
def check_draw(): 
    global game_over
    draw = True
    for element in list_of_zero:
        if element == 0:
            draw = False
    if draw == True:
        turtle.penup()
        turtle.goto(0,200)
        turtle.hideturtle()
        turtle.color("LightSlateBlue")
        turtle.write("Нічия",False, "center", font=["Arial", 33, "italic"] )
        print("Нічия")
        game_over = True
 
def check_victory():
    global turn
    global game_over
    victory = []
    for victory in list_victory:
        if list_of_zero[victory[0]] == list_of_zero[victory[1]] == list_of_zero[victory[2]]:
            if list_of_zero[victory[0]] != 0:
                game_over = True
                draw_line(start_index= victory[0], end_index= victory[2])
                turtle.penup()
                turtle.goto(0,200)
                turtle.hideturtle()
                turtle.color("violet")
                turtle.write(f"Переміг гравець №{turn}", False, "center", font= ["Arial", 33, "italic"])
                print("Переміг гравець №",turn)
    if game_over == False:
        check_draw() 
        
def draw_line(start_index, end_index):
    turtle.color("OrangeRed")
    turtle.pensize("5")
    if end_index - start_index == 2:
        start_x = list_of_x_y[start_index][0]   
        start_y = list_of_x_y[start_index][1]- 50
        end_x = list_of_x_y[end_index][0]+ 100
        end_y = list_of_x_y[end_index][1] - 50
        
    elif end_index - start_index == 6:
        start_x = list_of_x_y[start_index][0] + 50   
        start_y = list_of_x_y[start_index][1]
        end_x = list_of_x_y[end_index][0]+ 50
        end_y = list_of_x_y[end_index][1] - 100
        
    elif end_index - start_index == 8:
        start_x = list_of_x_y[start_index][0]  
        start_y = list_of_x_y[start_index][1]
        end_x = list_of_x_y[end_index][0]+ 100
        end_y = list_of_x_y[end_index][1] - 100
        
    elif end_index - start_index == 4:
        start_x = list_of_x_y[start_index][0] + 100  
        start_y = list_of_x_y[start_index][1]
        end_x = list_of_x_y[end_index][0]
        end_y = list_of_x_y[end_index][1] - 100
        
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()
    turtle.goto(end_x, end_y)
    
screen.onscreenclick(found_cr, btn = 2)
turtle.mainloop()
