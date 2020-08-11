class Solution:
    def plusOne(self, digits):
    	digit = int("".join(map(str, digits))) + 1
    	return list(map(int, str(digit)))
    
ans = Solution()
digs = [1,3,5,7]
print(ans.plusOne(digs))

    	