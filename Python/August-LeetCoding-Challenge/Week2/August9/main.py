class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh = set()
        rotten = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh.add((i,j))
                elif grid[i][j] == 2:
                    rotten.add((i,j))
                    
        minutes = 0
        
        directions = ((0,1), (1,0), (-1,0), (0,-1))
        
        while len(fresh) > 0:
            
            infected = set()
            
            for rot in rotten:

                i, j = rot
                for d in directions:
                    next_i, next_j = d
                    next_i += i
                    next_j += j
                    
                    if (next_i, next_j) in fresh:
                        fresh.remove((next_i, next_j))
                        infected.add((next_i, next_j))
                        
            if len(infected) == 0:
                return -1
            
            minutes += 1
            rotten = infected
            
        return minutes