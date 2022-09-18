from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set()
        negDiag = set()

        result = []
        sub = []

        def dfs(row):
            if row == n:
                result.append(sub.copy())
                return

            for col in range(n):
                if col not in cols and (row+col) not in posDiag and (row-col) not in negDiag:
                    str = ["." for _ in range(n)]
                    str[col] = "Q"
                    sub.append("".join(str))
                    cols.add(col)
                    posDiag.add(row+col)
                    negDiag.add(row-col)

                    dfs(row + 1)

                    cols.remove(col)
                    posDiag.remove(row+col)
                    negDiag.remove(row-col)
                    sub.pop()
            return

        dfs(0)
        return result

n = 4
a = Solution()
a.solveNQueens(4)
