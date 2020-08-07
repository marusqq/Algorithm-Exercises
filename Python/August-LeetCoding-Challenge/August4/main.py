import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        
        ans = math.log(num, 4)
        
        if round(ans) == ans:
            return True
        else:
            return False