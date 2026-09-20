import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=collections.defaultdict(set)
        c=collections.defaultdict(set)
        box=collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                val=board[i][j]

                if val in r[i] or val in c[j] or val in box[(i//3,j//3)]:
                    return False
                r[i].add(val)
                c[j].add(val)
                box[(i//3,j//3)].add(val)

        return True