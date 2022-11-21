"""
This class is used to initialize the gui and contains functions that create the board and background.
"""

import pygame
import os

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


# screenwidth of personal laptop: 1536
# screenheight of personal laptop: 864

# when implementing new colors, we need to add the color files and configure create_background
COLOR_1 = (101, 69, 101)
COLOR_2 = (245, 245, 220)
red_color = (216, 134, 134)
yellow_color = (216, 215, 134)
check_color = (223, 175, 105)

# standard size is 100
BOARD_SQUARE_SIZE_X = int(screen.get_size()[1] / 9.6)
BOARD_SQUARE_SIZE_Y = int(screen.get_size()[1] / 9.6)

# initial values of (0, 0) is the top left corner of the screen
BOARD_INITIAL_X_VALUE = screen.get_size()[0] / 2 - BOARD_SQUARE_SIZE_X*4
BOARD_INITIAL_Y_VALUE = screen.get_size()[1] / 2 - BOARD_SQUARE_SIZE_Y*4

# list containing the current locations of all of the chess pieces --> [[piece name, location]]
piecePositionList = []

# list of moves that are valid
possible_moves = []

# the piece that is currently selected
highlight_square = []

king_check_position = []  # used to change the color of the king when it is in check


# exit button location -- top right of screen
exit_button_location = [
    screen.get_size()[0] - 75, 0, screen.get_size()[0], 50]


def create_piece_image(address, sizex, sizey):
    """
    Creates an images to be displayed on the window

    Args:
        raddress: consists of the following format r"file_location"
        sizex (int): desired x size of the image
        sizey (int): desired y size of the image

    Returns:
        image: returns an image to be printed on the display
    """
    image = pygame.image.load(os.path.join(
        'Chess Pictures', address))
    image = pygame.transform.scale(image, (sizex, sizey))
    return image


def create_background():
    """
    Constructs the chess board and background objects
    """

    screen.fill((0, 0, 0))  # resets screen to black background

    square_position = ""
    color1 = COLOR_1
    color2 = COLOR_2

    for col in range(8):
        for row in range(8):
            if row == 0:
                square_position += "A"
            if row == 1:
                square_position += "B"
            if row == 2:
                square_position += "C"
            if row == 3:
                square_position += "D"
            if row == 4:
                square_position += "E"
            if row == 5:
                square_position += "F"
            if row == 6:
                square_position += "G"
            if row == 7:
                square_position += "H"

            if col == 0:
                square_position += "8"
            if col == 1:
                square_position += "7"
            if col == 2:
                square_position += "6"
            if col == 3:
                square_position += "5"
            if col == 4:
                square_position += "4"
            if col == 5:
                square_position += "3"
            if col == 6:
                square_position += "2"
            if col == 7:
                square_position += "1"

            if square_position in highlight_square:  # yellow color for square about to be moved
                pygame.draw.rect(screen, yellow_color,
                                 pygame.Rect(row*BOARD_SQUARE_SIZE_X + BOARD_INITIAL_X_VALUE,
                                             col*BOARD_SQUARE_SIZE_Y + BOARD_INITIAL_Y_VALUE,
                                             BOARD_SQUARE_SIZE_X,
                                             BOARD_SQUARE_SIZE_Y))

            elif square_position in king_check_position:  # orange color for king in check
                pygame.draw.rect(screen, check_color,
                                 pygame.Rect(row*BOARD_SQUARE_SIZE_X + BOARD_INITIAL_X_VALUE,
                                             col*BOARD_SQUARE_SIZE_Y + BOARD_INITIAL_Y_VALUE,
                                             BOARD_SQUARE_SIZE_X,
                                             BOARD_SQUARE_SIZE_Y))

            elif (row % 2 == 0 and col % 2 != 0) or (row % 2 != 0 and col % 2 == 0):
                if square_position in possible_moves:
                    # draw red square if in possible_moves
                    pygame.draw.rect(screen, red_color,
                                     pygame.Rect(row*BOARD_SQUARE_SIZE_X + BOARD_INITIAL_X_VALUE,
                                                 col*BOARD_SQUARE_SIZE_Y + BOARD_INITIAL_Y_VALUE,
                                                 BOARD_SQUARE_SIZE_X,
                                                 BOARD_SQUARE_SIZE_Y))

                # rect --> (init x, init y, x_size, y_size)
                else:
                    # draw normal sqare
                    pygame.draw.rect(screen, color1,
                                     pygame.Rect(row*BOARD_SQUARE_SIZE_X + BOARD_INITIAL_X_VALUE,
                                                 col*BOARD_SQUARE_SIZE_Y + BOARD_INITIAL_Y_VALUE,
                                                 BOARD_SQUARE_SIZE_X,
                                                 BOARD_SQUARE_SIZE_Y))
            else:
                if square_position in possible_moves:
                    # draw red square if in possible_moves
                    pygame.draw.rect(screen, red_color,
                                     pygame.Rect(row*BOARD_SQUARE_SIZE_X + BOARD_INITIAL_X_VALUE,
                                                 col*BOARD_SQUARE_SIZE_Y + BOARD_INITIAL_Y_VALUE,
                                                 BOARD_SQUARE_SIZE_X,
                                                 BOARD_SQUARE_SIZE_Y))
                else:
                    # draw normal sqare
                    pygame.draw.rect(screen, color2,
                                     pygame.Rect(row*BOARD_SQUARE_SIZE_X + BOARD_INITIAL_X_VALUE,
                                                 col*BOARD_SQUARE_SIZE_Y + BOARD_INITIAL_Y_VALUE,
                                                 BOARD_SQUARE_SIZE_X,
                                                 BOARD_SQUARE_SIZE_Y))
            square_position = ""  # resets square_position for each iteration

    # exit button
    pygame.draw.rect(screen, (23, 79, 83),
                     pygame.Rect(exit_button_location[0], exit_button_location[1],
                                 exit_button_location[2] -
                                 exit_button_location[0],
                                 exit_button_location[3] - exit_button_location[1]))

    # text for exit button
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('Exit', True, (134, 211, 216))
    textRect = text.get_rect(center=((exit_button_location[2] -
                                      exit_button_location[0])/2 + exit_button_location[0], (exit_button_location[3] -
                                     exit_button_location[1])/2 + exit_button_location[1]))
    screen.blit(text, textRect)


