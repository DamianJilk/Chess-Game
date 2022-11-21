"""
The main class of the chess game. 

Recent changes:
- When selecting a chess piece, all possible moves are displayed
- Possible moves that need to be implemented yet:
     --> restricting moves when king is in check
     --> restricting moves when a move would cause the king to be in check
     --> castling
- En passant possible moves
- King in check is under development -- does not keep color indicator when king is in check after piece is selected

Future Work:
- Finish possible moves
- Add clock
- Randomize the color (right now, white is always the user)
- Create AI 1.0 --> makes random moves
- Create AI 2.0 --> better than me (ELO ~ 1000)
"""

# import time
from chess_possible_moves import *

# when true, can move pieces anywhere without following the possible moves
debug_mode = False

# used to only check if king is in check once before making a move
king_in_check_counter = 0


def loop():
    """
    Main loop that repeats the while loop udntil the window is closed with gui.destroy()
    """
    place_pieces(start_game=True)

    firstPress = False

    running = True
    while running:
        event_list = pygame.event.get()

        global king_in_check_counter
        if king_in_check_counter == 0:
            king_in_check()  # used to check if the king is in check
            king_in_check_counter += 1

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] is True:
                    if pointer_on_exit():
                        # closes out of game when exit is clicked
                        pygame.quit()
                        running = False
                        break

                    if firstPress is False:
                        # the first piece is clicked

                        original_position = pointer_on_square()
                        if original_position != "" and square_has_piece(original_position):
                            firstPress = True
                            show_possible_moves(original_position)
                            break

                    if firstPress is True:
                        # second click
                        # final_position is where piece will move
                        final_position = pointer_on_square()

                        if final_position != "" and original_position != final_position:
                            if debug_mode:  # enables the user to make any move
                                move_piece(original_position, final_position)
                                king_in_check_counter = 0
                                firstPress = False
                                break
                            else:  # restricts user to only make possible moves
                                if final_position in possible_moves_list:
                                    move_piece(original_position,
                                               final_position)
                                    king_in_check_counter = 0  # resets counter to check if king is in check
                                    firstPress = False
                                    break
                                else:
                                    firstPress = False
                                    place_pieces()
                                    break
                        else:
                            firstPress = False
                            place_pieces()
                            break

                if pygame.mouse.get_pressed()[2] is True:
                    # right click
                    continue


def main():
    """
    The main function that calls the loop
    """
    loop()


main()
