'''
Created on Apr 1, 2015


@author: Garrett
'''
import csv, math




grid = []
rows = []
collumns = []
boxes = []
squares = []
with open('easy_sudoku.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    #print repr(open('easy_sudoku.csv', 'rb').read(200)) # dump 1st 200 bytes of file
    for row in reader:
        if len(row) == 9:
            grid.append(row)
            #print row1
        #print row
    #print grid






   
class Grid:
    
    #grid = []
    #constructor
    def __init__(self):
        self.row = []
        #grid = []
        #self.grid = grid
        #self.grid = []
        
def print_grid():
    h = 0
    for x in grid:
        #h = 0
        h += 1
        if h % 3 == 0:
            #print ("__________________________________")
            l = 0
            for i in x:
                if l == 8:
                    if i == '':
                        print i, "  | "
                    else:
                        print i, " | "
                    print ("_____________________________________________________")
                else: 
                    if i == '':
                        print i, "  | ",
                    else:
                        print i, " | ",
                l += 1
            print
        #h += 1
        else:
            for i in x:
                if i == '':
                    print i, "  | ",
                else:
                    print i, " | ", 
            print
        


#creating row class
class Row:
    
    #ID
    #Filled
    #needs list
    #left will be a counter starting at 9 that is decremented during update_needs
    
    def __init__(self, ID):
        #ID will be a number 1 - 9 (whatever the vertical coordinate is)
        self.ID = ID
        #creating needs array
        #self.grid = grid
        #unfilled array keeps track of which indices in the row are unfilled
        self.unfilled = []
        #binary array to store which numbers are in the row (index + 1)
        self.contents = []
        self.needs = []
        #initializing needs list to be all ones
        for i in range(9):
            self.unfilled.append(1)
            self.contents.append(0)
            self.needs.append(1)
        self.left = 9
         
        
       
        
        
    #method to update the needs list
    #needs is a binary list; 1 if it needs a number, 0 if it does not have it
    
    def update_unfilled(self):
        #iterator
        i = 0
        #keeps track of number left
        c = 0
        for x in grid[self.ID]:
            #keeps track of number left
            #c = 0
            if x == '':
                self.unfilled[i] = 0
                c += 1
            i += 1
        #setting new value of the number of spaces left to fill
        self.left = c
            
    #method to update contents and needs array
    def update_contents(self):
        #i = 0
        for x in grid[self.ID]:
            if x != '':
                i = int(x)
                self.contents[i - 1] = 1
                self.needs[i - 1] = 0
                
    
    
    #boolean method to check if row is filled
    #if left > 0, not filled (false); if left = 0, true
    def filled(self):
        if self.left > 0:
            return False
        else:
            return True
    
#creating collumn class
class Collumn:
    
    #ID
    #Filled
    #needs list
    #left will be a counter starting at 9 that is decremented during update_needs
    
    def __init__(self, ID):
        #ID will be a number 1 - 9 (whatever the horizontal coordinate is)
        self.ID = ID
        #creating needs array
        #self.grid = grid
        self.unfilled = []
        self.contents = []
        self.needs = []
        #initializing needs list to be all ones
        for i in range(9):
            self.unfilled.append(1)
            self.contents.append(0)
            self.needs.append(1)
        self.left = 9
        
        
    #method to update the needs list
    #needs is a binary list; 1 if it needs it, 0 if it does not have it
    
    def update_unfilled(self):
        #iterator
        i = 0
        #keeps track of number left
        c = 0
        for x in grid:
            #keeps track of number left
            #c = 0
            if x[self.ID] == '':
                self.unfilled[i] = 0
                c += 1
            i += 1
            #print x
        self.left = c
            
    #boolean method to check if row is filled
    #if left > 0, not filled (false); if left = 0, true
    def filled(self):
        if self.left > 0:
            return False
        else:
            return True
    
    #method to update contents and needs array
    def update_contents(self):
        i = 0
        for x in grid:
            if x[self.ID] != '':
                j = int(x[self.ID])
                self.contents[j - 1] = 1
                self.needs[j - 1] = 0
            i += 1
                  
    
    
#creating box class
class Box:
    
    #X and Y give coordinates of upper left of box
    #X
    #Y
    #Filled
    #needs list
    #left will be a counter starting at 9 that is decremented during update_needs
    
    def __init__(self, X, Y):
        #ID will be a number 1 - 9 (whatever the horizontal coordinate is)
        self.X = X
        self.Y = Y
        #creating needs array
        #self.grid = grid
        self.unfilled = []
        self.contents = []
        self.needs = []
        #initializing needs list to be all ones
        for i in range(9):
            self.unfilled.append(1)
            self.contents.append(0)
            self.needs.append(1)
        self.left = 9
        
        
    #method to update the needs list
    #needs is a binary list; 1 if it needs it, 0 if it does not have it
    
    def update_unfilled(self):
        #iterator
        n = 0
        #temp variable to keep track of left
        c = 0
        x = self.X
        y = self.Y
        for i in range(3):
            rw = grid[y + i]
            #print rw
            for j in range(3):
                if rw[(x + j)] != '':
                    #print rw[x + j]
                    self.unfilled[n] = 0
                    c += 1
                n += 1
            #print x
        self.left = c
    
    def update_contents(self):
        #iterator
        n = 0
        x = self.X
        y = self.Y
        for i in range(3):
            rw = grid[x + i]
            #print rw
            for j in range(3):
                e = rw[(y + j)]
                if e != '':
                    m = int(e) - 1
                    self.contents[m] = 1
                    self.needs[m] = 0
                n += 1
    
    
    #boolean method to check if row is filled
    #if left > 0, not filled (false); if left = 0, true
    def filled(self):
        if self.left > 0:
            return False
        else:
            return True
    


#creating square class
class Square:
    
    #filled
    #possibles (binary list for possible numbers in index + 1)
    
    def __init__(self, X, Y):
        self.row = X
        self.collumn = Y
        #creating box IDs
        self.bx = X - (X % 3)
        self.by = Y - (Y % 3)
        e = grid[X]
        self.value = e[Y]
        if e[Y] == '':
            self.filled = False
        else:
            self.filled = True
        self.possibles = []
        #initializing possibles array to have all 1's
        for i in range(9):
            if self.filled == False:
                self.possibles.append(1)
            else:
                self.possibles.append(0)
        '''
        if self.filled == False:
            #for each element in the row
            for m in e:
                if m != '':
                    self.possibles[int(m) - 1] = 0
                    '''
                    
    #method to update possibles array
    def update_possibles(self):
        #updating possibles for row
        e = grid[self.row]
        print "row ", self.row + 1, ": ", e
        #print "self.collumn = ", self.collumn
        if self.filled == False:
            #for each element in the row
            for m in e:
                if m != '':
                    #print int(m) - 1
                    self.possibles[int(m) - 1] = 0
            #print self.possibles
            #updating for collumn
            for x in grid:
                if x[self.collumn] != '':
                    #print int(x[self.collumn]) - 1
                    self.possibles[int(x[self.collumn]) - 1] = 0
            #print self.possibles
            #updating for box
            for i in range(3):
                rw = grid[self.bx + i]
                #print "row is  : ", rw
                for j in range(3):
                    if rw[self.by + j] != '':
                        #print rw[self.by + j]
                        self.possibles[int(rw[self.by + j]) - 1] = 0
            print "Possibles array for ", self.row, ", ", self.collumn, " is: ", self.possibles
    #method to solve the value of the square
    #using possibles array, see if there is only one possible value
    #to do this, append all numbers that have a one to a separate array
    #if only one index has a 1 (length of new array = 1), then that must be the value for that square
    def solve_square(self):
        #only do this method if the square is unfilled
        #updating possibles array
        self.update_possibles()
        if self.filled == False:
            #updating possibles array
            #self.update_possibles()
            #array to keep track of which numbers are possible
            ones = []
            #updating ones array to keep track of possible numbers
            for i in range(9):
                if self.possibles[i] == 1:
                    ones.append(i + 1)
            #if there is only one element in possibles array, then update the grid and mark square as unfilled
            if len(ones) == 1:
                e = grid[self.row]
                e[self.collumn] = ones[0]
                self.value = ones[0]
                self.filled = True
                print "Square ", self.row, self.collumn, " is solved and equals ", e[self.collumn]
             


#putting everything in rows, grids, boxes, squares
def create_grid():
    #i = 0
    for i in range(9):
        r = Row(i)
        #print "Row ", i+1, ": ", r
        rows.append(r)
        #adding collumns
        c = Collumn(i)
        collumns.append(c)
        #adding box and squares
        for j in range(9):
            #adding square
            s = Square(i, j)
            squares.append(s)
            if i % 3 == 0 and j % 3 == 0:
                b = Box(i, j)
                boxes.append(b)
        


#takes input row ID, which finds the row from Rows array
def test_solve_row(ID):
    #getting appropriate row from rows array
    r = rows[ID]
    for i in range(9):
        #updating unfilled array
        r.update_unfilled()
        r.update_contents()
        #print "Row ", ID, ": ", r.contents
        #print r.filled()
        #only solve the row if it is unfilled
        if r.filled() == False:
            #print r.filled()
            #updating unfilled array
            #row number is ID, collumn number is i
            s = Square(ID, i)
            #updating possibles array
            #s.update_possibles()
            #print "Square ", ID, ", ", i
            s.solve_square()
            #print s.possibles




#takes input collumn ID, which finds the collumn from Collumns array
def test_solve_collumn(ID):
    #getting appropriate col from collumns array
    c = collumns[ID]
    for i in range(9):
        #updating unfilled array
        c.update_unfilled()
        c.update_contents()
        #print "Here is the needs array", c.needs
        print
        #print "Row ", ID, ": ", r.contents
        #print c.filled()
        #only continue if column is unfilled and if the column needs that number
        if c.filled() == False and c.needs[i] == 1:
            #going through each square in collumn to see if it could possibly hold value i
            #add all the squares possible to an array called possies
            #if the length of that array is 1, then the square in the array have value i
            possies = []
            #variable to keep track of length of possies; will be incremented each time square is added to array
            #if plen > 1; break out of loop because cannot determine value
            print
            print "Test for ", i + 1
            print
            plen = 0
            for j in range(9):
                #if more than one square in possies array, break out of loop
                if plen > 1:
                    print "breaking out of loop"
                    break
                s = Square(j, ID)
                s.update_possibles()
                if s.possibles[i] == 1:
                    print
                    print "Appending ", s.row, ", ", s.collumn, "for value ", i + 1
                    print
                    possies.append(s)
                    plen += 1
            if plen == 1:
                #s.value = possies[0]
                #updating left field for collumn to see if it is filled
                #c.left -= 1
                e = grid[possies[0].row]
                e[ID] = i + 1
                print "plen is 1 and value is ", i
                


#takes input row ID, which finds the row from Rows array
def test_solve_row2(ID):
    #getting appropriate col from collumns array
    r = rows[ID]
    #i is the number we are trying to solve for in each row
    for i in range(9):
        #updating unfilled array
        r.update_unfilled()
        r.update_contents()
        #print "Here is the needs array", c.needs
        print
        #print "Row ", ID, ": ", r.contents
        #print c.filled()
        #only continue if row is unfilled and if the row needs that number
        if r.filled() == False and r.needs[i] == 1:
            #going through each square in collumn to see if it could possibly hold value i
            #add all the squares possible to an array called possies
            #if the length of that array is 1, then the square in the array have value i
            possies = []
            #variable to keep track of length of possies; will be incremented each time square is added to array
            #if plen > 1; break out of loop because cannot determine value
            print
            print "Test for ", i + 1
            print
            plen = 0
            for j in range(9):
                #if more than one square in possies array, break out of loop
                if plen > 1:
                    print "breaking out of loop"
                    break
                s = Square(ID, j)
                s.update_possibles()
                if s.possibles[i] == 1:
                    print
                    print "Appending ", s.row, ", ", s.collumn, "for value ", i + 1
                    print
                    possies.append(s)
                    plen += 1
            if plen == 1:
                #s.value = possies[0]
                #updating left field for collumn to see if it is filled
                #c.left -= 1
                e = grid[ID]
                e[possies[0].collumn] = i + 1
                print "plen is 1 and value is ", i
            


#takes input box X and Y coordinates, which finds the box from boxes array
#formula to find index of box in boxes array: X + Y/3
def test_solve_box2(X, Y):
    #calculating index of box in boxes array based on formula ID = X + Y/3
    ID = X + (Y/3)
    b = boxes[ID]
    #i is the number we are trying to solve for in each row
    for i in range(9):
        #updating unfilled array
        b.update_unfilled()
        b.update_contents()
        #print "Here is the needs array", c.needs
        print
        #print "Row ", ID, ": ", r.contents
        #print c.filled()
        #only continue if row is unfilled and if the row needs that number
        if b.filled() == False and b.needs[i] == 1:
            #going through each square in collumn to see if it could possibly hold value i
            #add all the squares possible to an array called possies
            #if the length of that array is 1, then the square in the array have value i
            possies = []
            #variable to keep track of length of possies; will be incremented each time square is added to array
            #if plen > 1; break out of loop because cannot determine value
            print
            print "Test for ", i + 1
            print
            plen = 0
            #need nested for loops to iterate through box
            for j in range(3):
                for k in range(3):
                    #if more than one square in possies array, break out of loop
                    if plen > 1:
                        print "breaking out of loop"
                        break
                    s = Square(X + j, Y + k)
                    s.update_possibles()
                    if s.possibles[i] == 1:
                        print
                        print "Appending ", s.row, ", ", s.collumn, "for value ", i + 1
                        print
                        possies.append(s)
                        plen += 1
            if plen == 1:
                #s.value = possies[0]
                #updating left field for collumn to see if it is filled
                #c.left -= 1
                e = grid[possies[0].row]
                e[possies[0].collumn] = i + 1
                print "plen is 1 and value is ", i
            




#takes input box X and Y coordinates, which finds the box from boxes array
#formula to find index of box in boxes array: X + Y/3
def test_solve_box(ID):
    #initializing X and Y values (they will change later)
    X = 0
    Y = 0
    if ID < 3:
        X = 0
        Y = ID * 3
    elif ID < 6 and ID >= 3:
        X = 3
        Y = (ID % 3) * 3
    else:
        X = 6
        Y = (ID % 3) * 3
    #calculating index of box in boxes array based on formula ID = X + Y/3
    #ID = X + (Y/3)
    print "X = ", X
    print "Y = ", Y
    b = boxes[ID]
    #i is the number we are trying to solve for in each row
    for i in range(9):
        #updating unfilled array
        b.update_unfilled()
        b.update_contents()
        #print "Here is the needs array", c.needs
        print
        print "Box needs", b.needs
        print
        #print "Row ", ID, ": ", r.contents
        #print c.filled()
        #only continue if row is unfilled and if the row needs that number
        if b.filled() == False and b.needs[i] == 1:
            #going through each square in collumn to see if it could possibly hold value i
            #add all the squares possible to an array called possies
            #if the length of that array is 1, then the square in the array have value i
            possies = []
            #variable to keep track of length of possies; will be incremented each time square is added to array
            #if plen > 1; break out of loop because cannot determine value
            print
            print "Test for ", i + 1
            print
            plen = 0
            #need nested for loops to iterate through box
            for j in range(3):
                for k in range(3):
                    #if more than one square in possies array, break out of loop
                    if plen > 1:
                        print "breaking out of loop"
                        break
                    s = Square(X + j, Y + k)
                    s.update_possibles()
                    if s.possibles[i] == 1:
                        print
                        print "Appending ", s.row, ", ", s.collumn, "for value ", i + 1
                        #print "Row is : ", rows[s.row]
                        print
                        possies.append(s)
                        plen += 1
            if plen == 1:
                #s.value = possies[0]
                #updating left field for collumn to see if it is filled
                #c.left -= 1
                e = grid[possies[0].row]
                e[possies[0].collumn] = i + 1
                print "plen is 1 and value is ", i
            




#function to see if grid is filled
def grid_filled():
    #variable to keep track of unfilled spaces
    uf = 81
    for r in grid:
        for i in range(9):
            if r[i] != '':
                uf -= 1
    print "unfilled squares = ", uf
    if uf > 0:
        return False
    else:
        return True
            




#function to solve the whole sudoku grid
###
#While the grid is unsolved, iterate through all rows, columns, and boxes to solve
#to start, I will have a timeout feature to make sure loop doesn't run forever
###
def solve_grid1():
    #importing time
    import time
    timeout = time.time() + 60
    while grid_filled() == False and time.time() < timeout:
        for i in range(9):
            test_solve_row(i)
            test_solve_row2(i)
            test_solve_collumn(i)
            test_solve_box(i)




#Testing all my functions
g = Grid()    
print_grid()
print
r = Row(0)
r.update_contents()
r.update_unfilled()
print r.contents
print r.needs
print r.unfilled
print r.left
print
c = Collumn(1)
c.update_unfilled()
c.update_contents()
print c.contents
print c.needs
print c.unfilled 
print
b = Box(0,6)
b.update_unfilled()
b.update_contents()
print b.contents
print b.needs
print b.unfilled  
print
print ("Testing square")
s = Square(7,1)
s.update_possibles()
print s.possibles
print
create_grid()
rows[5].update_contents();
print rows[5].contents
print
print "Testing solve_square for square 6,3"
s63 = Square(3, 6)
#print "Value of square (3,6) is ", s63.value
#s63.solve_square()
#print s63.possibles
print
test_solve_row(3)
print
print "Solving collumn"
print
test_solve_collumn(1)
#s41 = Square(4,1)
#s41.solve_square()
print
print "Solving row 6"
test_solve_row2(5)
print
print "Solving box 0, 0"
test_solve_box(0)
print
print "solving box 0, 6"
print
test_solve_box(6)
print
#print "Square has value ", s41.value
solve_grid1()
print
print_grid()
#print grid_filled()




