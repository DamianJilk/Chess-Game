"""
This class is used to show all possible moves for the current chess position.
"""

from chess_setup_movement import *

# list of valid letters
letter_list = ["A", "B", "C", "D", "E", "F", "G", "H"]
# list of valid numbers
number_list = ["1", "2", "3", "4", "5", "6", "7", "8"]
possible_moves_list = []  # used to see possible moves outside of this class


def show_possible_moves(position: str):
    """
    When called with a position, adds all of the possible moves of that piece to
    possible_moves list. Then updates board and resets highlighted squares.

    Args:
        position (str): position such as "A7"
    """
    # highlights current piece
    highlight_square.append(position)

    for iterate_piece in piecePositionList:
        if iterate_piece[1] == position:
            piece = iterate_piece
    if piece[0][6:] == "pawn" and piece[0][:5] == "white":
        white_pawn_possible_moves(piece)

    if piece[0][6:] == "pawn" and piece[0][:5] == "black":
        black_pawn_possible_moves(piece)

    if piece[0][6:] == "rook" and piece[0][:5] == "white":
        white_rook_possible_moves(piece)

    if piece[0][6:] == "rook" and piece[0][:5] == "black":
        black_rook_possible_moves(piece)

    if piece[0][6:] == "knight" and piece[0][:5] == "white":
        white_knight_possible_moves(piece)

    if piece[0][6:] == "knight" and piece[0][:5] == "black":
        black_knight_possible_moves(piece)

    if piece[0][6:] == "bishop" and piece[0][:5] == "white":
        white_bishop_possible_moves(piece)

    if piece[0][6:] == "bishop" and piece[0][:5] == "black":
        black_bishop_possible_moves(piece)

    if piece[0][6:] == "queen" and piece[0][:5] == "white":
        white_queen_possible_moves(piece)

    if piece[0][6:] == "queen" and piece[0][:5] == "black":
        black_queen_possible_moves(piece)

    if piece[0][6:] == "king" and piece[0][:5] == "white":
        white_king_possible_moves(piece)

    if piece[0][6:] == "king" and piece[0][:5] == "black":
        black_king_possible_moves(piece)

    place_pieces()

    # clears highlighted square and possible moves after printing to screen
    highlight_square.clear()
    # saves previous possible moves to use outside of this class
    possible_moves_list[:] = possible_moves
    possible_moves.clear()


def white_pawn_possible_moves(piece: list):
    """
    Adds all possible moves for a white pawn to possible_moves list

    Args:
        piece (list): example --> ["white pawn", "A7"]
    """
    # need to do - check if king is in check
    # need to do - check if king will be in check after move

    pawn_move_one = True
    pawn_move_two = True
    capture_piece_right = False
    capture_piece_left = False

    for iterate_piece in piecePositionList:
        if iterate_piece[1] == piece[1][0] + str(int(piece[1][1]) + 1):
            # checks if piece is in the way of moving one forward
            pawn_move_one = False

        if iterate_piece[1] == piece[1][0] + str(int(piece[1][1]) + 2):
            # checks if piece is in the way of moving two forward
            pawn_move_two = False

        if iterate_piece[1] == chr(ord(piece[1][0]) + 1) + str(int(piece[1][1]) + 1):
            # checks if there is a piece one space diagonal on the right side
            if iterate_piece[0][:5] != "white":
                capture_piece_right = True

        if iterate_piece[1] == chr(ord(piece[1][0]) - 1) + str(int(piece[1][1]) + 1):
            # checks if there is a piece one space diagonal on the left side
            if iterate_piece[0][:5] != "white":
                capture_piece_left = True

    if pawn_move_one is True:
        # adds moving forward one
        possible_moves.append(piece[1][0] + str(int(piece[1][1]) + 1))

    if pawn_move_two is True and piece[1][1] == "2" and pawn_move_one is True:
        # need to check if this is first move (should only be on 2nd row)
        # adds moving forward twice
        possible_moves.append(piece[1][0] + str(int(piece[1][1]) + 2))

    if capture_piece_right is True:
        # adds right capture
        possible_moves.append(
            chr(ord(piece[1][0]) + 1) + str(int(piece[1][1]) + 1))

    if capture_piece_left is True:
        # adds left capture
        possible_moves.append(
            chr(ord(piece[1][0]) - 1) + str(int(piece[1][1]) + 1))

    # checks en passant captures
    if piece[1][1] == "5":
        if len(en_passant_list) != 0:
            if en_passant_list[-1][1] == chr(ord(piece[1][0]) - 1) + piece[1][1]:
                possible_moves.append(
                    chr(ord(piece[1][0]) - 1) + str(int(piece[1][1]) + 1))
            if en_passant_list[-1][1] == chr(ord(piece[1][0]) + 1) + piece[1][1]:
                possible_moves.append(
                    chr(ord(piece[1][0]) + 1) + str(int(piece[1][1]) + 1))


def black_pawn_possible_moves(piece: list):
    """
    Adds all possible moves for a black pawn to possible_moves list

    Args:
        piece (list): example --> ["white pawn", "A7"]
    """
    # need to do - check if king is in check
    # need to do - check if king will be in check after move

    pawn_move_one = True
    pawn_move_two = True
    capture_piece_right = False
    capture_piece_left = False

    for iterate_piece in piecePositionList:
        if iterate_piece[1] == piece[1][0] + str(int(piece[1][1]) - 1):
            # checks if piece is in the way of moving one forward
            pawn_move_one = False

        if iterate_piece[1] == piece[1][0] + str(int(piece[1][1]) - 2):
            # checks if piece is in the way of moving two forward
            pawn_move_two = False

        if iterate_piece[1] == chr(ord(piece[1][0]) + 1) + str(int(piece[1][1]) - 1):
            # checks if there is a piece one space diagonal on the right side
            if iterate_piece[0][:5] != "black":
                capture_piece_right = True

        if iterate_piece[1] == chr(ord(piece[1][0]) - 1) + str(int(piece[1][1]) - 1):
            # checks if there is a piece one space diagonal on the left side
            if iterate_piece[0][:5] != "black":
                capture_piece_left = True

    if pawn_move_one is True:
        # adds moving forward one
        possible_moves.append(piece[1][0] + str(int(piece[1][1]) - 1))

    if pawn_move_two is True and piece[1][1] == "7" and pawn_move_one is True:
        # need to check if this is first move (should only be on 7th row)
        # adds moving forward twice
        possible_moves.append(piece[1][0] + str(int(piece[1][1]) - 2))

    if capture_piece_right is True:
        # adds right capture
        possible_moves.append(
            chr(ord(piece[1][0]) + 1) + str(int(piece[1][1]) - 1))

    if capture_piece_left is True:
        # adds left capture
        possible_moves.append(
            chr(ord(piece[1][0]) - 1) + str(int(piece[1][1]) - 1))

    # checks en passant captures
    if piece[1][1] == "4":
        if len(en_passant_list) != 0:
            if en_passant_list[-1][1] == chr(ord(piece[1][0]) - 1) + piece[1][1]:
                possible_moves.append(
                    chr(ord(piece[1][0]) - 1) + str(int(piece[1][1]) - 1))
            if en_passant_list[-1][1] == chr(ord(piece[1][0]) + 1) + piece[1][1]:
                possible_moves.append(
                    chr(ord(piece[1][0]) + 1) + str(int(piece[1][1]) - 1))


