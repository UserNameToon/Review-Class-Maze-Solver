"""*****************************************************************************
Name:    Chanchatri Chaichanathong
course:  CMPT 200 X03L
purpose: Review Class
ID:      3056450
*****************************************************************************"""

#q1
# Purpose: this method sum the interger from the user input
# Parameters: sInput: string or int
# Return: the sum of the input
def sum_of_int(sInput):
    #convert to string
    intStr = str(sInput)
    if len(intStr) <= 1:
        return int(intStr)
    return int(intStr[0]) + sum_of_int(intStr[1::])

#q2
# Purpose: this method call a helper method 
# Parameters: aList: list of interger
# Return: the result of the helper fuction
def find_max(aList):
    return rec_find_max(aList,0,len(aList)-1)

# Purpose: this method find the maximum interger in a list
# Parameters: aList: list of int
#             start: start position from index 0 toward the end 
#             end  : start position from the end toward index 0
# Return: the maximum interger in the list
def rec_find_max(aList,start,end):
    if start == end :    #end condition
        return aList[start]
    #retrun maximum at start or end depending on which is bigger
    return rec_find_max(aList,start +1 ,end) if aList[start] < aList[end] else rec_find_max(aList,start,end - 1)            

#q3 
'''
This is a MazeSolver class that is used by main() to solve the maze extracted
by user txt file. the class store the maze in a form of string, its also store 
2 tuples acting as a start position coordinate and end position coordinate.
the maze's actual boundary is hight of the boudary * 2 +1 and the width of the 
boudary * 2 + 1, thus when determind the starting and the ending position need to
account for the extra char acting as the outliner. the maze solver imprement backtracking
and recursion to solve the maze. 
'''
class MazeSolver: 
    # Purpose: this method initialize the obj
    # Parameters: maze: string representing the maze
    #             start: start position of the maze
    #             end  : end position of the maze
    # Return: None   
    def __init__(self, maze,start,end):
        self._maze = maze
        self._start = start
        self._end = end
        self._move = [] 
        self._mazeList = []
        
        #convert the str to a list for writing the solution 
        for i in self._maze:
            temp = []
            for j in i:
                temp.append(j)
            self._mazeList.append(temp) 
        #solve the maze upon calling the instance   
        self.solve(self._start)
        
    # Purpose: this method return the string representing the solution 
    # Parameters: None 
    # Return: the maximum interger in the list        
    def __repr__(self):
        s = ''
        #return no solution if the maze can't be solve
        if len(self._move) == 0:
            return 'No solution'
        #return the solution
        else:
            for i in self._mazeList:
                s += '\n'+''.join(i)                 
            return str(s)
        
    # Purpose: this method solve the maze using recursion and backtracking
    # Parameters: coor: coordinate of the current move
    # Return: validation of the move    
    def solve(self,coor):
        #change the coordinate parameter to x,y for ease of use since coor 
        #is a turple
        x,y = coor[0],coor[1] 
        
        #compare coor to the end, if found, replace the spot with 'F' to show 
        #the end on the maze, since the end spot is a valide move, return true 
        if coor == self._end:
            #self._mazeList[x][y] = ''
            return True
        #return false if hiting walls or mark spot
        if self._mazeList[x][y] in '|-+*':
            return False
        #return false if move list is empty (checking for cycling)
        if len(self._move) == 0 and coor != self._start :
            return False
        #print(coor)
        
        #mark current spot
        self._mazeList[x][y] = '*'
        #add current spot to move List
        self._move.append((x,y))
        
        #check up
        if self.solve((x -1, y)): return True
        #check Down
        if self.solve((x +1, y)): return True           
        #check left
        if self.solve((x, y -1)): return True
        #check right 
        if self.solve((x, y +1)): return True        
        
        #remove mark if path is invalide
        self._mazeList[x][y] = ' '
        #remove move from the list
        self._move.remove((x,y))
        #return false if there is no valide path
        return False
    
# Purpose: this method ask user for the input of the file name and create a solver 
# instance using MazeSolver class
# Parameters: none
# thrown: inform user of invalide input
# Return: solution of the input maze
def main():
    #loop if user input is invalide
    while True:
        try:
            userInput = input('Enter file name: ')
            mazeFile = open_file(userInput)
            break
        #alert user if the input is invalid
        except: print('Invalid inpunt!')
    #maze = open_file('maze510.txt')
    
    #create MazeSolver instance
    mazeObj = MazeSolver(mazeFile[0],mazeFile[1],mazeFile[2])
    print(mazeObj)
    
# Purpose: this method test all the maze file
# Parameters: none
# Return: show the solution of each maze
def test():
    #list of all the maze file
    listOfMaze = ['maze510.txt','maze510cycles.txt', 'maze510island.txt',
                  'maze510islandnosoln.txt','maze510nosoln.txt','maze1020.txt',
                  'maze50100.txt']
    #show file name + solution
    for i in listOfMaze:
        maze = open_file(i)
        #create mazesolver instance
        testMaze = MazeSolver(maze[0],maze[1],maze[2])
        #print solution for each one + their file name 
        print('\n'+ i + ' : ', testMaze)   
        
# Purpose: this method open file from the userinput
# Parameters: fileName: string - userinput 
# Return: list of list contain maze, the start position, the end position 
def open_file(fileName):
    listMaze = []
    #read file
    inFile = open(fileName,'r')
    for i in inFile:
        #append file obj in a list
        listMaze.append(i.strip()) #striping the '\n'
    #boundary of each maze
    boundary = listMaze[0].split()
    #determind the start and the end
    start = ((int(boundary[0])*2 )-1, 1)
    end = (1,(int(boundary[1])*2 )-1)
    #return list of [maze, start, end]
    return [listMaze[3:], start,end]
main()