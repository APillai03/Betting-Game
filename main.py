import turtle,random  
root = turtle.Screen()
root.setup(height=500,width=500)
root.bgcolor('black')
root.title("Betting Game")
race = False
colors = ['red','green','blue','purple','yellow','white']
pos = [90,60,30,0,-30,-60]
turtles = []
for i in range(6):
    t1 = turtle.Turtle(shape='turtle')
    t1.color(colors[i])
    t1.penup()
    t1.goto(x=-240,y=pos[i])
    t1.pendown()
    turtles.append(t1)
bet = root.textinput(title='BET',prompt='Who will win the race(Enter a color): ')
bet = bet.lower()
my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.goto(-100, 200)
my_turtle.color("White")

while(bet not in colors):
    my_turtle.write("Please enter the correct color!", font=("Arial", 16, "italic",'bold'))
    bet = root.textinput(title='BET',prompt='Who will win the race(Enter a color): ')
if bet:
    my_turtle.clear()
    race = True
while race:
    for t1 in turtles:
        if(t1.xcor()>230):
            race = False
            winner = t1.pencolor()
            if(winner==bet):
                my_turtle.write("You Win!!", font=("Arial", 16, "italic"))
                break
            else:
                my_turtle.write(f"You lost {winner} Won!!", font=("Arial", 20, "italic"))
                break
        t1.forward(random.randint(0,10))

root.exitonclick()