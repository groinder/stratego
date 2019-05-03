from multiprocessing import Pool

from stratego.MinMax2 import MinMax2
from stratego.MinMax2AB import MinMax2AB
from stratego.Stratego import Stratego


def play(size, player1, player2):
    stratego = Stratego(size)

    player1_points = 0
    player2_points = 0

    player1_moves = 0
    player2_moves = 0

    player1_moves_time = 0
    player2_moves_time = 0

    player1_turn = True
    while not stratego.is_finished():
        if player1_turn:
            points, space, move_time = player1.move(stratego)
            player1_points += points
            player1_moves += 1
            player1_moves_time += move_time
        else:
            points, space, move_time = player2.move(stratego)
            player2_points += points
            player2_moves += 1
            player2_moves_time += move_time

        player1_turn = not player1_turn

    return size, player1_points, player1_moves, player1_moves_time, player2_points, player2_moves, player2_moves_time


if __name__ == '__main__':
    start_size = 4
    end_size = 11
    min_max = MinMax2(2)
    min_max_ab = MinMax2AB(2)

    print("Player 1: MinMax, Player 2: MinMaxAB")
    print("size,player1_points,player1_moves,player1_moves_time,player2_points,player2_moves,player2_moves_time")
    with Pool(processes=4) as pool:
        sizes = range(start_size, end_size)
        res = pool.starmap(play, [(size, min_max, min_max_ab) for size in sizes])
        for game in res:
            print("{},{},{},{},{},{},{}".format(*game))
        pool.close()
        pool.join()

    print("Player 1: MinMaxAB, Player 2: MinMax")
    print("size,player1_points,player1_moves,player1_moves_time,player2_points,player2_moves,player2_moves_time")
    with Pool(processes=4) as pool:
        sizes = range(start_size, end_size)
        res = pool.starmap(play, [(size, min_max_ab, min_max) for size in sizes])
        for game in res:
            print("{},{},{},{},{},{},{}".format(*game))
        pool.close()
        pool.join()
