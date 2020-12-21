# --- Imported libraries --- #
from tkinter import *
from tkinter import messagebox
import random

# --- Declaring starting variables --- #
window = Tk()
window.title("Tic-Tac-Toe Mania")
window.geometry("600x600")

board = [['-', '-', '-'], 
         ['-', '-', '-'], 
         ['-', '-', '-']]

boardCom = [[8, 1, 6], 
            [3, 5, 7], 
            [4, 9, 2]]

magicSqPl = [[0, 0, 0], 
             [0, 0, 0], 
             [0, 0, 0]]

magicSqCom = [[0, 0, 0], 
              [0, 0, 0], 
              [0, 0, 0]]

Xturn = True
Playerturn = True
winner = False
tie = False

# --- Custom functions --- #
def clicked(g,num,num2):
    global Xturn, board

    if board[num][num2] == "-" and Xturn == True:
        g["text"] = "X"
        Xturn = False
        board[num][num2] = "X"
        reset = win()
        if reset == True:
            board[0][0] = "-"
            board[0][1] = "-"
            board[0][2] = "-"
            board[1][0] = "-"
            board[1][1] = "-"
            board[1][2] = "-"
            board[2][0] = "-"
            board[2][1] = "-"
            board[2][2] = "-"
    elif board[num][num2] == "-" and Xturn == False:
        g["text"] = "O"
        Xturn = True
        board[num][num2] = "O"
        reset = win()
        if reset == True:
            board[0][0] = "-"
            board[0][1] = "-"
            board[0][2] = "-"
            board[1][0] = "-"
            board[1][1] = "-"
            board[1][2] = "-"
            board[2][0] = "-"
            board[2][1] = "-"
            board[2][2] = "-"
    else:
        messagebox.showerror("Wrong move!", "Try again!")

def clickedCom(g,num,num2,c,x1,y2,x3,y4,x5,y6,x7,y8):
    global Playerturn, boardCom, magicSqPl, winner, tie
    
    if winner == False:
        if boardCom[num][num2] != -1 and Playerturn == True:
            Playerturn = False
            c.create_line(x1,y2,x3,y4,width=5)
            c.create_line(x5,y6,x7,y8,width=5)
            magicSqPl[num][num2] = boardCom[num][num2]
            boardCom[num][num2] = -1
            winner = winCom()
            tie = tieCom()
    
        else:
            messagebox.showerror("Wrong move!", "Try again!")
    
        if winner == False and Playerturn == False and tie == False:
            Playerturn = playCom(Playerturn)
    elif winner == True:
        tie = False
        
        boardCom[0][0] = 8
        boardCom[0][1] = 1
        boardCom[0][2] = 6
        boardCom[1][0] = 3
        boardCom[1][1] = 5
        boardCom[1][2] = 7
        boardCom[2][0] = 4
        boardCom[2][1] = 9
        boardCom[2][2] = 2
        
        magicSqPl[0][0] = 0
        magicSqPl[0][1] = 0
        magicSqPl[0][2] = 0
        magicSqPl[1][0] = 0
        magicSqPl[1][1] = 0
        magicSqPl[1][2] = 0
        magicSqPl[2][0] = 0
        magicSqPl[2][1] = 0
        magicSqPl[2][2] = 0
        
        magicSqCom[0][0] = 0
        magicSqCom[0][1] = 0
        magicSqCom[0][2] = 0
        magicSqCom[1][0] = 0
        magicSqCom[1][1] = 0
        magicSqCom[1][2] = 0
        magicSqCom[2][0] = 0
        magicSqCom[2][1] = 0
        magicSqCom[2][2] = 0
        
        Playerturn = True
        
        return
    elif tie == True:
        boardCom[0][0] = 8
        boardCom[0][1] = 1
        boardCom[0][2] = 6
        boardCom[1][0] = 3
        boardCom[1][1] = 5
        boardCom[1][2] = 7
        boardCom[2][0] = 4
        boardCom[2][1] = 9
        boardCom[2][2] = 2
        
        magicSqPl[0][0] = 0
        magicSqPl[0][1] = 0
        magicSqPl[0][2] = 0
        magicSqPl[1][0] = 0
        magicSqPl[1][1] = 0
        magicSqPl[1][2] = 0
        magicSqPl[2][0] = 0
        magicSqPl[2][1] = 0
        magicSqPl[2][2] = 0
        
        magicSqCom[0][0] = 0
        magicSqCom[0][1] = 0
        magicSqCom[0][2] = 0
        magicSqCom[1][0] = 0
        magicSqCom[1][1] = 0
        magicSqCom[1][2] = 0
        magicSqCom[2][0] = 0
        magicSqCom[2][1] = 0
        magicSqCom[2][2] = 0
        
        Playerturn = True
        
        return

