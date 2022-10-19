"""
This class simulates a chess game. It is currently under development.
"""

import tkinter
from PIL import ImageTk, Image

# screenwidth of laptop: 1536
# print(gui.winfo_screenwidth())
# screenheight of laptop: 864
# print(gui.winfo_screenheight())

gui = tkinter.Tk()
gui.attributes('-fullscreen', True)
gui.title("Testing title")


COLOR_1 = "lightgreen"
COLOR_2 = "beige"

# standard size is 100
BOARD_SQUARE_SIZE_X = 100
BOARD_SQUARE_SIZE_Y = 100

# initial values of (0, 0) is the top left corner of the screen
BOARD_INITIAL_X_VALUE = 0
BOARD_INITIAL_Y_VALUE = 0

# list containing the current locations of all of the chess pieces --> [[piece name, location]]
piecePositionList = []


def create_image(raddress, background_color, sizex, sizey):
    """
    Creates an images to be displayed on the window

    Args:
        raddress: consists of the following format r"file_location"
        background_color (str): sets the background color of the image
        sizex (int): desired x size of the image
        sizey (int): desired y size of the image

    Returns:
        image: returns an image to be printed on the display
    """

    image = Image.open(raddress)
    image = image.resize((sizex, sizey))
    test = ImageTk.PhotoImage(image)
    label = tkinter.Label(image=test, borderwidth=0,
                          background=background_color)
    label.image = test
    return label


