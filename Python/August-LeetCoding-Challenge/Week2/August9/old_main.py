class Solution:
    def orangesRotting(self, grid):
        print(grid)
        for line in grid:
            print(line)
            #for square in line:
        
        minutes = 0
        locs = dict()
 
        
        while True:
            
            ans, locs = self.update(grid, locs)
            
            if ans[0] == 'error':
                return ans[1]

            break_loop = self.rot(grid, locs) 
            if break_loop:
                break

            minutes += 1

        return minutes

    def rot(self, grid, locs):

        rotters = locs[2]
        add_after = []
        remove_after = []
        print('ROTTERS', rotters)
        for i in range(len(rotters)):
            print('i', i)
            #for loc in rotters:

            remove_after.append(rotters[i])

            try:
                if self.get_orange(grid, rotters[i][0], rotters[i][1] - 1) == 1 and rotters[i][0] >= 0 and rotters[i][1] - 1 >= 0:
                    self.change_orange(grid, rotters[i][0], rotters[i][1] - 1, 2)
                    add_after.append([rotters[i][0] ,rotters[i][1] - 1])
            except:
                pass
        
            try:
            
                if self.get_orange(grid, rotters[i][0], rotters[i][1] + 1) == 1 and rotters[i][0] >= 0 and rotters[i][1] + 1 >= 0:
                    self.change_orange(grid, rotters[i][0], rotters[i][1] + 1, 2)
                    add_after.append([rotters[i][0], rotters[i][1] + 1])
            except:
                pass

            try:
            
                if self.get_orange(grid, rotters[i][0] - 1, rotters[i][1]) == 1 and rotters[i][0] - 1 >= 0 and rotters[i][1] >= 0:
                    self.change_orange(grid, rotters[i][0] - 1, rotters[i][1], 2)
                    add_after.append([rotters[i][0] - 1, rotters[i][1]])
            except:
                pass

            try:
            
                if self.get_orange(grid, rotters[i][0] + 1, rotters[i][1]) == 1 and rotters[i][0] + 1 >= 0 and rotters[i][1] >= 0:
                    self.change_orange(grid, rotters[i][0] + 1, rotters[i][1], 2)
                    add_after.append([rotters[i][0] + 1, rotters[i][1]])
            except:
                pass

        print(locs)
        for line in grid:
            print(line)

        if len(add_after) <= 0:
            return True
        
        else:
            for new_rot in add_after:
                self.add_to_dict(locs, 2, new_rot)
        
            return False

    def add_to_dict(self, dict, key, value):
        try:
            dict[key].append(value)
        except:
            dict[key] = [value]

    def change_orange(self, grid, x, y, value):
        grid[y][x] = value
        return

    def get_orange(self, grid, x, y):
        try:
            return grid[y][x]
        except:
            return None


    def update(self, grid, locs):
        
        fresh_count = 0
        rotten_count = 0

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    fresh_count += 1
                    self.add_to_dict(locs, 1, [y,x])
                    
                
                elif grid[y][x] == 2:
                    rotten_count += 1
                    self.add_to_dict(locs, 2, [y,x])
                   
        if fresh_count == 0:
            return ['error', 0]
        
        if rotten_count == 0:
            return ['error', -1]

        return [fresh_count, rotten_count], locs

            

#grid = [[0,2]]
grid = [[2,1,1],[1,1,0],[0,1,1]]
ans = Solution()
print("Minutes:", ans.orangesRotting(grid = grid))