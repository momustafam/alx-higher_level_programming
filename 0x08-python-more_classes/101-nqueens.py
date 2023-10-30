#!/usr/bin/python3
"""
    N Queens Problem
"""
import sys
import time


def find_place(q, cols, rows, d1, d2):
    '''
        find an appropriate row in the qth column to set the qth queen

        Args:
        -----
            q (int): the current column/queen
            cols (list): a list that contains row number for each queen
            rows (list): a list that contains rows of the chessboard
            d1 (list): a list that contains the first diagonals
            d2 (list): a list that contains the second diagonals

        Return:
        -------
        True if there is a place for the given queen
        False otherwise
    '''

    start = cols[q] + 1
    n = len(cols) - 1

    if start != 1:
        r = cols[q]
        rows[r] = 1
        d1[n-q+r] = 1
        d2[r+q-1] = 1
    # loop from next position of the queen to last row of the chessboard
    for r in range(start, n+1):
        # checking that the current row is non-attaking row
        if rows[r] and d1[n-q+r] and d2[r+q-1]:
            cols[q] = r
            rows[r], d1[n-q+r], d2[r+q-1] = 0, 0, 0
            return True
    return False


def get_chessboard(n):
    '''
        create a chessboard

        Args:
        -----
            n (int): number of rows/columns
    '''
    # 1 means that a new queen can use that place
    rows = [1 for i in range(n+1)]
    cols = [0 for i in range(n+1)]
    d1 = [1 for i in range(2*n)]
    d2 = d1[:]

    return (rows, cols, d1, d2)

def put_nqueens(n):
    '''
        Function that place N non-attacking queens on an NxN chessboard

        Args:
        -----
            N (int): number of rows and columns
    '''

    rows, cols, d1, d2 = get_chessboard(n)
    cur_q = 1
    found = None
    sols = []

    while True:
        while 1 <= cur_q <= n: 
            found = find_place(cur_q, cols, rows, d1, d2)
            if not found and cols[cur_q]:
                r = cols[cur_q]
                rows[r] = 1
                d1[n - cur_q + r] = 1
                d2[r + cur_q - 1] = 1
                cols[cur_q] = 0
                cur_q -= 1
            elif not found:
                cur_q -= 1
            else:
                cur_q += 1 

        # remove the chessboard except the first column to find another sol
        # or finish the break the loop (all possible solutions found)
        if not cur_q:
            break
        else:
            # store the solution
            sol = []
            for i in range(1, n+1):
                sol.append([cols[i]-1, i-1])
            sols.append(sol)
            temp = cols[1]
            # clear the chessboard to search about another solution
            rows, cols, d1, d2 = get_chessboard(n)
            r = temp
            cols[1] = r
            rows[r] = 0
            d1[n-1+r] = 0
            d2[r] = 0
            cur_q = 1
        
    # print all possible solutions
    for sol in sols:
        print(sol)


def main():
    '''
        Entry point of the program
    '''

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    n = sys.argv[1]
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(n)
    if n < 4:
        print("N must be at least 4")

    put_nqueens(n)


main()
