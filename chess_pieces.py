"""
This class is used to create the chess piece images and "blits" them onto the screen. 
All of these functions use the create_piece_image function.
"""

from chess_init import *


def black_bishop(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    black_bishop_image = create_piece_image(
        'black_bishop.png', BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    screen.blit(black_bishop_image, (get_piece_position_x(
        position), get_piece_position_y(position)))


def black_king(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    black_king_image = create_piece_image(
        'black_king.png', BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    screen.blit(black_king_image, (get_piece_position_x(
        position), get_piece_position_y(position)))


def black_knight(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    black_knight_image = create_piece_image(
        'black_knight.png', BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    screen.blit(black_knight_image, (get_piece_position_x(
        position), get_piece_position_y(position)))


def black_pawn(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    black_pawn_image = create_piece_image(
        'black_pawn.png', BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    screen.blit(black_pawn_image, (get_piece_position_x(
        position), get_piece_position_y(position)))


def black_queen(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    black_queen_image = create_piece_image(
        'black_queen.png', BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    screen.blit(black_queen_image, (get_piece_position_x(
        position), get_piece_position_y(position)))


def black_rook(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    black_rook_image = create_piece_image(
        'black_rook.png', BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    screen.blit(black_rook_image, (get_piece_position_x(
        position), get_piece_position_y(position)))


def white_bishop(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    white_bishop_image = create_piece_image(
        'white_bishop.png', BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    screen.blit(white_bishop_image, (get_piece_position_x(
        position), get_piece_position_y(position)))


def white_king(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    white_king_image = create_piece_image(
        'white_king.png', BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    screen.blit(white_king_image, (get_piece_position_x(
        position), get_piece_position_y(position)))


def white_knight(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    white_knight_image = create_piece_image(
        'white_knight.png', BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    screen.blit(white_knight_image, (get_piece_position_x(
        position), get_piece_position_y(position)))


def white_pawn(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    white_pawn_image = create_piece_image(
        'white_pawn.png', BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    screen.blit(white_pawn_image, (get_piece_position_x(
        position), get_piece_position_y(position)))


def white_queen(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    white_queen_image = create_piece_image(
        'white_queen.png', BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    screen.blit(white_queen_image, (get_piece_position_x(
        position), get_piece_position_y(position)))


def white_rook(position: str):
    """
    Constructs the chess piece on the display

    Args:
        position (str): position of chess piece ("A7")
    """

    white_rook_image = create_piece_image(
        'white_rook.png', BOARD_SQUARE_SIZE_X, BOARD_SQUARE_SIZE_Y)
    screen.blit(white_rook_image, (get_piece_position_x(
        position), get_piece_position_y(position)))