def white_rook_possible_moves(piece: list):
    """
    Adds all possible moves for a white rook to possible_moves list

    Args:
        piece (list): example --> ["white pawn", "A7"]
    """
    # need to do - check if king is in check
    # need to do - check if king will be in check after move
    # check if other pieces in the way

    horizontal_list = []
    vertical_list = []

    for iterate_piece in piecePositionList:
        if iterate_piece[1][0] == piece[1][0]:
            vertical_list.append(iterate_piece)
        if iterate_piece[1][1] == piece[1][1]:
            horizontal_list.append(iterate_piece)

    # right horizontal
    continue_iteration_rh = True
    add_first_rh = True
    break_outer_loop_rh = False
    for i in range(1, 8):
        if break_outer_loop_rh is False:
            horizontal_square_rh = chr(ord(piece[1][0]) + i) + piece[1][1]
            # increments letter to go to the right on the chess board
            if horizontal_square_rh[0] in letter_list:
                # ensures horizontal_square_rh is valid
                for iterate_piece in horizontal_list:
                    if horizontal_square_rh == iterate_piece[1]:
                        if iterate_piece[0][:5] == "white":
                            # if white piece, do not add and do not continue loop
                            continue_iteration_rh = False
                            break_outer_loop_rh = True
                            break

                        continue_iteration_rh = False
                        # adds the first piece in the row to the possible_moves
                        if add_first_rh is True:
                            possible_moves.append(horizontal_square_rh)
                            add_first_rh = False
                        break

                if continue_iteration_rh is True:
                    possible_moves.append(horizontal_square_rh)

    # left horizontal
    continue_iteration_lh = True
    add_first_lh = True
    break_outer_loop_lh = False
    for i in range(1, 8):
        if break_outer_loop_lh is False:
            horizontal_square_lh = chr(ord(piece[1][0]) - i) + piece[1][1]
            # increments letter to go to the left on the chess board
            if horizontal_square_lh[0] in letter_list:
                for iterate_piece in horizontal_list:
                    if horizontal_square_lh == iterate_piece[1]:
                        if iterate_piece[0][:5] == "white":
                            # if white piece, do not add and do not continue loop
                            continue_iteration_lh = False
                            break_outer_loop_lh = True
                            break
                        continue_iteration_lh = False
                        # adds the first piece in the row to the possible_moves
                        if add_first_lh is True:
                            possible_moves.append(horizontal_square_lh)
                            add_first_lh = False
                        break
                if continue_iteration_lh is True:
                    possible_moves.append(horizontal_square_lh)

    # up vertical
    continue_iteration_uv = True
    add_first_uv = True
    break_outer_loop_uv = False
    for i in range(1, 8):
        if break_outer_loop_uv is False:
            vertical_square_uv = piece[1][0] + str(int(piece[1][1]) + i)
            if vertical_square_uv[1:] in number_list:
                for iterate_piece in vertical_list:
                    if vertical_square_uv == iterate_piece[1]:
                        if iterate_piece[0][:5] == "white":
                            # if white piece, do not add and do not continue loop
                            continue_iteration_uv = False
                            break_outer_loop_uv = True
                            break
                        continue_iteration_uv = False
                        # adds the first piece in the row to the possible_moves
                        if add_first_uv is True:
                            possible_moves.append(vertical_square_uv)
                            add_first_uv = False
                        break
                if continue_iteration_uv is True:
                    possible_moves.append(vertical_square_uv)

    # down vertical
    continue_iteration_dv = True
    add_first_dv = True
    break_outer_loop_dv = False
    for i in range(1, 8):
        if break_outer_loop_dv is False:
            vertical_square_uv = piece[1][0] + str(int(piece[1][1]) - i)
            if vertical_square_uv[1:] in number_list:
                for iterate_piece in vertical_list:
                    if vertical_square_uv == iterate_piece[1]:
                        if iterate_piece[0][:5] == "white":
                            # if white piece, do not add and do not continue loop
                            continue_iteration_dv = False
                            break_outer_loop_dv = True
                            break
                        continue_iteration_dv = False
                        # adds the first piece in the row to the possible_moves
                        if add_first_dv is True:
                            possible_moves.append(vertical_square_uv)
                            add_first_dv = False
                        break
                if continue_iteration_dv is True:
                    possible_moves.append(vertical_square_uv)


