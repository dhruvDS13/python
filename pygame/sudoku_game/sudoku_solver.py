import numpy as np
puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

'''Below puzzle is not executed'''
# puzzle = [[0, 0, 3, 0, 2, 0, 6, 0, 0],
#           [9, 0, 0, 3, 0, 5, 0, 0, 1],
#           [0, 0, 1, 8, 0, 6, 4, 0, 0],
#           [0, 0, 8, 1, 0, 2, 0, 0, 4],
#           [0, 0, 0, 0, 5, 0, 0, 0, 0],
#           [5, 0, 0, 0, 0, 3, 1, 0, 0],
#           [0, 0, 7, 0, 0, 1, 0, 0, 0],
#           [2, 0, 0, 5, 0, 4, 0, 0, 3],
#           [0, 0, 6, 0, 1, 0, 9, 0, 0]]
 
print(np.matrix(puzzle))
# Function to check if a number is possible in the given position
def possible(y,x,n):
    global puzzle

    # Check the row
    for i in range(0,9):
        if puzzle[y][i] == n:
            return False
        
    # Check the column
    for i in range(0,9):
        if puzzle[i][x] == n:
            return False
    
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if puzzle[y0+i][x0+j] ==n:
                return False
    return True

# Function to solve the Sudoku puzzle using recursion and backtracking
def solve():
    global puzzle
    for y in range(9):
        for x in range(9):
            if puzzle[y][x] == 0:
                for n in range(1,10):
                    if possible(y, x, n):
                        puzzle[y][x] = n
                        
                        if solve():
                            return True
                        puzzle[y][x] = 0
                return False
            
    return True
    
if solve():
    print('\nSolved Puzzel:')
    print(np.matrix(puzzle))
else:
    print("No solution exists")
