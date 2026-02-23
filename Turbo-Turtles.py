import turtle as t 
import random

screen = t.Screen()
screen.setup(width=500, height=400)
userbet=screen.textinput(title="make you bet",prompt="which turtle will win the race")
colour=["red","orange","yellow","green","blue","purple"]
allturtle=[]

indexy=[-70,-40,-10,20,50,80]

for i in range(0,6):
    tim = t.Turtle(shape='turtle')
    
    tim.penup()
    tim.color(colour[i])
    tim.goto(x=-230, y=indexy[i])
    allturtle.append(tim)
    
if userbet:
    israceon=True
while israceon:
    for turtle in allturtle:
        if turtle.xcor()>230:
            wincolo=turtle.pencolor()
            if wincolo==userbet:
                print("you {wincolo} turtle won you got 1 dollar")
                israceon=False
            else:
                print("Better luck for next time ")
                israceon=False
        else:
            randistance=random.randint(0,10)
            turtle.forward(randistance)

screen.exitonclick()