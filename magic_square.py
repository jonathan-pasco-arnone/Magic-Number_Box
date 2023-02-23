""" Generates all posible magic square combinations """
#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: February 2023

MAGIC_NUMBER = 15

def magic_square_generator(magic_square, digit):
    """ Generates all possible combinations of squares """
    # Checks if the square works, then prints it if it does

    if digit == 8:
        while(magic_square[8] != 9):
            if (square_checker(magic_square)):
                print_square(magic_square)
            magic_square[8] += 1
            print_square(magic_square)
    else:
        for index in range(0,8,1):
            if magic_square[digit + 1] == 9:
                magic_square[digit] += 1
                magic_square[digit + 1] = 0
            magic_square_generator(magic_square, digit + 1)

def print_square(magic_square):
    """ Prints the magic square in proper format """
    print("\n", magic_square[0], " ", magic_square[1], " ", magic_square[2], "\n\n",
          magic_square[3], " ", magic_square[4], " ", magic_square[5], "\n\n",
          magic_square[6], " ", magic_square[7], " ", magic_square[8], "\n")

def square_checker(magic_square):
    """ Checks if the magic square works """
    rows = False
    columns = False
    diagonals = False

    # Checks all rows
    if (magic_square[0] + magic_square[1] + magic_square[2] == MAGIC_NUMBER and
            magic_square[3] + magic_square[4] + magic_square[5] == MAGIC_NUMBER and
            magic_square[6] + magic_square[7] + magic_square[8] == MAGIC_NUMBER):

        rows = True

    # Checks all columns
    if (magic_square[0] + magic_square[3] + magic_square[6] == MAGIC_NUMBER and
            magic_square[1] + magic_square[4] + magic_square[7] == MAGIC_NUMBER and
            magic_square[2] + magic_square[5] + magic_square[8] == MAGIC_NUMBER):

        columns = True

    # Checks both diagonals
    if (magic_square[0] + magic_square[4] + magic_square[8] == MAGIC_NUMBER and
            magic_square[2] + magic_square[4] + magic_square[6] == MAGIC_NUMBER):

        diagonals = True

    return rows and columns and diagonals

magic_square_generator([0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
