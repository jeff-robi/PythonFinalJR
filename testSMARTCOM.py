def playCom(Pturn):
    while Pturn == False:
        if magicSqPl[0][0] = 8 and magicSqPl[0][1] = 1:
            magi

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