from tkinter import *
import random

def next_turn(row,column):
    global player
    if buttons[row][column]['text']=="" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]["text"]=player
            if check_winner() is False:
                player=players[1]
                label.config(text=(player +" Turn "))
            elif check_winner() is True:
                label.config(text=(players[0]+" Wins "))
            elif check_winner()=="Tie":
                label.config(text="Tie")
        else:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player=players[0]
                label.config(text=(player +" Turn"))
            elif check_winner() is True:
                label.config(text=(players[1]+" Wins "))
            elif check_winner()=="Tie":
                label.config(text="Tie")

def check_winner():
    for row in range(3):
        if buttons[row][0]['text']==buttons[row][1]['text']==buttons[row][2]['text']!="":
             buttons[row][0].config(bg="Green")
             buttons[row][1].config(bg="Green")
             buttons[row][2].config(bg="Green")    
             return True
    for column in range(3):
        if buttons[0][column]['text']==buttons[1][column]['text']==buttons[2][column]['text']!="":
             buttons[0][column].config(bg="Green")
             buttons[1][column].config(bg="Green")
             buttons[2][column].config(bg="Green")    
             return True
    if buttons[0][0]['text']==buttons[1][1]['text']==buttons[2][2]['text']!="":
        buttons[0][0].config(bg="Green")
        buttons[1][1].config(bg="Green")
        buttons[2][2].config(bg="Green")    
        return True
    elif buttons[0][2]['text']==buttons[1][1]['text']==buttons[2][0]['text']!="":
        buttons[0][2].config(bg="Green")
        buttons[1][1].config(bg="Green")
        buttons[2][0].config(bg="Green")    
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="Yellow")
        return "Tie"
    else:
        return False
    
def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text']!="":
                spaces-=1
    if spaces==0:
        return False
    else:
        return True
    
def new_game():
    global player
    player=random.choice(players)
    label.config(text= player + " Turn")
    
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#FFFFFF")
    

window=Tk()
window.title("Tic-Tac-Toe")
window.configure(bg="grey")
window.geometry("1000x700")
window.resizable(False,False)

players=["X","O"]
player=random.choice(players)

buttons=[[0,0,0],
         [0,0,0],
         [0,0,0],
]

top_frame= Frame(window, bg="#567890",
                 width=1000, height=250
                 )
top_frame.place(x=0,y=0)

game_title=Label(top_frame,bg="#567890",
                 fg="White",text="Tic Tac Toe Game",
                 font=("",50))
game_title.place(x=250,y=0)

reset_button=Button(top_frame,bg="#567890",
                    fg="white",text="Restart Game",
                    font=("arial",20),command=new_game)
reset_button.place(x=400,y=110)

label=Label(top_frame,bg="#567890",
                 fg="White",text=player+" Turn",
                 font=("arial",30))
label.place(x=430,y=200)


bottom_frame=Frame(window,bg="white",
                   width=400,height=350,
                   )
bottom_frame.place(x=300,y=300)

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(bottom_frame,text="",
                                        font=("arial",40),
                                        width=5, height=1, 
                                        command= lambda row=row,
                                        column = column: next_turn(row,column))
        buttons[row][column].grid(row = row, column = column)
        
window.mainloop()