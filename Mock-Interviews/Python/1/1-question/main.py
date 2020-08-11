from itertools import permutations

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        value = 0
        for i in range(len(tiles)):
            perm = set(permutations(tiles, i+1))
            value += len(perm)        
        return value

    
ans = Solution()
print(ans.numTilePossibilities('AAABBC'))
        