#!/bin/python3
# https://www.hackerrank.com/challenges/queens-attack-2/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign
# queens_attack.py

import math
import numpy as np

import os
import random
import re
import sys
import pprint
from random import uniform
DEBUG= True

# The following solution is too slow
# def piece_activity(chess_board, dx, dy, count, Qx, Qy):
#     if(DEBUG):
#         print("^" * 30)
#         print(f"{dx}, {dy}, {count}, {Qx}, {Qy}")
#         print(np.matrix(chess_board))


#     board_size = len(chess_board)
#     if(Qx < 0 or Qy < 0 or Qx >= board_size or Qy >= board_size ):
#         return count
#     if(chess_board[Qx][Qy] != "0"):
#         return count
    
#     # increase count
#     count += 1

#     # mark element as visited
#     chess_board[Qx][Qy] = 'v'

#     count = piece_activity(chess_board,dx, dy, count, Qx+dx, Qy+dy)

#     return count
# # Complete the queensAttack function below.
# Too slow
# def queensAttack(n, k, r_q, c_q, obstacles):
#     working_r_q = r_q - 1
#     working_c_q = c_q - 1
#     working_obstacles = [(x-1, y-1) for x, y in obstacles]
#     if(DEBUG):
#         print('^' * 30)
#         print(f"{n}, {k}, {working_r_q}, {working_c_q}, {working_obstacles}")

#     # make an empty board:
#     chess_board = [ ["0" for i in range(n)] for j in range(n)]

#     # add obstacles
#     for x, y in working_obstacles:
#         chess_board[x][y] = "x"

#     # add the queen to the board
#     chess_board[working_r_q][working_c_q] = "Q"

#     # get activity
#     count = 0

#     # traverse in other directions
#     for i in range(-1, 2):
#         for j in range(-1, 2):
#             count = piece_activity(chess_board,i,j,count, working_r_q+i, working_c_q+j)

#     return count


def queensAttack(n, k, r_q, c_q, obstacles):
    count = 0
    working_r_q = r_q - 1
    working_c_q = c_q - 1
    working_obstacles = [(x-1, y-1) for x, y in obstacles]
    obstacles_dict = { key: 1 for key in working_obstacles }
    print(obstacles_dict)
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if(i==j==0):
                continue
            curr_x = working_r_q + i
            curr_y = working_c_q + j
            next_square = (curr_x, curr_y)

            while(curr_x >= 0 and curr_x < n and curr_y>=0 and curr_y < n):
                if(next_square in obstacles_dict):
                    curr_x = -1
                else:
                    count += 1

                    if DEBUG:
                        print("^"*30)
                        print(f"cur x: {curr_x}, curr y : {curr_y}, count = {count}")
                        print(f"direction ({i}, {j})")   
                    curr_x += i
                    curr_y +=  j
                    next_square = (curr_x, curr_y)
       
                    # count = piece_activity(chess_board,i,j,count, working_r_q+i, working_c_q+j)

    return count

if __name__ == '__main__':
    n = 1
    k = 0
    r_q = 1
    c_q = 1
    obstacles = []
    #[(5, 5), (4, 2), (2, 3)]
    # [(1, 1), (2, 3)]
    #[]
    # #[(2, 2), (2, 3), (2, 4), (3, 2), (3, 2) ,(3, 4), (4, 2), (4, 3),]    
    # 
    # 
    # #bigger input test
    # n = 1300
    # k = 200
    # r_q = 3
    # c_q = 3
    # obstacles = []
    # for i in range(k):
    #     ob_x = int(uniform(1, n))
    #     ob_y = int(uniform(1, n))
    #     if(ob_x != r_q and ob_y != c_q):
    #         obstacles.append( (ob_x, ob_y) )
        

    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result )

