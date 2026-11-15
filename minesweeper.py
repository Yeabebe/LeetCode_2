from typing import list 

class Solution:
    def updateBoard(self, board: list[list[str]], click: list[int]) -> list[list[str]]:
        m, n = len(board), len(board[0])
        r, c = click

        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        def dfs(r, c):
            mines = 0

            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n:
                        if board[nr][nc] == 'M':
                            mines += 1

            if mines > 0:
                board[r][c] = str(mines)
                return

            board[r][c] = 'B'

            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n:
                        if board[nr][nc] == 'E':
                            dfs(nr, nc)

        dfs(r, c)
        return board