def black_rook_possible_moves(piece: list):
    """
    Adds all possible moves for a black rook to possible_moves list

    Args:
        piece (list): example --> ["white pawn", "A7"]
    """
    horizontal_list = []
    vertical_list = []

    for iterate_piece in piecePositionList:
        if iterate_piece[1][0] == piece[1][0]:
            vertical_list.append(iterate_piece)
        if iterate_piece[1][1] == piece[1][1]:
            horizontal_list.append(iterate_piece)

    # right horizontal
    continue_iteration_rh = True
    add_first_rh = True
    break_outer_loop_rh = False
    for i in range(1, 8):
        if break_outer_loop_rh is False:
            horizontal_square_rh = chr(ord(piece[1][0]) + i) + piece[1][1]
            # increments letter to go to the right on the chess board
            if horizontal_square_rh[0] in letter_list:
                # ensures horizontal_square_rh is valid
                for iterate_piece in horizontal_list:
                    if horizontal_square_rh == iterate_piece[1]:
                        if iterate_piece[0][:5] == "black":
                            # if black piece, do not add and do not continue loop
                            continue_iteration_rh = False
                            break_outer_loop_rh = True
                            break

                        continue_iteration_rh = False
                        # adds the first piece in the row to the possible_moves
                        if add_first_rh is True:
                            possible_moves.append(horizontal_square_rh)
                            add_first_rh = False
                        break

                if continue_iteration_rh is True:
                    possible_moves.append(horizontal_square_rh)

    # left horizontal
    continue_iteration_lh = True
    add_first_lh = True
    break_outer_loop_lh = False
    for i in range(1, 8):
        if break_outer_loop_lh is False:
            horizontal_square_lh = chr(ord(piece[1][0]) - i) + piece[1][1]
            # increments letter to go to the left on the chess board
            if horizontal_square_lh[0] in letter_list:
                for iterate_piece in horizontal_list:
                    if horizontal_square_lh == iterate_piece[1]:
                        if iterate_piece[0][:5] == "black":
                            # if black piece, do not add and do not continue loop
                            continue_iteration_lh = False
                            break_outer_loop_lh = True
                            break
                        continue_iteration_lh = False
                        # adds the first piece in the row to the possible_moves
                        if add_first_lh is True:
                            possible_moves.append(horizontal_square_lh)
                            add_first_lh = False
                        break
                if continue_iteration_lh is True:
                    possible_moves.append(horizontal_square_lh)

    # up vertical
    continue_iteration_uv = True
    add_first_uv = True
    break_outer_loop_uv = False
    for i in range(1, 8):
        if break_outer_loop_uv is False:
            vertical_square_uv = piece[1][0] + str(int(piece[1][1]) + i)
            if vertical_square_uv[1:] in number_list:
                for iterate_piece in vertical_list:
                    if vertical_square_uv == iterate_piece[1]:
                        if iterate_piece[0][:5] == "black":
                            # if black piece, do not add and do not continue loop
                            continue_iteration_uv = False
                            break_outer_loop_uv = True
                            break
                        continue_iteration_uv = False
                        # adds the first piece in the row to the possible_moves
                        if add_first_uv is True:
                            possible_moves.append(vertical_square_uv)
                            add_first_uv = False
                        break
                if continue_iteration_uv is True:
                    possible_moves.append(vertical_square_uv)

    # down vertical
    continue_iteration_dv = True
    add_first_dv = True
    break_outer_loop_dv = False
    for i in range(1, 8):
        if break_outer_loop_dv is False:
            vertical_square_uv = piece[1][0] + str(int(piece[1][1]) - i)
            if vertical_square_uv[1:] in number_list:
                for iterate_piece in vertical_list:
                    if vertical_square_uv == iterate_piece[1]:
                        if iterate_piece[0][:5] == "black":
                            # if black piece, do not add and do not continue loop
                            continue_iteration_dv = False
                            break_outer_loop_dv = True
                            break
                        continue_iteration_dv = False
                        # adds the first piece in the row to the possible_moves
                        if add_first_dv is True:
                            possible_moves.append(vertical_square_uv)
                            add_first_dv = False
                        break
                if continue_iteration_dv is True:
                    possible_moves.append(vertical_square_uv)


def white_knight_possible_moves(piece: list):
    """
    Adds all possible moves for a white knight to possible_moves list

    Args:
        piece (list): example --> ["white pawn", "A7"]
    """
    knight_list = []

    knight_square_list = knight_positions(piece)

    for iterate_piece in piecePositionList:
        if iterate_piece[1] in knight_square_list:
            knight_list.append(iterate_piece)

    empty_square_tl1 = True
    top_left_1 = chr(ord(piece[1][0]) + 1) + str(int(piece[1][1]) + 2)
    if top_left_1[0] in letter_list and top_left_1[1:] in number_list:
        # ensures top_left_1 is valid
        for iterate_piece in knight_list:
            if top_left_1 == iterate_piece[1]:
                empty_square_tl1 = False
                if iterate_piece[0][:5] == "white":
                    continue
                    # do not add piece
                else:
                    # add piece
                    possible_moves.append(top_left_1)
        if empty_square_tl1 is True:
            possible_moves.append(top_left_1)

    empty_square_tl2 = True
    top_left_2 = chr(ord(piece[1][0]) + 2) + str(int(piece[1][1]) + 1)
    if top_left_2[0] in letter_list and top_left_2[1:] in number_list:
        # ensures top_left_2 is valid
        for iterate_piece in knight_list:
            if top_left_2 == iterate_piece[1]:
                empty_square_tl2 = False
                if iterate_piece[0][:5] == "white":
                    continue
                    # do not add piece
                else:
                    # add piece
                    possible_moves.append(top_left_2)
        if empty_square_tl2 is True:
            possible_moves.append(top_left_2)

    empty_square_bl1 = True
    bottom_left_1 = chr(ord(piece[1][0]) + 2) + str(int(piece[1][1]) - 1)
    if bottom_left_1[0] in letter_list and bottom_left_1[1:] in number_list:
        # ensures bottom_left_1 is valid
        for iterate_piece in knight_list:
            if bottom_left_1 == iterate_piece[1]:
                empty_square_bl1 = False
                if iterate_piece[0][:5] == "white":
                    continue
                    # do not add piece
                else:
                    # add piece
                    possible_moves.append(bottom_left_1)
        if empty_square_bl1 is True:
            possible_moves.append(bottom_left_1)

    empty_square_bl2 = True
    bottom_left_2 = chr(ord(piece[1][0]) + 1) + str(int(piece[1][1]) - 2)
    if bottom_left_2[0] in letter_list and bottom_left_2[1:] in number_list:
        # ensures bottom_left_2 is valid
        for iterate_piece in knight_list:
            if bottom_left_2 == iterate_piece[1]:
                empty_square_bl2 = False
                if iterate_piece[0][:5] == "white":
                    continue
                    # do not add piece
                else:
                    # add piece
                    possible_moves.append(bottom_left_2)
        if empty_square_bl2 is True:
            possible_moves.append(bottom_left_2)

    empty_square_br1 = True
    bottom_right_1 = chr(ord(piece[1][0]) - 1) + str(int(piece[1][1]) - 2)
    if bottom_right_1[0] in letter_list and bottom_right_1[1:] in number_list:
        # ensures bottom_right_1 is valid
        for iterate_piece in knight_list:
            if bottom_right_1 == iterate_piece[1]:
                empty_square_br1 = False
                if iterate_piece[0][:5] == "white":
                    continue
                    # do not add piece
                else:
                    # add piece
                    possible_moves.append(bottom_right_1)
        if empty_square_br1 is True:
            possible_moves.append(bottom_right_1)

    empty_square_br2 = True
    bottom_right_2 = chr(ord(piece[1][0]) - 2) + str(int(piece[1][1]) - 1)
    if bottom_right_2[0] in letter_list and bottom_right_2[1:] in number_list:
        # ensures bottom_right_2 is valid
        for iterate_piece in knight_list:
            if bottom_right_2 == iterate_piece[1]:
                empty_square_br2 = False
                if iterate_piece[0][:5] == "white":
                    continue
                    # do not add piece
                else:
                    # add piece
                    possible_moves.append(bottom_right_2)
        if empty_square_br2 is True:
            possible_moves.append(bottom_right_2)

    empty_square_tr1 = True
    top_right_1 = chr(ord(piece[1][0]) - 2) + str(int(piece[1][1]) + 1)
    if top_right_1[0] in letter_list and top_right_1[1:] in number_list:
        # ensures top_right_1 is valid
        for iterate_piece in knight_list:
            if top_right_1 == iterate_piece[1]:
                empty_square_tr1 = False
                if iterate_piece[0][:5] == "white":
                    continue
                    # do not add piece
                else:
                    # add piece
                    possible_moves.append(top_right_1)
        if empty_square_tr1 is True:
            possible_moves.append(top_right_1)

    empty_square_tr2 = True
    top_right_2 = chr(ord(piece[1][0]) - 1) + str(int(piece[1][1]) + 2)
    if top_right_2[0] in letter_list and top_right_2[1:] in number_list:
        # ensures top_right_2 is valid
        for iterate_piece in knight_list:
            if top_right_2 == iterate_piece[1]:
                empty_square_tr2 = False
                if iterate_piece[0][:5] == "white":
                    continue
                    # do not add piece
                else:
                    # add piece
                    possible_moves.append(top_right_2)
        if empty_square_tr2 is True:
            possible_moves.append(top_right_2)


