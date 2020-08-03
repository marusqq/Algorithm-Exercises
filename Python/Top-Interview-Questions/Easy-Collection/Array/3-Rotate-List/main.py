class Solution:

    def old_reverse(self, list, start, finish) -> list:
        if start is None and finish is None:
            list = list[::-1]
        elif start == 0:
            list = list[start:finish][::-1] + list[finish:]
        else:
            list = list[:start] + list[start:finish][::-1]

    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    def rotate(self, nums, k: int) -> None:

        length_num = len(nums)
        k = k % length_num

        # self.old_reverse(nums, None, None)
        # self.old_reverse(nums, 0, k - 1)
        # self.old_reverse(nums, k, length_num)
        self.reverse(nums, 0, length_num - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, length_num - 1)

        #return nums

# ans = Solution()
# list_of_num = [1,2,3,4,5]
# ans.rotate(list_of_num, 1)