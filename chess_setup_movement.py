"""
This class contains helper functions such as placing pieces on the board and moving pieces around the board.
"""

from chess_pieces import *

# list of all pawns that moved two squares and could potentially be taken via en passant
en_passant_list = []


def place_pieces(start_game=False):
    """
    If state_game = True, the all of the pieces will be placed on the board.
    If start_game = false, all of the pieces will be generated based on piecePositionList

    Args:
        start_game (bool, optional): true indicates that it is the start. Defaults to False.
    """

    if start_game:
        create_background()
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
        create_background()
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

    pygame.display.update()


def check_en_passant(old_position, new_position):
    """
    Adds pieces to en_passant_list if it is a possible en passant move

    Args:
        old_position (str): position of original chess square (e.g. "A7")
        new_position (str): position of new chess square (e.g. "A7")
    """
    if old_position == old_position[0] + "7" and new_position == old_position[0] + "5":
        for piece_position in piecePositionList:
            if piece_position[1] == old_position and piece_position[0][6:] == "pawn":
                en_passant_list.append(
                    [piece_position[0], piece_position[1][0] + str(int(piece_position[1][1]) - 2)])
    if old_position == old_position[0] + "2" and new_position == old_position[0] + "4":
        for piece_position in piecePositionList:
            if piece_position[1] == old_position and piece_position[0][6:] == "pawn":
                en_passant_list.append(
                    [piece_position[0], piece_position[1][0] + str(int(piece_position[1][1]) + 2)])


def move_piece(old_position: str, new_position: str):
    """
    Moves a piece and calls place_pieces to regenerate the board after

    Args:
        old_position (str): position of original chess square (e.g. "A7")
        new_position (str): position of new chess square (e.g. "A7")
    """
    remove_en_passant = False  # wait two moves before removing the option to en passant
    if len(en_passant_list) != 0:
        remove_en_passant = True

    check_en_passant(old_position, new_position)

    for piece_position in piecePositionList:  # removes piece if piece is being taken
        if new_position == piece_position[1]:
            piecePositionList.remove(piece_position)

        # remove en passant piece
        if len(en_passant_list) != 0:
            if piece_position[1] == en_passant_list[-1][1] and \
                (old_position[0] == chr(ord(new_position[0]) + 1)
                    or old_position[0] == chr(ord(new_position[0]) - 1)) \
                    and piece_position[0][6:] == "pawn" and (new_position[1] == "6" or new_position[1] == "3"):
                piecePositionList.remove(piece_position)

    # moves the piece in piecePositionList (i.e. [[black pawn, A7]])
    for piece_position in piecePositionList:
        if old_position == piece_position[1]:
            piecePositionList.remove(piece_position)
            piecePositionList.append([piece_position[0], new_position])

    if remove_en_passant:
        # removes the possible en passant move from the list after 2 moves
        en_passant_list.pop(0)
    place_pieces()


def pointer_on_square():
    """
    Checks if the mouse is on one of the chess board squares

    Returns:
        "" if not on a square
        position of square like "A7" if pointer is on square
    """
    square = ""

    for i in range(8):
        for j in range(8):
            if pygame.mouse.get_pos()[0] > BOARD_INITIAL_X_VALUE + BOARD_SQUARE_SIZE_X*i and \
                    pygame.mouse.get_pos()[1] < BOARD_INITIAL_Y_VALUE + BOARD_SQUARE_SIZE_Y*(j+1):
                if pygame.mouse.get_pos()[0] < BOARD_INITIAL_X_VALUE + BOARD_SQUARE_SIZE_X*(i+1) and \
                        pygame.mouse.get_pos()[1] > BOARD_INITIAL_Y_VALUE + BOARD_SQUARE_SIZE_Y*j:
                    if i == 0:
                        square += "A"
                    if i == 1:
                        square += "B"
                    if i == 2:
                        square += "C"
                    if i == 3:
                        square += "D"
                    if i == 4:
                        square += "E"
                    if i == 5:
                        square += "F"
                    if i == 6:
                        square += "G"
                    if i == 7:
                        square += "H"

                    if j == 0:
                        square += "8"
                    if j == 1:
                        square += "7"
                    if j == 2:
                        square += "6"
                    if j == 3:
                        square += "5"
                    if j == 4:
                        square += "4"
                    if j == 5:
                        square += "3"
                    if j == 6:
                        square += "2"
                    if j == 7:
                        square += "1"
    return square


def square_has_piece(square):
    for piece in piecePositionList:
        if piece[1] == square:
            return True
    return False