def black_knight_possible_moves(piece: list):
    """
    Adds all possible moves for a black knight to possible_moves list

    Args:
        piece (list): example --> ["white pawn", "A7"]
    """
    knight_list = []

    knight_square_list = knight_positions(piece)

    for iterate_piece in piecePositionList:
        if iterate_piece[1] in knight_square_list:
            knight_list.append(iterate_piece)

    empty_square_tl1 = True
    top_left_1 = chr(ord(piece[1][0]) + 1) + str(int(piece[1][1]) + 2)
    if top_left_1[0] in letter_list and top_left_1[1:] in number_list:
        # ensures top_left_1 is valid
        for iterate_piece in knight_list:
            if top_left_1 == iterate_piece[1]:
                empty_square_tl1 = False
                if iterate_piece[0][:5] == "black":
                    continue
                    # do not add piece
                else:
                    # add piece
                    possible_moves.append(top_left_1)
        if empty_square_tl1 is True:
            possible_moves.append(top_left_1)

    empty_square_tl2 = True
    top_left_2 = chr(ord(piece[1][0]) + 2) + str(int(piece[1][1]) + 1)
    if top_left_2[0] in letter_list and top_left_2[1:] in number_list:
        # ensures top_left_2 is valid
        for iterate_piece in knight_list:
            if top_left_2 == iterate_piece[1]:
                empty_square_tl2 = False
                if iterate_piece[0][:5] == "black":
                    continue
                    # do not add piece
                else:
                    # add piece
                    possible_moves.append(top_left_2)
        if empty_square_tl2 is True:
            possible_moves.append(top_left_2)

    empty_square_bl1 = True
    bottom_left_1 = chr(ord(piece[1][0]) + 2) + str(int(piece[1][1]) - 1)
    if bottom_left_1[0] in letter_list and bottom_left_1[1:] in number_list:
        # ensures bottom_left_1 is valid
        for iterate_piece in knight_list:
            if bottom_left_1 == iterate_piece[1]:
                empty_square_bl1 = False
                if iterate_piece[0][:5] == "black":
                    continue
                    # do not add piece
                else:
                    # add piece
                    possible_moves.append(bottom_left_1)
        if empty_square_bl1 is True:
            possible_moves.append(bottom_left_1)

    empty_square_bl2 = True
    bottom_left_2 = chr(ord(piece[1][0]) + 1) + str(int(piece[1][1]) - 2)
    if bottom_left_2[0] in letter_list and bottom_left_2[1:] in number_list:
        # ensures bottom_left_2 is valid
        for iterate_piece in knight_list:
            if bottom_left_2 == iterate_piece[1]:
                empty_square_bl2 = False
                if iterate_piece[0][:5] == "black":
                    continue
                    # do not add piece
                else:
                    # add piece
                    possible_moves.append(bottom_left_2)
        if empty_square_bl2 is True:
            possible_moves.append(bottom_left_2)

    empty_square_br1 = True
    bottom_right_1 = chr(ord(piece[1][0]) - 1) + str(int(piece[1][1]) - 2)
    if bottom_right_1[0] in letter_list and bottom_right_1[1:] in number_list:
        # ensures bottom_right_1 is valid
        for iterate_piece in knight_list:
            if bottom_right_1 == iterate_piece[1]:
                empty_square_br1 = False
                if iterate_piece[0][:5] == "black":
                    continue
                    # do not add piece
                else:
                    # add piece
                    possible_moves.append(bottom_right_1)
        if empty_square_br1 is True:
            possible_moves.append(bottom_right_1)

    empty_square_br2 = True
    bottom_right_2 = chr(ord(piece[1][0]) - 2) + str(int(piece[1][1]) - 1)
    if bottom_right_2[0] in letter_list and bottom_right_2[1:] in number_list:
        # ensures bottom_right_2 is valid
        for iterate_piece in knight_list:
            if bottom_right_2 == iterate_piece[1]:
                empty_square_br2 = False
                if iterate_piece[0][:5] == "black":
                    continue
                    # do not add piece
                else:
                    # add piece
                    possible_moves.append(bottom_right_2)
        if empty_square_br2 is True:
            possible_moves.append(bottom_right_2)

    empty_square_tr1 = True
    top_right_1 = chr(ord(piece[1][0]) - 2) + str(int(piece[1][1]) + 1)
    if top_right_1[0] in letter_list and top_right_1[1:] in number_list:
        # ensures top_right_1 is valid
        for iterate_piece in knight_list:
            if top_right_1 == iterate_piece[1]:
                empty_square_tr1 = False
                if iterate_piece[0][:5] == "black":
                    continue
                    # do not add piece
                else:
                    # add piece
                    possible_moves.append(top_right_1)
        if empty_square_tr1 is True:
            possible_moves.append(top_right_1)

    empty_square_tr2 = True
    top_right_2 = chr(ord(piece[1][0]) - 1) + str(int(piece[1][1]) + 2)
    if top_right_2[0] in letter_list and top_right_2[1:] in number_list:
        # ensures top_right_2 is valid
        for iterate_piece in knight_list:
            if top_right_2 == iterate_piece[1]:
                empty_square_tr2 = False
                if iterate_piece[0][:5] == "black":
                    continue
                    # do not add piece
                else:
                    # add piece
                    possible_moves.append(top_right_2)
        if empty_square_tr2 is True:
            possible_moves.append(top_right_2)


