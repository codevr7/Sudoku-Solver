# Solves a nine by nine sudoku grid 
def sudoku_solver(ls):
    # The first empty row and collumn of the grid
    row,coll = next_empty(ls)   
    if row is None: return ls  # If there is no empty cell then sudoku grid is full
    for pos_val in range(1,10):  #   
        if is_valid(ls,row,coll,pos_val):
            ls[row][coll] = pos_val
            if sudoku_solver(ls):
                return ls
        ls[row][coll] = 0
    return False

# Checks whether a value is possible on sudoku grid
def is_valid(ls,row,coll,val):
    # Checks whether value possible on row
    if val in ls[row]:
        return False
    # Checks whether value is possible on collumn
    curr = 0
    for i in ls:
        if val == ls[curr][coll]:
            return False
        curr += 1
    # Check whether value is in box
    x = (row // 3) * 3
    y = (coll // 3) * 3
    for i in range(x,x + 3):
        for j in range(y,y + 3):
            if ls[i][j] == val:
                return False
    return True

# Finds next empty cell in sudoku grid
def next_empty(ls):
    for i in range(9):
        for j in range(9):
            if ls[i][j] == 0:
                return i,j
    return None,None

def line(ls):
    STR = []
    if isinstance(ls,list) == False:
        return ls
    for i in ls:
        print(i,end = '\n')
    return True

if __name__ == '__main__':
    inp = [[0,0,6,0,0,0,0,2,0],
           [0,0,1,0,0,0,0,6,9],
           [5,7,4,0,0,0,0,0,0],
           [8,0,0,6,0,0,0,0,0],
           [0,0,0,0,9,0,8,3,0],
           [0,5,0,0,1,0,0,0,0],
           [0,0,0,0,0,0,0,0,7],
           [1,0,0,0,0,5,0,0,4],
           [0,0,0,7,0,4,6,0,0]]
    print(line(sudoku_solver(inp)))
