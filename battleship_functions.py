# Use these constants in your code 

MIN_SHIP_SIZE = 1
MAX_SHIP_SIZE = 10
MAX_GRID_SIZE = 10
UNKNOWN = '-'
EMPTY = '.'
HIT = 'X'
MISS = 'M'


def read_ship_data(game_file):

    """ (file open for reading) -> list of list of objects

    Return a list containing the ship characters in game_file as a list 
    of strings at index 0, and ship sizes in game_file as a list of ints 
    at index 1.

    """
    #delet "\n" at the end of the line
    ship_character_list = game_file.readline().strip('\n')
    ship_size_list = game_file.readline().strip('\n')
    
    #split the line by space
    ship_character_list = ship_character_list.split(' ')
    ship_size_list = ship_size_list.split(' ')
    
    #get the length of ship_size_list
    length = len(ship_size_list)
    
    #change the type of every element in ship_size_list to int
    for i in range(0, length):
        ship_size_list[i] = int(ship_size_list[i])
        
    return [ship_character_list, ship_size_list]


    # complete the function body for read_ship_data here
# Write the rest of the required functions here
# Don't forget to follow the Function Design Recipe



def has_ship(grid, row_index, column_index, character, size):

    """list of list of str, int, int, str, int) -> bool

    Return True iff the ship appears with the correct size, completely 
    in a row or a completely in a column at the given starting 
    cell(row_index, column_index).

    >>> grid = [['a','a','a'],['.','a','.'],['.','a','.']]
    >>> has_ship(grid, 0, 1, 'a', 3)
    True
    >>> grid = [['a','.','a'],['.','a','.'],['a','a','a']]
    >>> has_ship(grid, 0, 0, 'a', 3)
    False

    """
    number_of_row = len(grid)
    number_of_column = len(grid[0])

    #suppose there is no ship satisfied the condition
    find_ship = False

    #the number of contionous cell on right side
    continous_number_right_side = 0

    #first we can check the right side of the starting point
    #check the cell on the right of the cell
    #if the number of continous equals to the ship size
    #then we find a ship
    #if the element is not the character, then the continous number must reset.
    for i in range(column_index, number_of_column):
        if grid[row_index][i] == character:
            continous_number_right_side += 1
            if (continous_number_right_side == size):
                find_ship = True
        else:
            continous_number_right_side = 0
    
    #now we should check the bottom of the starting point
    #the rest part is similar to the part above
    continous_number_bottom_side = 0
    for i in range(row_index, number_of_row):
        if grid[i][column_index] == character:
            continous_number_bottom_side += 1
            if (continous_number_bottom_side == size):
                    find_ship = True
        else:
            continous_number_bottom_side = 0
    
    return find_ship




def validate_character_count(grid, ship_character_list, ship_size_list):

    """(list of list of str, list of str, list of int) -> bool

    Return True iff the grid contains the correct number of ship 
    characters for each ship in ship_character_list, equal to the corresponding
    number in ship_size_list, and the correct number of '.' in the grid

    >>> grid = [['a','.','.'],['b','a','.'],['b','a','.']]
    >>> validate_character_count(grid, ['a'], [3])
    False
    >>> grid = [['a','b','.'],['b','a','.'],['.','a','b']]
    >>> validate_character_count(grid, ['a', 'b'], [3, 3])
    True

    """
    number_of_row = len(grid)
    number_of_column = len(grid[0])
    #use to count the number of '.'
    number_of_empty = 0
    
    for ship_character in ship_character_list:
        #initial the count_ship_character to count the 
        #occurance of that character in the whole grid
        count_ship_character = 0
        for i_row in range(0, number_of_row):
            for i_column in range(0, number_of_column):
                if grid[i_row][i_column] == ship_character:
                    count_ship_character += 1
                if grid[i_row][i_column] == EMPTY:
                    number_of_empty += 1

        ship_character_index = ship_character_list.index(ship_character)

        #if count_ship_character doee not equal to the corresponding number
        #in ship_size_list
        #then the function should return False
        if count_ship_character != ship_size_list[ship_character_index]:
            return False


    grid_size = number_of_row * number_of_column
    #the count of number_of_empty was repeated many times
    #(length of ship_character_list)
    number_of_empty = number_of_empty / len(ship_character_list)
    total_ship_size = sum(ship_size_list)

    #check whether the number of '.' is corect or not, it should be 
    #the size of grid minus the total ship size
    return (grid_size == (total_ship_size + number_of_empty))