def white_bishop_possible_moves(piece: list):
    """
    Adds all possible moves for a white bishop to possible_moves list

    Args:
        piece (list): example --> ["white pawn", "A7"]
    """
    # need to do - check if king is in check
    # need to do - check if king will be in check after move
    # check if other pieces in the way

    # diagonal_list shows pieces that are on the diagonals
    diagonal_list = []

    # lists or diagonal squares
    diagonal_piece_list_r_u = diagonal_r_u(piece)
    diagonal_piece_list_l_u = diagonal_l_u(piece)
    diagonal_piece_list_r_d = diagonal_r_d(piece)
    diagonal_piece_list_l_d = diagonal_l_d(piece)

    for iterate_piece in piecePositionList:
        if iterate_piece[1] in diagonal_piece_list_r_u or \
                iterate_piece[1] in diagonal_piece_list_l_u or \
                iterate_piece[1] in diagonal_piece_list_r_d or \
                iterate_piece[1] in diagonal_piece_list_l_d:
            diagonal_list.append(iterate_piece)

    # right up
    continue_iteration_ru = True
    add_first_ru = True
    break_outer_loop_ru = False
    for i in range(1, 8):
        if break_outer_loop_ru is False:
            diagonal_square_ru = chr(
                ord(piece[1][0]) + i) + str(int(piece[1][1]) + i)
            # increments letter to go to the right on the chess board
            if diagonal_square_ru[0] in letter_list and diagonal_square_ru[1:] in number_list:
                # ensures diagonal_square_ru is valid
                for iterate_piece in diagonal_list:
                    if diagonal_square_ru == iterate_piece[1]:
                        if iterate_piece[0][:5] == "white":
                            # if white piece, do not add and do not continue loop
                            continue_iteration_ru = False
                            break_outer_loop_ru = True
                            break

                        continue_iteration_ru = False
                        # adds the first piece in the row to the possible_moves
                        if add_first_ru is True:
                            possible_moves.append(diagonal_square_ru)
                            add_first_ru = False
                        break

                if continue_iteration_ru is True:
                    possible_moves.append(diagonal_square_ru)

    # left up
    continue_iteration_lu = True
    add_first_lu = True
    break_outer_loop_lu = False
    for i in range(1, 8):
        if break_outer_loop_lu is False:
            diagonal_square_lu = chr(
                ord(piece[1][0]) - i) + str(int(piece[1][1]) + i)
            # increments letter to go to the left on the chess board
            if diagonal_square_lu[0] in letter_list and diagonal_square_lu[1:] in number_list:
                for iterate_piece in diagonal_list:
                    if diagonal_square_lu == iterate_piece[1]:
                        if iterate_piece[0][:5] == "white":
                            # if white piece, do not add and do not continue loop
                            continue_iteration_lu = False
                            break_outer_loop_lu = True
                            break
                        continue_iteration_lu = False
                        # adds the first piece in the row to the possible_moves
                        if add_first_lu is True:
                            possible_moves.append(diagonal_square_lu)
                            add_first_lu = False
                        break
                if continue_iteration_lu is True:
                    possible_moves.append(diagonal_square_lu)

    # right down
    continue_iteration_rd = True
    add_first_rd = True
    break_outer_loop_rd = False
    for i in range(1, 8):
        if break_outer_loop_rd is False:
            diagonal_square_rd = chr(
                ord(piece[1][0]) + i) + str(int(piece[1][1]) - i)
            if diagonal_square_rd[0] in letter_list and diagonal_square_rd[1:] in number_list:
                for iterate_piece in diagonal_list:
                    if diagonal_square_rd == iterate_piece[1]:
                        if iterate_piece[0][:5] == "white":
                            # if white piece, do not add and do not continue loop
                            continue_iteration_rd = False
                            break_outer_loop_rd = True
                            break
                        continue_iteration_rd = False
                        # adds the first piece in the row to the possible_moves
                        if add_first_rd is True:
                            possible_moves.append(diagonal_square_rd)
                            add_first_rd = False
                        break
                if continue_iteration_rd is True:
                    possible_moves.append(diagonal_square_rd)

    # left down
    continue_iteration_lv = True
    add_first_lv = True
    break_outer_loop_lv = False
    for i in range(1, 8):
        if break_outer_loop_lv is False:
            diagonal_square_lv = chr(
                ord(piece[1][0]) - i) + str(int(piece[1][1]) - i)
            if diagonal_square_lv[0] in letter_list and diagonal_square_lv[1:] in number_list:
                for iterate_piece in diagonal_list:
                    if diagonal_square_lv == iterate_piece[1]:
                        if iterate_piece[0][:5] == "white":
                            # if white piece, do not add and do not continue loop
                            continue_iteration_lv = False
                            break_outer_loop_lv = True
                            break
                        continue_iteration_lv = False
                        # adds the first piece in the row to the possible_moves
                        if add_first_lv is True:
                            possible_moves.append(diagonal_square_lv)
                            add_first_lv = False
                        break
                if continue_iteration_lv is True:
                    possible_moves.append(diagonal_square_lv)