def reg():
    reg_win = Toplevel()
    
    grid1 = Button(reg_win,
                        text=" ",
                        font="Times 40",
                        width=4,
                        height=2,
                        command=lambda: clicked(grid1,0,0))
    grid2 = Button(reg_win,
                        text=" ",
                        font="Times 40",
                        width=4,
                        height=2,
                        command=lambda: clicked(grid2,0,1))
    grid3 = Button(reg_win,
                        text=" ",
                        font="Times 40",
                        width=4,
                        height=2,
                        command=lambda: clicked(grid3,0,2))
    grid4 = Button(reg_win,
                        text=" ",
                        font="Times 40",
                        width=4,
                        height=2,
                        command=lambda: clicked(grid4,1,0))
    grid5 = Button(reg_win,
                        text=" ",
                        font="Times 40",
                        width=4,
                        height=2,
                        command=lambda: clicked(grid5,1,1))
    grid6 = Button(reg_win,
                        text=" ",
                        font="Times 40",
                        width=4,
                        height=2,
                        command=lambda: clicked(grid6,1,2))
    grid7 = Button(reg_win,
                        text=" ",
                        font="Times 40",
                        width=4,
                        height=2,
                        command=lambda: clicked(grid7,2,0))
    grid8 = Button(reg_win,
                        text=" ",
                        font="Times 40",
                        width=4,
                        height=2,
                        command=lambda: clicked(grid8,2,1))
    grid9 = Button(reg_win,
                        text=" ",
                        font="Times 40",
                        width=4,
                        height=2,
                        command=lambda: clicked(grid9,2,2))

    grid1.grid(row=0, column=0)
    grid2.grid(row=0, column=1)
    grid3.grid(row=0, column=2)
    grid4.grid(row=1, column=0)
    grid5.grid(row=1, column=1)
    grid6.grid(row=1, column=2)
    grid7.grid(row=2, column=0)
    grid8.grid(row=2, column=1)
    grid9.grid(row=2, column=2)

def com():
    com_win = Tk()
    com_win.geometry("210x320")
    global winner
    winner = False
    grid1 = Button(com_win,
                        text=" ",
                        font="Times 40",
                        width=2,
                        height=1,
                        command=lambda: clickedCom(grid1,0,0,c,10,10,90,90,90,10,10,90))
    grid2 = Button(com_win,
                        text=" ",
                        font="Times 40",
                        width=2,
                        height=1,
                        command=lambda: clickedCom(grid1,0,1,c,110,10,190,90,190,10,110,90))
    grid3 = Button(com_win,
                        text=" ",
                        font="Times 40",
                        width=2,
                        height=1,
                        command=lambda: clickedCom(grid1,0,2,c,210,10,290,90,290,10,210,90))
    grid4 = Button(com_win,
                        text=" ",
                        font="Times 40",
                        width=2,
                        height=1,
                        command=lambda: clickedCom(grid4,1,0,c,10,110,90,190,10,190,90,110))
    grid5 = Button(com_win,
                        text=" ",
                        font="Times 40",
                        width=2,
                        height=1,
                        command=lambda: clickedCom(grid5,1,1,c,110,110,190,190,190,110,110,190))
    grid6 = Button(com_win,
                        text=" ",
                        font="Times 40",
                        width=2,
                        height=1,
                        command=lambda: clickedCom(grid6,1,2,c,210,110,290,190,210,190,290,110))
    grid7 = Button(com_win,
                        text=" ",
                        font="Times 40",
                        width=2,
                        height=1,
                        command=lambda: clickedCom(grid7,2,0,c,10,210,90,290,10,290,90,210))
    grid8 = Button(com_win,
                        text=" ",
                        font="Times 40",
                        width=2,
                        height=1,
                        command=lambda: clickedCom(grid8,2,1,c,110,210,190,290,110,290,190,210))
    grid9 = Button(com_win,
                        text=" ",
                        font="Times 40",
                        width=2,
                        height=1,
                        command=lambda: clickedCom(grid9,2,2,c,210,210,290,290,210,290,290,210))

    grid1.grid(row=0, column=0)
    grid2.grid(row=0, column=1)
    grid3.grid(row=0, column=2)
    grid4.grid(row=1, column=0)
    grid5.grid(row=1, column=1)
    grid6.grid(row=1, column=2)
    grid7.grid(row=2, column=0)
    grid8.grid(row=2, column=1)
    grid9.grid(row=2, column=2)
    
    com_can = Tk()
    global c
    c = Canvas(com_can,width=300,height=300)
    c.grid(row=0, column=0)
    c.create_line(100,10,100,290)
    c.create_line(200,10,200,290)
    c.create_line(10,100,290,100)
    c.create_line(10,200,290,200)

def win():
    win = False

    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")

    return win