def validate_ship_positions(grid, ship_character_list, ship_size_list):

    """(list of list of str, list of str, list of int) -> bool

    Return True iff the grid contains each ship in ship_character_list
    aligned completely in a row or column. Check that each ship is contained
    completely in consecutive cells all in the same row, or all in the same 
    column, depending on if it is oriented horizontally or vertically and
    the ship size should be correct.

    >>> grid = [['a','d','.'],['a','d','.'],['.','d','a']]
    >>> validate_ship_positions(grid, ['a', 'd'], [3, 3])
    False
    >>> grid = [['a','d','.'],['a','d','.'],['a','d','a']]
    >>> validate_ship_positions(grid, ['a', 'd'], [3, 3])
    True

    """
    number_of_row = len(grid)
    number_of_column = len(grid[0])

    #all the ship character must satisfied the requirement
    for ship_character in ship_character_list:
        #use finish to check whether we found a ship or not
        find = False
        for i_row in range(0, number_of_row):
            for i_column in range(0, number_of_column):
                if grid[i_row][i_column] == ship_character:
                    ship_size = ship_size_list[ship_character_list.index(ship_character)]
                    if has_ship(grid, i_row, i_column, ship_character, ship_size):
                        find = True
        #if there is no ship satisfied the requirement, return False
        if not find:
            return False
    #if all the condition is true, then return True
    return True





def validate_fleet_grid(grid, ship_character_list, ship_size_list):

    """(list of list of str, list of str, list of int) -> bool

    Return True iff the potential fleet grid is a valid fleet grid
    the grid contains the correct number of ship characters for each ship 
    in ship_character_list, equal to the corresponding number in 
    ship_size_list, and the correct number of '.' in the grid and all the
    ship's position should be valid

    >>> grid = [['.','.','a'],['.','a','.'],['.','a','.']]
    >>> validate_fleet_grid(grid, ['a'], [3])
    False
    >>> grid = [['a','.','.'],['a','.','.'],['.','.','.']]
    >>> validate_fleet_grid(grid, ['a'], [2])
    True
    >>> grid = [['a','b','.'],['a','.','.'],['.','.','.']]
    >>> validate_fleet_grid(grid, ['a'], [2])
    False
    >>> grid = [['a','b','.'],['a','.','.'],['.','.','.']]
    >>> validate_fleet_grid(grid, ['a', 'b'], [2, 1])
    True

    """
    #we need to check whether it satisfied both validate_character_count()
    #and validate_ship_positions()
    return (validate_character_count(grid, ship_character_list, \
        ship_size_list)) and (validate_ship_positions(grid, \
            ship_character_list, ship_size_list))
    
def valid_cell(row_index, column_index, grid_size):

    """(int, int, int) -> bool

    Return True iff the cell specified by the row and the 
    column(point(row_index, column_index)) is a valid cell 
    inside a square grid of that size.

    >>> valid_cell(1, 1, 4)
    True
    >>> valid_cell(3, 3, 6)
    True
    >>> valid_cell(6, 3, 6)
    False

    """
    #row_index and column index must less that the grid_size
    return (row_index < grid_size) and (column_index < grid_size) 

def is_not_given_char(row_index, column_index, grid, given_char):

    """(int, int, list of list of str, str) -> bool

    Return True iff the cell specified by the row and the 
    column(point(row_index, column_index)) does not equal to the given_char.

    >>> grid = [['a','b','.'],['.','b','.'],['c','a','.']]
    >>> is_not_given_char( 1, 1, grid, 'c')
    True
    >>> grid = [['a','a','.'],['b','a','.'],['c','a','.']]
    >>> is_not_given_char( 2, 0, grid, 'c')
    False

    """
    #if the cell specified by point(row_index, column_index) does not equal
    #to the given_char, return True. Otherwise, return False

    return (grid[row_index][column_index] != given_char)

