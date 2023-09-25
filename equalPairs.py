class Solution(object):
    def equalPairs(self, grid):
        d={}
        l=0
        for k in range(len(grid)):
            d[k]=grid[k][:]
        for i in range(len(grid)):
            for j in range(i):
                grid[j][i],grid[i][j]=grid[i][j],grid[j][i]
        for i in range(len(grid)):
            for j in range(len(grid)):
                if d[i] == grid[j]:
                    l+=1
        return l