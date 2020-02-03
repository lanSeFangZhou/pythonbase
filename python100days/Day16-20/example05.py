'''
递归回溯法：叫称为试探法，按选优条件向前搜索，当搜索到某一步，
发现原先选择并不优或达不到目标时，就退回一步重新选择。
经典问题：骑士巡逻
'''

import os
import sys
import time

size = 5
total = 0

def print_board(board):
    # os.system('clear')
    for row in board:
        for col in row:
            print(str(col).center(4), end='')
        print()


def patrol(board, row, col, step=1):
    if row >= 0 and row < size and \
        col >= 0 and col < size and \
        board[row][col] == 0:
        board[row][col] == step
        if step == size * size:
            global total
            total += 1
            print(f'第{total}=种走法: ')
            print_board(board)
        patrol(board, row - 2, col - 1, step + 1)
        patrol(board, row - 1, col - 2, step + 1)
        patrol(board, row + 1, col - 2, step + 1)
        patrol(board, row + 2, col - 1, step + 1)
        patrol(board, row + 2, col + 1, step + 1)
        patrol(board, row + 1, col + 2, step + 1)
        patrol(board, row - 1, col + 2, step + 1)
        patrol(board, row - 2, col + 1, step + 1)
        board[row][col] = 0

def main():
    board = [[0] * size for _ in range(size)]
    patrol(board, size - 1, size - 1)

if __name__ == '__main__':
    main()