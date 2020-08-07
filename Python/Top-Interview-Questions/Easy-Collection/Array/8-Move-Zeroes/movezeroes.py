class Solution:
    def moveZeroes(self, nums):
        insert = 0
        while True:  
            try:
            	nums.remove(0)
            	insert += 1
            	
            except ValueError:
             for _ in range(insert):
             	nums.insert(len(nums), 0)
             break
             
        	    
        	    
ans = Solution()
array = [1,2,3,4,0,6,7]
ans.moveZeroes(array)
        	