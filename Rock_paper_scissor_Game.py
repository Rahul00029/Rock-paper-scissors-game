import tkinter
import tkinter.messagebox
from tkinter import *
from PIL import Image,ImageTk
from random import randint

win=Tk()
win.title("Rock Paper Scissor Game")
win.config(background="black")
win.resizable("false","false")

image_rock1=ImageTk.PhotoImage(Image.open("left rock.png"))
image_paper1=ImageTk.PhotoImage(Image.open("left paper.png"))
image_scissor1=ImageTk.PhotoImage(Image.open("left scissors.png"))

image_rock2=ImageTk.PhotoImage(Image.open("right rock.png"))
image_paper2=ImageTk.PhotoImage(Image.open("right paper.png"))
image_scissor2=ImageTk.PhotoImage(Image.open("right scissors.png"))


label_computer=Label(win,image=image_scissor1)
label_player=Label(win,image=image_scissor2)
label_computer.grid(row=1,column=0)
label_player.grid(row=1,column=4)

computer_score=Label(win, text=0, font=("arial",60,"bold"), fg="red")
player_score=Label(win, text=0, font=("arial",60,"bold"), fg="red")
computer_score.grid(row=1,column=1)
player_score.grid(row=1,column=3)

computer_indicator=Label(win,font=("arial",35,"bold"),text="COMPUTER",bg="orange",fg="white")
player_indicator=Label(win,font=("arial",35,"bold"),text="PLAYER",bg="orange",fg="white")
computer_indicator.grid(row=0,column=1)
player_indicator.grid(row=0,column=3)

final_messaage=Label(win,font=("arial",20,"bold"),bg="red",fg="pink")
final_messaage.grid(row=3,column=2)

def msg_update(a):
    final_messaage["text"]=a

def reset():
    computer_score['text'] = 0
    player_score["text"] = 0
    final_messaage["text"] = ""
    label_computer["image"] = image_scissor1
    label_player["image"] = image_scissor2


def C_score_update():
    final=int(computer_score['text'])
    final+=1
    computer_score["text"]=str(final)
    if final==10:
        tkinter.messagebox.showinfo("Final Result","Sorry,You loss the Game!\nBetter luck for next time!!")
        reset()

def P_score_update():
    final=int(player_score['text'])
    final+=1
    player_score["text"]=str(final)
    if final==10:
        tkinter.messagebox.showinfo("Final Result","Wow,You win the Game!!")
        reset()


def winner_check(p,c):
    if p==c:
        msg_update("It's a tie")
    elif p=="rock":
        if c=="paper":
            msg_update("Computer Wins !!")
            C_score_update()
        else:
            msg_update("Player Wins !!")
            P_score_update()
    elif p=="paper":
        if c=="scissor":
            msg_update("Computer Wins !!")
            C_score_update()
        else:
            msg_update("Player Wins !!")
            P_score_update()
    elif p=="scissor":
        if c=="rock":
            msg_update("Computer Wins !!")
            C_score_update()
        else:
            msg_update("Player Wins !!")
            P_score_update()
    else:
        pass
to_select=["rock","paper","scissor"]

def choice_update(a):
    choice_computer=to_select[randint(0,2)]
    if choice_computer=="rock":
        label_computer.configure(image=image_rock1)
    elif choice_computer=="paper":
        label_computer.configure(image=image_paper1)
    else:
        label_computer.configure(image=image_scissor1)
    if a=="rock":
        label_player.configure(image=image_rock2)
    elif a=="paper":
        label_player.configure(image=image_paper2)
    else:
        label_player.configure(image=image_scissor2)
    winner_check(a,choice_computer)

b_rock=Button(win,width=16,height=3,text="ROCK",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("rock")).grid(row=2,column=1)
b_paper=Button(win,width=16,height=3,text="PAPER",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("paper")).grid(row=2,column=2)
b_scissor=Button(win,width=16,height=3,text="SCISSOR",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("scissor")).grid(row=2,column=3)


win.mainloop()