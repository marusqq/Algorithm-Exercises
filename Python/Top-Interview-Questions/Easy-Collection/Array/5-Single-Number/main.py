class Solution:
	def singleNumber(self, nums):

		while len(nums) > 0:
			 result = self.try_to_remove(nums[0], nums)
			 if result is not None:
			 	return result
			 	
	def try_to_remove(self, rem, array):
			array.remove(rem)
			try:
				array.remove(rem)
				return None
			except:
				return rem
				
				
ans = Solution()
numbers = [1, 3, 3, 1, 7, 9, 9]
print(ans.singleNumber(numbers))