def black_bishop_possible_moves(piece: list):
    """
    Adds all possible moves for a black bishop to possible_moves list

    Args:
        piece (list): example --> ["white pawn", "A7"]
    """
    # need to do - check if king is in check
    # need to do - check if king will be in check after move
    # check if other pieces in the way

    # diagonal_list shows pieces that are on the diagonals
    diagonal_list = []

    # lists or diagonal squares
    diagonal_piece_list_r_u = diagonal_r_u(piece)
    diagonal_piece_list_l_u = diagonal_l_u(piece)
    diagonal_piece_list_r_d = diagonal_r_d(piece)
    diagonal_piece_list_l_d = diagonal_l_d(piece)

    for iterate_piece in piecePositionList:
        if iterate_piece[1] in diagonal_piece_list_r_u or \
                iterate_piece[1] in diagonal_piece_list_l_u or \
                iterate_piece[1] in diagonal_piece_list_r_d or \
                iterate_piece[1] in diagonal_piece_list_l_d:
            diagonal_list.append(iterate_piece)

    # right up
    continue_iteration_ru = True
    add_first_ru = True
    break_outer_loop_ru = False
    for i in range(1, 8):
        if break_outer_loop_ru is False:
            diagonal_square_ru = chr(
                ord(piece[1][0]) + i) + str(int(piece[1][1]) + i)
            # increments letter to go to the right on the chess board
            if diagonal_square_ru[0] in letter_list and diagonal_square_ru[1:] in number_list:
                # ensures diagonal_square_ru is valid
                for iterate_piece in diagonal_list:
                    if diagonal_square_ru == iterate_piece[1]:
                        if iterate_piece[0][:5] == "black":
                            # if black piece, do not add and do not continue loop
                            continue_iteration_ru = False
                            break_outer_loop_ru = True
                            break

                        continue_iteration_ru = False
                        # adds the first piece in the row to the possible_moves
                        if add_first_ru is True:
                            possible_moves.append(diagonal_square_ru)
                            add_first_ru = False
                        break

                if continue_iteration_ru is True:
                    possible_moves.append(diagonal_square_ru)

    # left up
    continue_iteration_lu = True
    add_first_lu = True
    break_outer_loop_lu = False
    for i in range(1, 8):
        if break_outer_loop_lu is False:
            diagonal_square_lu = chr(
                ord(piece[1][0]) - i) + str(int(piece[1][1]) + i)
            # increments letter to go to the left on the chess board
            if diagonal_square_lu[0] in letter_list and diagonal_square_lu[1:] in number_list:
                for iterate_piece in diagonal_list:
                    if diagonal_square_lu == iterate_piece[1]:
                        if iterate_piece[0][:5] == "black":
                            # if black piece, do not add and do not continue loop
                            continue_iteration_lu = False
                            break_outer_loop_lu = True
                            break
                        continue_iteration_lu = False
                        # adds the first piece in the row to the possible_moves
                        if add_first_lu is True:
                            possible_moves.append(diagonal_square_lu)
                            add_first_lu = False
                        break
                if continue_iteration_lu is True:
                    possible_moves.append(diagonal_square_lu)

    # right down
    continue_iteration_rd = True
    add_first_rd = True
    break_outer_loop_rd = False
    for i in range(1, 8):
        if break_outer_loop_rd is False:
            diagonal_square_rd = chr(
                ord(piece[1][0]) + i) + str(int(piece[1][1]) - i)
            if diagonal_square_rd[0] in letter_list and diagonal_square_rd[1:] in number_list:
                for iterate_piece in diagonal_list:
                    if diagonal_square_rd == iterate_piece[1]:
                        if iterate_piece[0][:5] == "black":
                            # if black piece, do not add and do not continue loop
                            continue_iteration_rd = False
                            break_outer_loop_rd = True
                            break
                        continue_iteration_rd = False
                        # adds the first piece in the row to the possible_moves
                        if add_first_rd is True:
                            possible_moves.append(diagonal_square_rd)
                            add_first_rd = False
                        break
                if continue_iteration_rd is True:
                    possible_moves.append(diagonal_square_rd)

    # left down
    continue_iteration_lv = True
    add_first_lv = True
    break_outer_loop_lv = False
    for i in range(1, 8):
        if break_outer_loop_lv is False:
            diagonal_square_lv = chr(
                ord(piece[1][0]) - i) + str(int(piece[1][1]) - i)
            if diagonal_square_lv[0] in letter_list and diagonal_square_lv[1:] in number_list:
                for iterate_piece in diagonal_list:
                    if diagonal_square_lv == iterate_piece[1]:
                        if iterate_piece[0][:5] == "black":
                            # if black piece, do not add and do not continue loop
                            continue_iteration_lv = False
                            break_outer_loop_lv = True
                            break
                        continue_iteration_lv = False
                        # adds the first piece in the row to the possible_moves
                        if add_first_lv is True:
                            possible_moves.append(diagonal_square_lv)
                            add_first_lv = False
                        break
                if continue_iteration_lv is True:
                    possible_moves.append(diagonal_square_lv)


def white_queen_possible_moves(piece: list):
    """
    Adds all possible moves for a white queen to possible_moves list

    Args:
        piece (list): example --> ["white pawn", "A7"]
    """
    # both rook and bishop possible moves
    white_rook_possible_moves(piece)
    white_bishop_possible_moves(piece)


def black_queen_possible_moves(piece: list):
    """
    Adds all possible moves for a black queen to possible_moves list

    Args:
        piece (list): example --> ["white pawn", "A7"]
    """
    # both rook and bishop possible moves
    black_rook_possible_moves(piece)
    black_bishop_possible_moves(piece)