def update_fleet_grid(row_index, column_index, grid, 
    ship_character_list, ship_size_list, hit_list):

    """(int, int, list of list of str, list of str, 
        list of int, list of int) -> NoneType

    Update the fleet grid by converting the ship character in the 
    point(row_index, column_index) to upper-case, and also the hit_list 
    to indicate that there has been a hit. 
    Call the function print_sunk_message() when the ship sunk.

    >>> grid = [['d','A','s'],['D','a','s'],['.','a','s']]
    >>> ship_character_list = ['a', 's', 'd']
    >>> ship_size_list = [3, 3, 2]
    >>> hit_list = [1, 0, 1]
    >>> update_fleet_grid( 0, 0, grid, ship_character_list, \
        ship_size_list, hit_list)
    The size 2 d ship has been sunk!
    >>> grid
    [['D', 'A', 's'], ['D', 'a', 's'], ['.', 'a', 's']]
    >>> hit_list
    [1, 0, 2]
    >>> update_fleet_grid( 1, 1, grid, ship_character_list, \
        ship_size_list, hit_list)
    >>> grid
    [['D', 'A', 's'], ['D', 'A', 's'], ['.', 'a', 's']]
    >>> hit_list
    [2, 0, 2]
    
    """

    #get the index of grid[row_index][column_index] in the ship_character_list
    #and the ship size
    index = ship_character_list.index(grid[row_index][column_index])
    ship_size = ship_size_list[index]

    #call .upper() to set the cell to upper case
    grid[row_index][column_index] = grid[row_index][column_index].upper()

    #plus one on the correspond value in the hit_list
    hit_list[index] += 1

    if ship_size == hit_list[index]:
        print_sunk_message(ship_size, grid[row_index][column_index].lower())


def update_target_grid(row_index, column_index, target_grid, fleet_grid):

    """(int, int, list of list of str, list of list of str) -> NoneType

    Set the element of the specified cellin the target grid 
    point(row_index, column_index) to HIT or MISS using the information from
    the corresponding cell in the fleet grid.

    >>> target_grid = [['-', 'X', '-'], ['X', '-', '-'], ['-', '-', '-']]
    >>> fleet_grid = [['B', 'A', 'c'], ['B', 'a', 'c'], ['.', 'a', 'c']]
    >>> update_target_grid(0, 0, target_grid, fleet_grid)
    >>> target_grid
    [['X', 'X', '-'], ['X', '-', '-'], ['-', '-', '-']]
    >>> update_target_grid(2, 0, target_grid, fleet_grid)
    >>> target_grid
    [['X', 'X', '-'], ['X', '-', '-'], ['M', '-', '-']]
    >>> update_target_grid(2, 1, target_grid, fleet_grid)
    >>> target_grid
    [['X', 'X', '-'], ['X', '-', '-'], ['M', 'M', '-']]

    """
    ship_character = fleet_grid[row_index][column_index]

    #if that ship_character is '.':
    if ship_character !=  EMPTY:

        #if ship_character is upper case, change the 
        #point in target_grid to 'X'
        #else, chenge to 'M'
        if ship_character.isupper():
            target_grid[row_index][column_index] = HIT
        else:
            target_grid[row_index][column_index] = MISS

    #if not empty, change the point in target_grid to 'M'
    else:
        target_grid[row_index][column_index] = MISS

def is_win(ship_size_list, hit_list):
    """(list of int, list of int) -> bool

    Return True iff the number of hits for each ship in the hits list
    is the same as the size of each ship 

    >>> ship_size = [2, 3, 4, 2]
    >>> hit_list = [2, 3, 4, 1]
    >>> is_win(ship_size, hit_list)
    False
    >>> ship_size = [2, 3, 4, 2]
    >>> hit_list = [2, 3, 4, 2]
    >>> is_win(ship_size, hit_list)
    True
    """
    #if ship_size_list == hit_list, then it means each element in 
    #ship_size_list equals to corresponding element in hit_list
    return ship_size_list == hit_list





##################################################
## Helper function to call in update_fleet_grid
## Do not change!
##################################################

def print_sunk_message(ship_size, ship_character):
    """ (int, str) -> NoneType
  
    Print a message telling player that a ship_size ship with ship_character
    has been sunk.
    """

    print('The size {0} {1} ship has been sunk!'.format(ship_size, ship_character))
    
    
if __name__ == '__main__':
    import doctest
   
    # uncomment the line below to run the docstring examples     
    doctest.testmod()

