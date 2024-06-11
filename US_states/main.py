import turtle
import pandas

data=pandas.read_csv("50_states.csv")
states=data.state.to_list()
print(states)

screen=turtle.Screen()
img="blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

def get_corr(x,y):
    print(x,y)




game_on=True
answers=[]
total_states=0
while game_on and total_states<50:
    answer = screen.textinput(title=f"{total_states}/50 - Guess the state?", prompt="Name?")
    answer_title = answer.title()
    print(answer_title)
    if answer_title in states:
        new_state = turtle.Turtle()
        answers.append(answer_title)
        answer_state=data[data.state==answer_title]
        new_x=float(answer_state.x)
        new_y=float(answer_state.y)
        new_state.penup()
        new_state.goto(new_x,new_y)
        new_state.write(answer_title)
        total_states +=1
    else:
        print("Not there")

turtle.onscreenclick(get_corr)
turtle.mainloop()