def white_king_possible_moves(piece: list):
    """
    Adds all possible moves for a white king to possible_moves list

    Args:
        piece (list): example --> ["white pawn", "A7"]
    """

    up_right = chr(ord(piece[1][0]) + 1) + str(int(piece[1][1]) + 1)
    up_right_empty = True

    right = chr(ord(piece[1][0]) + 1) + piece[1][1]
    right_empty = True

    down_right = chr(ord(piece[1][0]) + 1) + str(int(piece[1][1]) - 1)
    down_right_empty = True

    down = piece[1][0] + str(int(piece[1][1]) - 1)
    down_empty = True

    down_left = chr(ord(piece[1][0]) - 1) + str(int(piece[1][1]) - 1)
    down_left_empty = True

    left = chr(ord(piece[1][0]) - 1) + piece[1][1]
    left_empty = True

    up_left = chr(ord(piece[1][0]) - 1) + str(int(piece[1][1]) + 1)
    up_left_empty = True

    up = piece[1][0] + str(int(piece[1][1]) + 1)
    up_empty = True

    for iterate_piece in piecePositionList:
        if iterate_piece[1] == up_right and up_right[0] in letter_list and up_right[1:] in number_list:
            up_right_empty = False
            if iterate_piece[0][:5] != "white":
                possible_moves.append(up_right)
        if iterate_piece[1] == right and right[0] in letter_list and right[1:] in number_list:
            right_empty = False
            if iterate_piece[0][:5] != "white":
                possible_moves.append(right)
        if iterate_piece[1] == down_right and down_right[0] in letter_list and down_right[1:] in number_list:
            down_right_empty = False
            if iterate_piece[0][:5] != "white":
                possible_moves.append(down_right)
        if iterate_piece[1] == down and down[0] in letter_list and down[1:] in number_list:
            down_empty = False
            if iterate_piece[0][:5] != "white":
                possible_moves.append(down)
        if iterate_piece[1] == down_left and down_left[0] in letter_list and down_left[1:] in number_list:
            down_left_empty = False
            if iterate_piece[0][:5] != "white":
                possible_moves.append(down_left)
        if iterate_piece[1] == left and left[0] in letter_list and left[1:] in number_list:
            left_empty = False
            if iterate_piece[0][:5] != "white":
                possible_moves.append(left)
        if iterate_piece[1] == up_left and up_left[0] in letter_list and up_left[1:] in number_list:
            up_left_empty = False
            if iterate_piece[0][:5] != "white":
                possible_moves.append(up_left)
        if iterate_piece[1] == up and up[0] in letter_list and up[1:] in number_list:
            up_empty = False
            if iterate_piece[0][:5] != "white":
                possible_moves.append(up)

    if up_right_empty:
        possible_moves.append(up_right)
    if right_empty:
        possible_moves.append(right)
    if down_right_empty:
        possible_moves.append(down_right)
    if down_empty:
        possible_moves.append(down)
    if down_left_empty:
        possible_moves.append(down_left)
    if left_empty:
        possible_moves.append(left)
    if up_left_empty:
        possible_moves.append(up_left)
    if up_empty:
        possible_moves.append(up)


def black_king_possible_moves(piece: list):
    """
    Adds all possible moves for a black king to possible_moves list

    Args:
        piece (list): example --> ["white pawn", "A7"]
    """
    up_right = chr(ord(piece[1][0]) + 1) + str(int(piece[1][1]) + 1)
    up_right_empty = True

    right = chr(ord(piece[1][0]) + 1) + piece[1][1]
    right_empty = True

    down_right = chr(ord(piece[1][0]) + 1) + str(int(piece[1][1]) - 1)
    down_right_empty = True

    down = piece[1][0] + str(int(piece[1][1]) - 1)
    down_empty = True

    down_left = chr(ord(piece[1][0]) - 1) + str(int(piece[1][1]) - 1)
    down_left_empty = True

    left = chr(ord(piece[1][0]) - 1) + piece[1][1]
    left_empty = True

    up_left = chr(ord(piece[1][0]) - 1) + str(int(piece[1][1]) + 1)
    up_left_empty = True

    up = piece[1][0] + str(int(piece[1][1]) + 1)
    up_empty = True

    for iterate_piece in piecePositionList:
        if iterate_piece[1] == up_right and up_right[0] in letter_list and up_right[1:] in number_list:
            up_right_empty = False
            if iterate_piece[0][:5] != "black":
                possible_moves.append(up_right)
        if iterate_piece[1] == right and right[0] in letter_list and right[1:] in number_list:
            right_empty = False
            if iterate_piece[0][:5] != "black":
                possible_moves.append(right)
        if iterate_piece[1] == down_right and down_right[0] in letter_list and down_right[1:] in number_list:
            down_right_empty = False
            if iterate_piece[0][:5] != "black":
                possible_moves.append(down_right)
        if iterate_piece[1] == down and down[0] in letter_list and down[1:] in number_list:
            down_empty = False
            if iterate_piece[0][:5] != "black":
                possible_moves.append(down)
        if iterate_piece[1] == down_left and down_left[0] in letter_list and down_left[1:] in number_list:
            down_left_empty = False
            if iterate_piece[0][:5] != "black":
                possible_moves.append(down_left)
        if iterate_piece[1] == left and left[0] in letter_list and left[1:] in number_list:
            left_empty = False
            if iterate_piece[0][:5] != "black":
                possible_moves.append(left)
        if iterate_piece[1] == up_left and up_left[0] in letter_list and up_left[1:] in number_list:
            up_left_empty = False
            if iterate_piece[0][:5] != "black":
                possible_moves.append(up_left)
        if iterate_piece[1] == up and up[0] in letter_list and up[1:] in number_list:
            up_empty = False
            if iterate_piece[0][:5] != "black":
                possible_moves.append(up)

    if up_right_empty:
        possible_moves.append(up_right)
    if right_empty:
        possible_moves.append(right)
    if down_right_empty:
        possible_moves.append(down_right)
    if down_empty:
        possible_moves.append(down)
    if down_left_empty:
        possible_moves.append(down_left)
    if left_empty:
        possible_moves.append(left)
    if up_left_empty:
        possible_moves.append(up_left)
    if up_empty:
        possible_moves.append(up)


def diagonal_r_u(piece: list):
    """
    Used to find all squares diagonally up and right

    Args:
        piece (list): example --> ["white pawn", "A7"]

    Returns:
        _type_: list of squares. example --> ["A7", "B6", "C5"]
    """
    return_list = []

    for i in range(1, 8):
        diagonal_square = chr(ord(piece[1][0]) + i) + str(int(piece[1][1]) + i)
        if diagonal_square[0] in letter_list and diagonal_square[1:] in number_list:
            return_list.append(diagonal_square)

    return return_list


