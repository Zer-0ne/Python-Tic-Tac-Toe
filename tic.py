from functools import cache
from random import choice
from threading import Thread
from tkinter import *
from tkinter import messagebox
from tkinter import font


@cache
class tic_tac_toe:
    def __init__(self):
        self.b = [[0,0,0],
                [0,0,0],
                [0,0,0]]
        self.root = Tk()
        self.clicked = True
        self.count = 0
        self.players=['O','X']
        self.player = (self.players[0])
        self.root.title('TIC-TAC-TOE')
        self.root.configure(bg='black')
        self.root.resizable(False,False)
        # self.b = [[0,0,0],[0,0,0],[0,0,0]
        self.nav_bar()
        self.frame2 = Frame(self.root).grid(row=0,column=0)
        for row in range(3):
            for column in range(3):
                # self.row_column = self.b[row][column]
                self.b[row][column]= Button(self.frame2,text='',font='helvetica 34',height=6,width=10,border=0,borderwidth=0,bg='black',fg='red',command=lambda row=row,column =column:self.b_click(row,column))
                self.b[row][column].grid(row=row,column=column)
                # self.b['command'] = lambda row=row,column=column: self.b_click(row,column)
        self.footer()
        self.root.mainloop()
    def footer(self):
        self.frame3 = Frame(self.root,relief=SUNKEN).grid(row=100,sticky=S+W+E)
        self.score_x_ = Label(self.frame3,text='X Turns',background='black',foreground='green').grid(row=100,column=0,sticky=S+W+E)
        self.score_y_ = Label(self.frame3,text='O Turns',background='black',foreground='green').grid(row=100,column=1,sticky=S+W+E)
        Label(self.frame3,text='sahil khan',background='black',foreground='green').grid(row=100,column=2,sticky=S+W+E)
    def b_click(self,row,column):
        if self.b[row][column]['text']== '' and self.check_winner() is False:
            if self.player == self.players[0]:
                self.b[row][column]['text'] =self.player
                if self.check_winner() is False:
                    self.player = self.players[1]
                elif self.check_winner() is True:
                    messagebox.showinfo('winner',f'{self.players[0]} win the game!!')
                    self.count =1
                    self.continue_game()
                    self.footer()
                    return True
                elif self.check_winner() == 'Tie':
                    self.q=messagebox.askyesno('Tie the game',"The game is tie\nDo you want to reset the game")
                    if self.q== True:
                        self.reset()
                    else:
                        self.exit_game()
            else:
                if self.player == self.players[1]:
                    self.b[row][column]['text'] =self.player
                    if self.check_winner() is False:
                        self.player = self.players[0]
                    elif self.check_winner() is True:
                        messagebox.showinfo('winner',f'{self.players[1]} win the game!!')
                        
                        self.count =1
                        self.continue_game()
                        self.footer()
                        return False
                    elif self.check_winner() == 'Tie':
                        self.q=messagebox.askyesno('Tie the game',"The game is tie\nDo you want to reset the game")
                        if self.q == True:
                            self.continue_game()
                        else:
                            self.exit_game()
    def continue_game(self):
        cont = messagebox.askyesno('Tic-Tac-Toe','Do yo want to continue the game??')
        if cont==True:
            for row in range(3):
                for column in range(3):
                    self.b[row][column]['text']=''
                    self.b[row][column].config(fg='red')
        else:
            self.exit_game()
    def check_winner(self):
        for row in range(3):
            if self.b[row][0]['text']==self.b[row][1]['text'] ==self.b[row][2]['text'] !='':
                self.b[row][0].config(fg='green')
                self.b[row][1].config(fg='green')
                self.b[row][2].config(fg='green')
                return True
        for column in range(3):
            if self.b[0][column]['text']==self.b[1][column]['text']==self.b[2][column]['text']!='':
                self.b[0][column].config(fg='green')
                self.b[1][column].config(fg='green')
                self.b[2][column].config(fg='green')
                return True
        if self.b[0][0]['text']==self.b[1][1]['text']==self.b[2][2]['text']!='':
            self.b[0][0].config(fg='green')
            self.b[1][1].config(fg='green')
            self.b[2][2].config(fg='green')
            return True
        elif self.b[0][2]['text']==self.b[1][1]['text']==self.b[2][0]['text']!='':
            self.b[0][2].config(fg='green')
            self.b[1][1].config(fg='green')
            self.b[2][0].config(fg='green')
            return True
        elif self.empty_space() is False:
            return 'Tie'
        else:
            return False
    def empty_space(self):
        space = 9
        for row in range(3):
            for column in range(3):
                if self.b[row][column]['text']!='':
                    space-=1
        if space==0:
            return False
        else:
            return True
    def reset(self):
        self.space = 9
        self.clicked = True 
        self.count =0
        for row in range(3):
            for column in range (3):
                self.b[row][column]['text']=''
                self.b[row][column].config(fg='red')

    def exit_game(self):
        exit_ =messagebox.askyesno('Tic-Tac-Toe','Do You Want To Exit The Game')
        if exit_ == True:
            exit()
        # elif self.count==1 :
        #     self.reset()
        else:
            if self.count==1:
                self.reset()
    def nav_bar(self):
        self.font = 'helvetica 16'
        self.frame1 = Frame(self.root).grid(row=50,column=0,sticky='nsew')
        self.menubar = Menu(self.frame1,background='black',
                            foreground='red',activebackground='red',
                            activeforeground='black',font=self.font)
        self.file = Menu(self.menubar,tearoff=0,background='black',foreground='red',activebackground='red',
                            activeforeground='black')
        self.file.add_command(label='New game',font=self.font,command=lambda:self.reset())
        self.file.add_command(label='Reset',font=self.font,command=lambda:self.reset())
        self.file.add_separator()
        self.file.add_command(label='Exit',font=self.font,command=lambda:self.exit_game())
        self.menubar.add_cascade(label='File',menu=self.file)
        self.help = Menu(self.menubar,tearoff=0,background='black',foreground='red',activebackground='red',activeforeground='black')
        self.help.add_command(label='About',font=self.font,command=lambda:self.about())
        self.help.add_command(label='Rule',font=self.font,command=lambda:self.rule())
        self.menubar.add_cascade(label='help',menu=self.help)
        self.root.config(menu=self.menubar)
    
    def about(self):
        messagebox.showinfo('Tic-Tac-Toe','Created By Sahil khan')
    def rule(self):
        messagebox.showinfo('Tic-Tac-Toe','* The game is played on a grid that\'s 3 squares by 3 squares\n\n* You are X, Your friend is O and vise versa\n\n* The first player to get 3 of her marks in a row (up,down,across,or diagonally) is the winner.\n\n* When all 9 square are full the game is over or tie')
    
if __name__ == "__main__":
    tic_tac_toe()