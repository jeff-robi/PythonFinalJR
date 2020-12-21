# --- Imported libraries --- #
from tkinter import *
from tkinter import messagebox
import random

# --- Declaring starting variables --- #
window = Tk() #opening window, addign title and setting size
window.title("Tic-Tac-Toe Mania")
window.geometry("600x600")

board = [['-', '-', '-'], #board list for pvp mode
         ['-', '-', '-'], 
         ['-', '-', '-']]

boardCom = [[8, 1, 6], #boardCom list for com mode
            [3, 5, 7], 
            [4, 9, 2]]

magicSqPl = [[0, 0, 0], #magicsquare list for player in com mode
             [0, 0, 0], 
             [0, 0, 0]]

magicSqCom = [[0, 0, 0], #magicsquare list for com in com mode
              [0, 0, 0], 
              [0, 0, 0]]

Xturn = True #Some boolean variables being initialized for later use
Playerturn = True
winner = False
tie = False

# --- Custom functions --- #
def clicked(g,num,num2): #Function for clicking buttons in pvp mode
    global Xturn, board #Making some variables global for function use

    if board[num][num2] == "-" and Xturn == True: #Check to see if player X can play
        g["text"] = "X"
        Xturn = False
        board[num][num2] = "X"
        reset = win() #Check to see if win, if so reset game board for next game
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
    elif board[num][num2] == "-" and Xturn == False: #Check to see if player O can play
        g["text"] = "O"
        Xturn = True
        board[num][num2] = "O"
        reset = win() #Check to see if win, if so reset game board for next game
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
        messagebox.showerror("Wrong move!", "Try again!") #If space is taken, print error

def clickedCom(g,num,num2,c,x1,y2,x3,y4,x5,y6,x7,y8): #Function for clicking buttons in com mode
    global Playerturn, boardCom, magicSqPl, winner, tie #Making some variables global for function use
    
    if winner == False: #Checking if anyone has won
        if boardCom[num][num2] != -1 and Playerturn == True: #Check to see if player X can play
            Playerturn = False
            c.create_line(x1,y2,x3,y4,width=5) #Creating X and placing it
            c.create_line(x5,y6,x7,y8,width=5)
            magicSqPl[num][num2] = boardCom[num][num2] #Adjusting lists for win scan
            boardCom[num][num2] = -1
            winner = winCom() #Testing for winner
            tie = tieCom() #Testing for tie
    
        else:
            messagebox.showerror("Wrong move!", "Try again!") #If space is taken, print error
    
        if winner == False and Playerturn == False and tie == False: #Check to see if Com O can play
            Playerturn = playCom(Playerturn) #Runs com controller function
    elif winner == True: #Checks for winner of game
        tie = False #Makes sure it can't be a tie if its won
        
        boardCom[0][0] = 8 #Resetting all the lists back to default values
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
        
        Playerturn = True #resetting X back to turn 1
        
        return
    elif tie == True: #Checks for tie
        boardCom[0][0] = 8 #Resetting all the lists back to default values
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
        
        Playerturn = True #resetting X back to turn 1
        
        return

def reg(): #Function for building the window for the pvp mode
    reg_win = Toplevel()
    
    grid1 = Button(reg_win, #Code for all the buttons/grid
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

    grid1.grid(row=0, column=0) #Laying out the grid of buttons
    grid2.grid(row=0, column=1)
    grid3.grid(row=0, column=2)
    grid4.grid(row=1, column=0)
    grid5.grid(row=1, column=1)
    grid6.grid(row=1, column=2)
    grid7.grid(row=2, column=0)
    grid8.grid(row=2, column=1)
    grid9.grid(row=2, column=2)

def com(): #Function for building the window for the com mode
    com_win = Tk()
    com_win.geometry("210x320") #Initializing and setting new window size
    global winner #Making winner global for function
    winner = False #Resetting winner to false for new game
    grid1 = Button(com_win, #Code for all the buttons/grid
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

    grid1.grid(row=0, column=0) #Laying out the grid of buttons
    grid2.grid(row=0, column=1)
    grid3.grid(row=0, column=2)
    grid4.grid(row=1, column=0)
    grid5.grid(row=1, column=1)
    grid6.grid(row=1, column=2)
    grid7.grid(row=2, column=0)
    grid8.grid(row=2, column=1)
    grid9.grid(row=2, column=2)
    
    com_can = Tk() #Creating the tic tac toe board drawing for the com mode
    global c
    c = Canvas(com_can,width=300,height=300)
    c.grid(row=0, column=0)
    c.create_line(100,10,100,290)
    c.create_line(200,10,200,290)
    c.create_line(10,100,290,100)
    c.create_line(10,200,290,200)

def win(): #Function for calculating a win in the pvp mode
    win = False #Resetting win to false

    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X": #Checking all possible board wins for each player
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

    return win #Returning the value of win

def winCom(): #Function for calculating a win in the com mode
    win = False #Resetting win to false

    if magicSqPl[0][0] + magicSqPl[0][1] + magicSqPl[0][2] == 15: #Checking all possible board wins for the player and com
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

    return win #Returning the value of win

def tieCom(): #Function for calculating a tie
    tie = False #Resetting tie to false
    
    if boardCom[0][0] == -1 and boardCom[0][1] == -1 and boardCom[0][2] == -1: #Checking to see if all spaces are taken for the tie
        if boardCom[1][0] == -1 and boardCom[1][1] == -1 and boardCom[1][2] == -1:
            if boardCom[2][0] == -1 and boardCom[2][1] == -1 and boardCom[2][2] == -1:
                tie = True #if all spaces are taken, its a tie
                messagebox.showinfo("Tie.", "Looks like no one won...") #Message anmouncing the tie
    return tie #Returning the value of tie

def playCom(Pturn): #Function for computer to play
    while Pturn == False:

        x = random.randint(0, 2) #Random numbers to generate computers play
        y = random.randint(0, 2)

        print(x,y)

        if boardCom[x][y] != -1: #Checking to make sure box isn't taken, then drawing an O to the appropriate box
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
            magicSqCom[x][y] = boardCom[x][y] #Adjusting lists for com square and board
            boardCom[x][y] = -1
            winCom() #Checking for win
            Pturn = True #Setting playerturn to true
            
            return Pturn #Returning value of pturn

# --- Program widgets --- #
title = Label(window, #This code creates the first main window
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
title.grid(padx=25) #This code lays the elements in the main window out neatly
titleSpace.grid()
button_reg.grid()
buttonSpace.grid()
button_5.grid()
buttonSpace2.grid()
exitSpace.grid()
button_exit.grid()

window.mainloop()