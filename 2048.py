#This program is a 2048 clone for Python. The original code is licensed under the MIT license.
#The object of the game is to combine numbered tiles by sliding them on a 4x4 grid to create a tile with the number 2048.
#If the grid is filled with numbers in such a way that no more moves can be made, you lose.
#Written in Python 2.7.6


import random
import copy

print "Welcome to 2048!"
print "Move left (l), right(r), up(u), or down (d) by entering the appropriate keys."


class Grid():
    state = [[list([0,False]) for i in range(4)] for i in range(4)]

    def placeNew(self):
        #Places a new value into the grid, either a 2 or a 4.
        while True:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if self.state[y][x][0] == 0:
                if random.randint(0, 9) == 0:
                    self.state[y][x][0] = 2
                else:
                    self.state[y][x][0] = 1
                break

    def move(self, x, y, direc):
        #Moves a cell as far as it can, including merging (but it will only merge once)
        nx = x+direc[0]
        ny = y+direc[1]
        global score
        if nx < 0 or nx > 3 or ny < 0 or ny > 3:
            return
        else:
            os = self.state[y][x][0]
            ns = self.state[ny][nx][0]
            if os != ns and ns != 0:
                return
            elif ns == 0:
                self.state[y][x][0] = 0
                self.state[ny][nx][0] = os
                self.move(nx, ny, direc)
            else:
                if not(self.state[y][x][1]):
                    score += (self.state[y][x][0] * 4)
                    self.state[y][x] = [0,False]
                    self.state[ny][nx] = [self.state[ny][nx][0] + 1, True]
                    self.move(nx, ny, direc)
                    
                    
        for x in range(4):
            for y in range(4):
                self.state[y][x][1] = False

    def isDone(self):
        #Returns False if there are still valid moves left, True if no more moves can be made.
        for x in range(4):
            for y in range(4):
                if not(self.state[y][x][0] == 0):
                    return False
        for i in range(3):
            for j in range(4):
                if self.state[i][j][0] == self.state[i+1][j][0]:
                    return False
                if self.state[j][i][0] == self.state[j][i+1][0]:
                    return False
        return True

    def shift(self, direc):
        #Shifts everything in the grid in the direction of direc, if it can. Can only shift if there is at least one possible
        #combination of values to be made, or as long as there is space.
        rstate = copy.deepcopy(self.state)
        rangex = range(4)
        rangey = range(4)
        if direc[0]:
            if direc[0] == 1:
                rangex = rangex[::-1]
            for x in rangex:
                for y in rangey:
                    self.move(x,y,direc)
        if direc[1]:
            if direc[1] == 1:
                rangey = rangey[::-1]
            for y in rangey:
                for x in rangex:
                    self.move(x,y,direc)


        if self.state != rstate:
            self.placeNew()




##init
score = 0
     
stage = Grid()
for i in range(2):
    stage.placeNew()



while(not(stage.isDone())):
    print "score =", score
    for i in range(4):
        out = ""
        for j in range(4):
            cell = stage.state[i][j][0]
            if cell:
                out += str(2 ** cell) + " "
            else:
                out += "0 "
        print out

    uinput = raw_input()
    if uinput == "l":
        direc = [-1,0]
    elif uinput == "r":
        direc = [1,0]
    elif uinput == "u":
        direc = [0,-1]
    elif uinput == "d":
        direc = [0,1]
    else:
        print "please enter valid input"
        continue
    stage.shift(direc)
print "you lose"

#The MIT License (MIT)

#Copyright (c) 2014 Gabriele Cirulli

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
