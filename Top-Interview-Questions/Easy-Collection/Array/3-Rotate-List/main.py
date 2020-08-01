class Solution:
    def rotate(self, nums, k: int):
        #custom logic goes here

        for k in range(0, k):
            nums = nums[-1:] + nums[:-1]
            #k -= 1

        return nums
    
ans = Solution()
input_nums = [1,2,3,4,5,6,7]
k = 3
print(ans.rotate(input_nums, k))

    