class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(dict)
        cols = defaultdict(dict)
        sqrs = defaultdict(dict)
        for r in range(9):
            sq_row=r//3
            for c in range(9):                
                v = board[r][c]
                if v!=".":
                    if v in rows[r]:
                        #print(f"{v} already exists in row {r}:{rows[r]}\n")
                        return False
                    if v in cols[c]:
                        #print(f"{v} already exists in col {c}:{cols[c]}\n")
                        return False
                    rows[r][v]=1
                    cols[c][v]=1
                    sq_col=c//3
                    sq_key = sq_row*10+sq_col
                    if v in sqrs[sq_key]:
                        #print(f"{v} already exists in sql {sq_key}:{sqrs[sq_key]}\n")
                        return False
                    sqrs[sq_key][v]=1
                    #print(f"r={r} c={c} sq_key={sq_key} value={v}")
        return True

