from inspect import BoundArguments

from skelot import Createboard


EMPTY = "." 
BoardDimension = 5
def CreateBoard(BoardDimension): 
    Board = [] 
    for Row in range(BoardDimension): 
        Board.append([]) 
    for Column in range(BoardDimension): 
        Board[Row].append(EMPTY) 
    return Board 

value = Createboard(BoardDimension)
print(value)