def get_piece_position_x(position: str, initial_position=BOARD_INITIAL_X_VALUE,
                         square_size=BOARD_SQUARE_SIZE_X):
    """
    Used to determine the x coordinate (in pixels) given the position of the square

    Args:
        position (str): position of chess square (e.g. "A7")
        initial_position (int, optional): initial x position. Defaults to BOARD_INITIAL_X_VALUE.
        square_size (int, optional): size of x axis the squares. Defaults to BOARD_SQUARE_SIZE_X.

    Returns:
        int: y coordinate (in pixels)
    """

    position_x = {"A": 0*square_size + initial_position, "B": 1*square_size + initial_position,
                  "C": 2*square_size + initial_position, "D": 3*square_size + initial_position,
                  "E": 4*square_size + initial_position, "F": 5*square_size + initial_position,
                  "G": 6*square_size + initial_position, "H": 7*square_size + initial_position}
    if position[0] in position_x:
        return position_x[position[0]]
    else:
        print("Incorrect format for get_piece_position_x")
        return None


def get_piece_position_y(position: str, initial_position=BOARD_INITIAL_Y_VALUE,
                         square_size=BOARD_SQUARE_SIZE_Y):
    """
    Used to determine the y coordinate (in pixels) given the position of the square

    Args:
        position (str): position of chess square (e.g. "A7")
        initial_position (int, optional): initial y position. Defaults to BOARD_INITIAL_Y_VALUE.
        square_size (int, optional): size of y axis the squares. Defaults to BOARD_SQUARE_SIZE_Y.

    Returns:
        int: y coordinate (in pixels)
    """

    position_x = {"8": 0*square_size + initial_position, "7": 1*square_size + initial_position,
                  "6": 2*square_size + initial_position, "5": 3*square_size + initial_position,
                  "4": 4*square_size + initial_position, "3": 5*square_size + initial_position,
                  "2": 6*square_size + initial_position, "1": 7*square_size + initial_position}
    if position[1] in position_x:
        return position_x[position[1]]
    else:
        print("Incorrect format for get_piece_position_y")
        return None


def get_board_color(position: str):
    """
    Given the position and the board colors, this funciton will return the color of the square.

    Args:
        position (str): position of chess square (e.g. "A7")

    Returns:
        (str): returns the color of the square
    """
    if position in possible_moves:
        return "#D88686"
    color1squares = ["A1", "A3", "A5", "A7", "B2", "B4", "B6", "B8", "C1", "C3", "C5", "C7",
                     "D2", "D4", "D6", "D8", "E1", "E3", "E5", "E7", "F2", "F4", "F6", "F8",
                     "G1", "G3", "G5", "G7", "H2", "H4", "H6", "H8"]
    color2squares = ["A2", "A4", "A6", "A8", "B1", "B3", "B5", "B7", "C2", "C4", "C6", "C8",
                     "D1", "D3", "D5", "D7", "E2", "E4", "E6", "E8", "F1", "F3", "F5", "F7",
                     "G2", "G4", "G6", "G8", "H1", "H3", "H5", "H7"]
    if position in color1squares:
        return COLOR_1
    elif position in color2squares:
        return COLOR_2
    else:
        print("Incorrect format for square name")
        return None


def pointer_on_exit():
    """
    Determines if the mouse pointer is within the exit button

    Returns:
        True if pointer is on exit and returns False if not
    """
    if pygame.mouse.get_pos()[0] >= exit_button_location[0] and \
            pygame.mouse.get_pos()[1] <= exit_button_location[3]:
        if pygame.mouse.get_pos()[0] <= exit_button_location[2] and \
                pygame.mouse.get_pos()[1] >= exit_button_location[1]:
            return True
    return False
