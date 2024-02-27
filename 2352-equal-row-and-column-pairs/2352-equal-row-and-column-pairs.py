class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        columns = [[] for i in range(len(grid))]
        
        for i in range(0,len(grid)):
            for j in range(0,len(grid)):
                columns[j].append(grid[i][j])
        
        pairs = 0
        for row in range(len(grid)):
            for col in range(len(grid)):
                if grid[row]== columns[col]:
                    pairs+=1
        return pairs
                
                
        