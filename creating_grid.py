grid=[]

#print(grid.append([3,0,6,5,0,8,4,0,0]), '\n',
#grid.append([5,2,0,0,0,0,0,0,0]),
#grid.append([0,8,7,0,0,0,0,3,1]),
#grid.append([0,0,3,0,1,0,0,8,0]),
#grid.append([9,0,0,8,6,3,0,0,5]),
#grid.append([0,5,0,0,9,0,6,0,0]),
#grid.append([1,3,0,0,0,0,2,5,0]),
#grid.append([0,0,0,0,0,0,0,7,4]),
#grid.append([0,0,5,2,0,6,3,0,0]))

def create_grid(grid):
    for i in range(9):
        for j in range(9):
            print (grid[i][j])
def find_empty_location(grid,l): 
    for row in range(9): 
        for col in range(9): 
            if(grid[row][col]==0):
                l[0]=row 
                l[1]=col 
                return True
    return False 

def used_in_row(grid,row,num): 
    for i in range(9): 
        if(grid[row][i] == num): 
            return True
    return False
def used_in_col(grid,col,num): 
    for i in range(9): 
        if(grid[i][col] == num): 
            return True
    return False
  
# Returns a boolean which indicates whether any assigned entry 
# within the specified 3x3 box matches the given number 
def used_in_box(grid,row,col,num): 
    for i in range(3): 
        for j in range(3): 
            if(grid[i+row][j+col] == num): 
                return True
def check_location_is_safe(grid,row,col,num): 
    return not used_in_row(grid,row,num) and not used_in_col(grid,col,num) and not used_in_box(grid,row - row%3,col - col%3,num) 
def solve_sudoku(grid): 
      
    # 'l' is a list variable that keeps the record of row and col in find_empty_location Function     
    l=[0,0] 
      
    # If there is no unassigned location, we are done     
    if(not find_empty_location(grid,l)): 
        return True
      
    # Assigning list values to row and col that we got from the above Function  
    row=l[0] 
    col=l[1] 
      
    # consider digits 1 to 9 
    for num in range(1,10): 
          
        # if looks promising 
        if(check_location_is_safe(grid,row,col,num)): 
              
            # make tentative assignment 
            grid[row][col]=num 
  
            # return, if success, ya! 
            if(solve_sudoku(grid)): 
                return True
  
            # failure, unmake & try again 
            grid[row][col] = 0
              
    # this triggers backtracking         
    return False 

if __name__=="__main__": 
      
    # creating a 2D array for the grid 
    grid=[[0 for x in range(9)]for y in range(9)]

    #grid1=[[3,0,6,5,0,8,4,0,0], 
          #[5,2,0,0,0,0,0,0,0], 
          #[0,8,7,0,0,0,0,3,1], 
          #[0,0,3,0,1,0,0,8,0], 
          #[9,0,0,8,6,3,0,0,5], 
          #[0,5,0,0,9,0,6,0,0], 
          #[1,3,0,0,0,0,2,5,0], 
          #[0,0,0,0,0,0,0,7,4], 
          #[0,0,5,2,0,6,3,0,0]] 
      

    if(solve_sudoku(grid)): 
        create_grid(grid) 
    else: 
        print ("No solution exists")        