def diagonal_l_u(piece: list):
    """
    Used to find all squares diagonally up and left

    Args:
        piece (list): example --> ["white pawn", "A7"]

    Returns:
        _type_: list of squares. example --> ["A7", "B6", "C5"]
    """
    return_list = []

    for i in range(1, 8):
        diagonal_square = chr(ord(piece[1][0]) - i) + str(int(piece[1][1]) + i)
        if diagonal_square[0] in letter_list and diagonal_square[1:] in number_list:
            return_list.append(diagonal_square)

    return return_list


def diagonal_r_d(piece: list):
    """
    Used to find all squares diagonally down and right

    Args:
        piece (list): example --> ["white pawn", "A7"]

    Returns:
        _type_: list of squares. example --> ["A7", "B6", "C5"]
    """
    return_list = []

    for i in range(1, 8):
        diagonal_square = chr(ord(piece[1][0]) + i) + str(int(piece[1][1]) - i)
        if diagonal_square[0] in letter_list and diagonal_square[1:] in number_list:
            return_list.append(diagonal_square)

    return return_list


def diagonal_l_d(piece: list):
    """
    Used to find all squares diagonally up and left

    Args:
        piece (list): example --> ["white pawn", "A7"]

    Returns:
        _type_: list of squares. example --> ["A7", "B6", "C5"]
    """
    return_list = []

    for i in range(1, 8):
        diagonal_square = chr(ord(piece[1][0]) - i) + str(int(piece[1][1]) - i)
        if diagonal_square[0] in letter_list and diagonal_square[1:] in number_list:
            return_list.append(diagonal_square)

    return return_list


def knight_positions(piece: list):
    """
    Used to find all positions a knight can move

    Args:
        piece (list): example --> ["white pawn", "A7"]

    Returns:
        _type_: list of squares. example --> ["A7", "B6", "C5"]
    """

    # need to implement yet!!
    return_list = []
    # knight position 1
    top_left_1 = chr(ord(piece[1][0]) + 1) + str(int(piece[1][1]) + 2)
    # knight position 2
    top_left_2 = chr(ord(piece[1][0]) + 2) + str(int(piece[1][1]) + 1)
    # knight position 3
    bottom_left_1 = chr(ord(piece[1][0]) + 2) + str(int(piece[1][1]) - 1)
    # knight position 4
    bottom_left_2 = chr(ord(piece[1][0]) + 1) + str(int(piece[1][1]) - 2)
    # knight position 5
    bottom_right_1 = chr(ord(piece[1][0]) - 1) + str(int(piece[1][1]) - 2)
    # knight position 6
    bottom_right_2 = chr(ord(piece[1][0]) - 2) + str(int(piece[1][1]) - 1)
    # knight position 7
    top_right_1 = chr(ord(piece[1][0]) - 2) + str(int(piece[1][1]) + 1)
    # knight position 8
    top_right_2 = chr(ord(piece[1][0]) - 1) + str(int(piece[1][1]) + 2)

    if top_left_1[0] in letter_list and top_left_1[1:] in number_list:
        return_list.append(top_left_1)
    if top_left_2[0] in letter_list and top_left_2[1:] in number_list:
        return_list.append(top_left_2)
    if bottom_left_1[0] in letter_list and bottom_left_1[1:] in number_list:
        return_list.append(bottom_left_1)
    if bottom_left_2[0] in letter_list and bottom_left_2[1:] in number_list:
        return_list.append(bottom_left_2)
    if bottom_right_1[0] in letter_list and bottom_right_1[1:] in number_list:
        return_list.append(bottom_right_1)
    if bottom_right_2[0] in letter_list and bottom_right_2[1:] in number_list:
        return_list.append(bottom_right_2)
    if top_right_1[0] in letter_list and top_right_1[1:] in number_list:
        return_list.append(top_right_1)
    if top_right_2[0] in letter_list and top_right_2[1:] in number_list:
        return_list.append(top_right_2)

    return return_list


def king_in_check():
    for piece in piecePositionList:

        if piece[0][6:] == "pawn" and piece[0][:5] == "white":
            white_pawn_possible_moves(piece)

        if piece[0][6:] == "pawn" and piece[0][:5] == "black":
            black_pawn_possible_moves(piece)

        if piece[0][6:] == "rook" and piece[0][:5] == "white":
            white_rook_possible_moves(piece)

        if piece[0][6:] == "rook" and piece[0][:5] == "black":
            black_rook_possible_moves(piece)

        if piece[0][6:] == "knight" and piece[0][:5] == "white":
            white_knight_possible_moves(piece)

        if piece[0][6:] == "knight" and piece[0][:5] == "black":
            black_knight_possible_moves(piece)

        if piece[0][6:] == "bishop" and piece[0][:5] == "white":
            white_bishop_possible_moves(piece)

        if piece[0][6:] == "bishop" and piece[0][:5] == "black":
            black_bishop_possible_moves(piece)

        if piece[0][6:] == "queen" and piece[0][:5] == "white":
            white_queen_possible_moves(piece)

        if piece[0][6:] == "queen" and piece[0][:5] == "black":
            black_queen_possible_moves(piece)

        if piece[0][6:] == "king" and piece[0][:5] == "white":
            white_king_possible_moves(piece)

        if piece[0][6:] == "king" and piece[0][:5] == "black":
            black_king_possible_moves(piece)

    for move in possible_moves:
        curr_piece = get_piece_from_position(move)
        if curr_piece is not None:
            if curr_piece[0] == "black king":
                print("black king is in check")
                king_check_position.append(curr_piece[1])

            if curr_piece[0] == "white king":
                print("white king is in check")
                king_check_position.append(curr_piece[1])

    possible_moves.clear()
    place_pieces()
    king_check_position.clear()

    # TODO -- implement king_in_check for all functions in show_possible_moves to limit possible moves to defend the king
    # TODO -- determine if moving a piece somewhere would put the king in check for show_possible_moves to prevent moves that cause checkmate


def get_piece_from_position(position):
    for piece in piecePositionList:
        if piece[1] == position:
            return piece
    return None
