import chess
import sunfish
import math
import random
import sys



def minimaxRoot(depth, board,isMaximizing):
    possibleMoves = board.legal_moves
    bestMove = -9999
    bestMoveFinal = None
    for x in possibleMoves:
        move = chess.Move.from_uci(str(x))
        board.push(move)
        value = max(bestMove, minimax(depth - 1, board,-10000,10000, not isMaximizing))
        board.pop()
        if ( value > bestMove):
            print("Best score: ", bestMove)
            print("Best move: ", bestMoveFinal)
            bestMove = value
            bestMoveFinal = move
    return bestMoveFinal

def minimax(depth, board, alpha, beta, is_maximizing):
    if(depth == 0):
        return -evaluation(board)
    possibleMoves = board.legal_moves
    if is_maximizing:
        bestMove = -9999
        for x in possibleMoves:
            move = chess.Move.from_uci(str(x))
            board.push(move)
            bestMove = max(bestMove,minimax(depth - 1, board,alpha,beta, not is_maximizing))
            board.pop()
            alpha = max(alpha,bestMove)
            if beta <= alpha:
                return bestMove
    else:
        bestMove = 9999
        for x in possibleMoves:
            move = chess.Move.from_uci(str(x))
            board.push(move)
            bestMove = min(bestMove, minimax(depth - 1, board,alpha,beta, not is_maximizing))
            board.pop()
            beta = min(beta,bestMove)
            if(beta <= alpha):
                return bestMove

    return bestMove


def calculateMove(board):
    possible_moves = board.legal_moves
    if(len(possible_moves) == 0):
        print("No more possible moves...Game Over")
        sys.exit()
    bestMove = None
    bestValue = -9999
    n = 0
    for x in possible_moves:
        move = chess.Move.from_uci(str(x))
        board.push(move)
        boardValue = -evaluation(board)
        board.pop()
        if(boardValue > bestValue):
            bestValue = boardValue
            bestMove = move

    return bestMove

def evaluation(board):
    i = 0
    evaluation = 0
    x = True
    try:
        x = bool(board.piece_at(i).color)
    except AttributeError as e:
        x = x
    while i < 63:
        i += 1
        evaluation = evaluation + (getPieceValue(str(board.piece_at(i))) if x else -getPieceValue(str(board.piece_at(i))))
    return evaluation


def getPieceValue(piece):
    if piece is None:
        return 0
    value = 0
    if piece in ["P", "p"]:
        value = 10
    if piece in ["N", "n"]:
        value = 30
    if piece in ["B", "b"]:
        value = 30
    if piece in ["R", "r"]:
        value = 50
    if piece in ["Q", "q"]:
        value = 90
    if piece in ['K', 'k']:
        value = 900
    #value = value if (board.piece_at(place)).color else -value
    return value

def main():
    board = chess.Board()
    print(board)
    for n in range(100):
        if n%2 == 0:
            move = input("Enter move: ")
        else:
            print("Computers Turn:")
            move = minimaxRoot(3,board,True)
        move = chess.Move.from_uci(str(move))
        board.push(move)
        print(board)





if __name__ == "__main__":
    main()