# --- Imported libraries --- #
from tkinter import *
from tkinter import messagebox
# --- Custom functions --- #
def clicked(g,num,num2):
    global Xturn, board

    if board[num][num2] == "-" and Xturn == True:
        g["text"] = "X"
        Xturn = False
        board[num][num2] = "X"
        win()
    elif board[num][num2] == "-" and Xturn == False:
        g["text"] = "O"
        Xturn = True
        board[num][num2] = "O"
        win()
    else:
        messagebox.showerror("Wrong move!", "Try again!")

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
# --- Declaring starting variables --- #
window = Tk()
window.title("Tic-Tac-Toe Mania")
window.geometry("600x600")

board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
Xturn = True

# --- Program widgets --- #
title = Label(window,
                text="Welcome to Tic-Tac-Toe Mania!!!",
                font="Times 30",
                width=25,
                height=1)
button_reg = Button(window,
                text="Regular",
                font="Times 20",
                command=reg)
button_5 = Button(window,
                text="5x5 Board",
                font="Times 20")
button_7 = Button(window,
                text="7x7 Board",
                font="Times 20")
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
#fiv_win = Toplevel()
#sev_win = Toplevel() 

# --- Opening title window --- #
title.grid(padx=25)
titleSpace.grid()
button_reg.grid()
buttonSpace.grid()
button_5.grid()
buttonSpace2.grid()
button_7.grid()
exitSpace.grid()
button_exit.grid()

# --- Main game code --- #


window.mainloop()