def create_board():
    """
    Constructs the chess board
    """

    # note: prints from top left down to bottom right
    for col in range(8):
        for row in range(8):
            if (row % 2 == 0 and col % 2 != 0) or (row % 2 != 0 and col % 2 == 0):
                boardcolor1 = create_image(
                    r"C:\Users\jilkd\OneDrive\Documents\Python\Chess Pictures\Colors\lightgreen.png",
                    COLOR_1, BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
                boardcolor1.place(x=row*BOARD_SQUARE_SIZE_X + BOARD_INITIAL_X_VALUE,
                                  y=col*BOARD_SQUARE_SIZE_Y + BOARD_INITIAL_Y_VALUE)
            else:
                boardcolor2 = create_image(
                    r"C:\Users\jilkd\OneDrive\Documents\Python\Chess Pictures\Colors\beige.png",
                    COLOR_2, BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
                boardcolor2.place(x=row*BOARD_SQUARE_SIZE_X + BOARD_INITIAL_X_VALUE,
                                  y=col*BOARD_SQUARE_SIZE_Y + BOARD_INITIAL_Y_VALUE)


def black_bishop(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    black_bishop_image = create_image(
        r"C:\Users\jilkd\OneDrive\Documents\Python\Chess Pictures\Pieces\black_bishop.png",
        get_board_color(position), BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    black_bishop_image.place(x=get_piece_position_x(position),
                             y=get_piece_position_y(position))


def black_king(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    black_king_image = create_image(
        r"C:\Users\jilkd\OneDrive\Documents\Python\Chess Pictures\Pieces\black_king.png",
        get_board_color(position), BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    black_king_image.place(x=get_piece_position_x(position),
                           y=get_piece_position_y(position))


def black_knight(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    black_knight_image = create_image(
        r"C:\Users\jilkd\OneDrive\Documents\Python\Chess Pictures\Pieces\black_knight.png",
        get_board_color(position), BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    black_knight_image.place(x=get_piece_position_x(position),
                             y=get_piece_position_y(position))


def black_pawn(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    black_pawn_image = create_image(
        r"C:\Users\jilkd\OneDrive\Documents\Python\Chess Pictures\Pieces\black_pawn.png",
        get_board_color(position), BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    black_pawn_image.place(x=get_piece_position_x(position),
                           y=get_piece_position_y(position))


def black_queen(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    black_queen_image = create_image(
        r"C:\Users\jilkd\OneDrive\Documents\Python\Chess Pictures\Pieces\black_queen.png",
        get_board_color(position), BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    black_queen_image.place(x=get_piece_position_x(position),
                            y=get_piece_position_y(position))


def black_rook(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    black_rook_image = create_image(
        r"C:\Users\jilkd\OneDrive\Documents\Python\Chess Pictures\Pieces\black_rook.png",
        get_board_color(position), BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    black_rook_image.place(x=get_piece_position_x(position),
                           y=get_piece_position_y(position))


def white_bishop(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    white_bishop_image = create_image(
        r"C:\Users\jilkd\OneDrive\Documents\Python\Chess Pictures\Pieces\white_bishop.png",
        get_board_color(position), BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    white_bishop_image.place(x=get_piece_position_x(position),
                             y=get_piece_position_y(position))


def white_king(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    white_king_image = create_image(
        r"C:\Users\jilkd\OneDrive\Documents\Python\Chess Pictures\Pieces\white_king.png",
        get_board_color(position), BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    white_king_image.place(x=get_piece_position_x(position),
                           y=get_piece_position_y(position))


def white_knight(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    white_knight_image = create_image(
        r"C:\Users\jilkd\OneDrive\Documents\Python\Chess Pictures\Pieces\white_knight.png",
        get_board_color(position), BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    white_knight_image.place(x=get_piece_position_x(position),
                             y=get_piece_position_y(position))


def white_pawn(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    white_pawn_image = create_image(
        r"C:\Users\jilkd\OneDrive\Documents\Python\Chess Pictures\Pieces\white_pawn.png",
        get_board_color(position), BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    white_pawn_image.place(x=get_piece_position_x(position),
                           y=get_piece_position_y(position))


def white_queen(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    white_queen_image = create_image(
        r"C:\Users\jilkd\OneDrive\Documents\Python\Chess Pictures\Pieces\white_queen.png",
        get_board_color(position), BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    white_queen_image.place(x=get_piece_position_x(position),
                            y=get_piece_position_y(position))


def white_rook(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    white_rook_image = create_image(
        r"C:\Users\jilkd\OneDrive\Documents\Python\Chess Pictures\Pieces\white_rook.png",
        get_board_color(position), BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    white_rook_image.place(x=get_piece_position_x(position),
                           y=get_piece_position_y(position))


def place_pieces(start_game=False):
    """
    If state_game = True, the all of the pieces will be placed on the board.
    If start_game = false, all of the pieces will be generated based on piecePositionList

    Args:
        start_game (bool, optional): true indicates that it is the start. Defaults to False.
    """

    if start_game:
        create_board()
        black_pawn("A7")
        piecePositionList.append(["black pawn", "A7"])
        black_pawn("B7")
        piecePositionList.append(["black pawn", "B7"])
        black_pawn("C7")
        piecePositionList.append(["black pawn", "C7"])
        black_pawn("D7")
        piecePositionList.append(["black pawn", "D7"])
        black_pawn("E7")
        piecePositionList.append(["black pawn", "E7"])
        black_pawn("F7")
        piecePositionList.append(["black pawn", "F7"])
        black_pawn("G7")
        piecePositionList.append(["black pawn", "G7"])
        black_pawn("H7")
        piecePositionList.append(["black pawn", "H7"])
        black_rook("A8")
        piecePositionList.append(["black rook", "A8"])
        black_knight("B8")
        piecePositionList.append(["black knight", "B8"])
        black_bishop("C8")
        piecePositionList.append(["black bishop", "C8"])
        black_queen("D8")
        piecePositionList.append(["black queen", "D8"])
        black_king("E8")
        piecePositionList.append(["black king", "E8"])
        black_bishop("F8")
        piecePositionList.append(["black bishop", "F8"])
        black_knight("G8")
        piecePositionList.append(["black knight", "G8"])
        black_rook("H8")
        piecePositionList.append(["black rook", "H8"])

        white_pawn("A2")
        piecePositionList.append(["white pawn", "A2"])
        white_pawn("B2")
        piecePositionList.append(["white pawn", "B2"])
        white_pawn("C2")
        piecePositionList.append(["white pawn", "C2"])
        white_pawn("D2")
        piecePositionList.append(["white pawn", "D2"])
        white_pawn("E2")
        piecePositionList.append(["white pawn", "E2"])
        white_pawn("F2")
        piecePositionList.append(["white pawn", "F2"])
        white_pawn("G2")
        piecePositionList.append(["white pawn", "G2"])
        white_pawn("H2")
        piecePositionList.append(["white pawn", "H2"])
        white_rook("A1")
        piecePositionList.append(["white rook", "A1"])
        white_knight("B1")
        piecePositionList.append(["white knight", "B1"])
        white_bishop("C1")
        piecePositionList.append(["white bishop", "C1"])
        white_queen("D1")
        piecePositionList.append(["white queen", "D1"])
        white_king("E1")
        piecePositionList.append(["white king", "E1"])
        white_bishop("F1")
        piecePositionList.append(["white bishop", "F1"])
        white_knight("G1")
        piecePositionList.append(["white knight", "G1"])
        white_rook("H1")
        piecePositionList.append(["white rook", "H1"])

    else:
        clear_frame()
        create_board()
        for piece_position in piecePositionList:
            if piece_position[0] == "black pawn":
                black_pawn(piece_position[1])
            if piece_position[0] == "black rook":
                black_rook(piece_position[1])
            if piece_position[0] == "black knight":
                black_knight(piece_position[1])
            if piece_position[0] == "black bishop":
                black_bishop(piece_position[1])
            if piece_position[0] == "black queen":
                black_queen(piece_position[1])
            if piece_position[0] == "black king":
                black_king(piece_position[1])

            if piece_position[0] == "white pawn":
                white_pawn(piece_position[1])
            if piece_position[0] == "white rook":
                white_rook(piece_position[1])
            if piece_position[0] == "white knight":
                white_knight(piece_position[1])
            if piece_position[0] == "white bishop":
                white_bishop(piece_position[1])
            if piece_position[0] == "white queen":
                white_queen(piece_position[1])
            if piece_position[0] == "white king":
                white_king(piece_position[1])


def move_piece(old_position: str, new_position: str):
    """
    Moves a piece and calls place_pieces to regenerate the board after

    Args:
        old_position (str): position of original chess square (e.g. "A7")
        new_position (str): position of new chess square (e.g. "A7")
    """

    for piece_position in piecePositionList:
        if old_position == piece_position[1]:
            piecePositionList.remove(piece_position)
            piecePositionList.append([piece_position[0], new_position])
    place_pieces()


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


def clear_frame():
    """
    Used to "clear" the board in between moves. In reality, it clears the entire window
    """

    for widgets in gui.winfo_children():
        widgets.destroy()


def main():
    """
    The main function that runs all of the code above
    """

    place_pieces(start_game=True)
    move_piece("C8", "C6")
    move_piece("D1", "C8")

    button = tkinter.Button(gui, text="Exit", width=10, command=gui.destroy)
    button.pack()
    gui.mainloop()


main()
