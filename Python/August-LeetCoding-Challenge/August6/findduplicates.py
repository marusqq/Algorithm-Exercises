class Solution:
    def findDuplicates(self, nums):
        seen = {}
        dupes = []

        for x in nums:
        	if x not in seen:
        		seen[x] = 1
        	else:
        	       	if seen[x] == 1:
        	       		dupes.append(x)
        	       	seen[x] += 1
        	 	
        return dupes
        
ans = Solution()
array = [3, 7, 7, 9, 7, 2, 3]
print(ans.findDuplicates(array))