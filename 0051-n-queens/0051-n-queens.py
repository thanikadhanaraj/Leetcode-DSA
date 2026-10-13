class Solution:
    def solveNQueens(self, n):
        result = []

        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                ans = []

                for i in range(n):
                    ans.append("".join(board[i]))

                result.append(ans)
                return

            for col in range(n):

                # Check column
                safe = True

                for i in range(row):
                    if board[i][col] == "Q":
                        safe = False
                        break

                # Check left diagonal
                if safe:
                    i = row - 1
                    j = col - 1

                    while i >= 0 and j >= 0:
                        if board[i][j] == "Q":
                            safe = False
                            break
                        i -= 1
                        j -= 1

                # Check right diagonal
                if safe:
                    i = row - 1
                    j = col + 1

                    while i >= 0 and j < n:
                        if board[i][j] == "Q":
                            safe = False
                            break
                        i -= 1
                        j += 1

                if safe:
                    board[row][col] = "Q"

                    backtrack(row + 1)

                    board[row][col] = "."

        backtrack(0)

        return result