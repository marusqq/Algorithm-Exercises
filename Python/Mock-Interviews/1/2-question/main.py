class Solution:
    def gardenNoAdj(self, N: int, paths):
        connections = dict()

        gardens = {
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0
        }

        flowers = [1,2,3,4]
        flower_index = 1
        output = [1]
        
        for i in range(1,N+1):
            for path in paths:
                if i in path:
                    if path[0] == i:
                        path = path[1]

                    elif path[1] == i:
                        path = path[0]

                    try:
                        connections[i].append(path)

                    except:
                        connections[i] = [path]
            
            for roads in connections[i]:
                if gardens[roads] == 0:
                    gardens[roads] = roads

        return list(gardens.values())


ans = Solution()
N = 4
paths = [[1,2],[3,4]]
print(ans.gardenNoAdj(N, paths))



        