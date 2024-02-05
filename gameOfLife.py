import time
import numpy as np

GRID_HEIGHT = 40
GRID_WIDTH = 40
GEN_DURATION = 5 #seconds

gameGrid = np.random.choice([0,1],(GRID_HEIGHT,GRID_WIDTH))
temp_gameGrid = np.zeros((GRID_HEIGHT,GRID_WIDTH), dtype=int)

"""gameGrid =     [[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],]

temp_gameGrid = [[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],]"""

def live_neighbours(cell_coordinates):   #counts alive neighbours of a cell
    cell_row, cell_column = cell_coordinates
    neighbours_alive = 0
    
    for neighbour_relative_height in range(-1,2,1):
        for neighbour_relative_width in range(-1,2,1):
            
            neighbour_row = cell_row + neighbour_relative_height
            neighbour_column = cell_column + neighbour_relative_width
            
            if neighbour_row not in range(0, GRID_HEIGHT) or neighbour_column not in range(0, GRID_WIDTH) or (neighbour_relative_height == 0 and neighbour_relative_width == 0): #eliminates counting itself as a neighbour of itself
                continue
            else:
                if gameGrid[neighbour_row][neighbour_column] == 1:
                    neighbours_alive += 1

    return neighbours_alive


def cell_cycle(cell_coordinates): #decides death or live of a cell
    cell_row, cell_column = cell_coordinates
    cell = gameGrid[cell_row][cell_column]   
    neighbours_alive = live_neighbours(cell_coordinates)
    
    if cell == 1:
        if neighbours_alive < 2 or neighbours_alive > 3:
            #cell dies
            temp_gameGrid[cell_row][cell_column] = 0
        elif 2 <= neighbours_alive <= 3:
            # cell lives
            temp_gameGrid[cell_row][cell_column] = 1
    elif cell == 0:
        if neighbours_alive == 3:
            #cell comes alive
            temp_gameGrid[cell_row][cell_column] = 1
        else:
            temp_gameGrid[cell_row][cell_column] = 0


#game loop
gen = 0
while True:   
    #input() #for manual iteration
    print("Generation:", gen)
    gen += 1

    for row in range(GRID_HEIGHT):
        for column in range(GRID_WIDTH):
            print(gameGrid[row][column],end=" ")
            cell_cycle((row, column))
        print()
    print("- "*GRID_WIDTH)

    gameGrid = [row[:] for row in temp_gameGrid]

    time.sleep(GEN_DURATION)