def winCom():
    win = False

    if magicSqPl[0][0] + magicSqPl[0][1] + magicSqPl[0][2] == 15:
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif magicSqPl[1][0] + magicSqPl[1][1] + magicSqPl[1][2] == 15:
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif magicSqPl[2][0] + magicSqPl[2][1] + magicSqPl[2][2] == 15:
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif magicSqPl[0][0] + magicSqPl[1][0] + magicSqPl[2][0] == 15:
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif magicSqPl[0][1] + magicSqPl[1][1] + magicSqPl[2][1] == 15:
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif magicSqPl[0][2] + magicSqPl[1][2] + magicSqPl[2][2] == 15:
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif magicSqPl[0][0] + magicSqPl[1][1] + magicSqPl[2][2] == 15:
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif magicSqPl[0][2] + magicSqPl[1][1] + magicSqPl[2][0] == 15:
        win = True
        messagebox.showinfo("Winner!", "Good job, you won!")
    elif magicSqCom[0][0] + magicSqCom[0][1] + magicSqCom[0][2] == 15:
        win = True
        messagebox.showinfo("Game over", "Nice try, the computer won.")
    elif magicSqCom[1][0] + magicSqCom[1][1] + magicSqCom[1][2] == 15:
        win = True
        messagebox.showinfo("Game over", "Nice try, the computer won.")
    elif magicSqCom[2][0] + magicSqCom[2][1] + magicSqCom[2][2] == 15:
        win = True
        messagebox.showinfo("Game over", "Nice try, the computer won.")
    elif magicSqCom[0][0] + magicSqCom[1][0] + magicSqCom[2][0] == 15:
        win = True
        messagebox.showinfo("Game over", "Nice try, the computer won.")
    elif magicSqCom[0][1] + magicSqCom[1][1] + magicSqCom[2][1] == 15:
        win = True
        messagebox.showinfo("Game over", "Nice try, the computer won.")
    elif magicSqCom[0][2] + magicSqCom[1][2] + magicSqCom[2][2] == 15:
        win = True
        messagebox.showinfo("Game over", "Nice try, the computer won.")
    elif magicSqCom[0][0] + magicSqCom[1][1] + magicSqCom[2][2] == 15:
        win = True
        messagebox.showinfo("Game over", "Nice try, the computer won.")
    elif magicSqCom[0][2] + magicSqCom[1][1] + magicSqCom[2][0] == 15:
        win = True
        messagebox.showinfo("Game over", "Nice try, the computer won.")

    return win

def tieCom():
    tie = False
    
    if boardCom[0][0] == -1 and boardCom[0][1] == -1 and boardCom[0][2] == -1:
        if boardCom[1][0] == -1 and boardCom[1][1] == -1 and boardCom[1][2] == -1:
            if boardCom[2][0] == -1 and boardCom[2][1] == -1 and boardCom[2][2] == -1:
                tie = True
                messagebox.showinfo("Tie.", "Looks like no one won...")
    return tie

def playCom(Pturn):
    while Pturn == False:

        x = random.randint(0, 2)
        y = random.randint(0, 2)

        print(x,y)

        if boardCom[x][y] != -1:
            if x == 0 and y == 0:
                c.create_oval(10,10,90,90,width=5)
            elif x == 0 and y == 1:
                c.create_oval(110,10,190,90,width=5)
            elif x == 0 and y == 2:
                c.create_oval(210,10,290,90,width=5)
            elif x == 1 and y == 0:
                c.create_oval(10,110,90,190,width=5)
            elif x == 1 and y == 1:
                c.create_oval(110,110,190,190,width=5)
            elif x == 1 and y == 2:
                c.create_oval(210,110,290,190,width=5)
            elif x == 2 and y == 0:
                c.create_oval(10,210,90,290,width=5)
            elif x == 2 and y == 1:
                c.create_oval(110,210,190,290,width=5)
            elif x == 2 and y == 2:
                c.create_oval(290,290,210,210,width=5)
            magicSqCom[x][y] = boardCom[x][y]
            boardCom[x][y] = -1
            winCom()
            Pturn = True
            
            return Pturn

# --- Program widgets --- #
title = Label(window,
                text="Welcome to Tic-Tac-Toe Mania!!!",
                font="Times 30",
                width=25,
                height=1)
button_reg = Button(window,
                text="VS Player",
                font="Times 20",
                command=reg)
button_5 = Button(window,
                text="VS Com",
                font="Times 20",
                command=com)
button_exit = Button(window,
                text="Exit Game",
                command=window.quit,
                font="Times 12")
titleSpace = Label(window,
                text="",
                width=1,
                height=8)
buttonSpace = Label(window,
                text="",
                width=1,
                height=2)
buttonSpace2 = Label(window,
                text="",
                width=1,
                height=2)
exitSpace = Label(window,
                text="",
                width=1,
                height=9)
#sev_win = Toplevel() 

# --- Opening title window --- #
title.grid(padx=25)
titleSpace.grid()
button_reg.grid()
buttonSpace.grid()
button_5.grid()
buttonSpace2.grid()
exitSpace.grid()
button_exit.grid()

window.mainloop()