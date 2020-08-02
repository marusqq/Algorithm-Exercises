class Solution:

    def reverse(self, list, start, finish) -> list:
        if start is None and finish is None:
            return list[::-1]
        elif start == 0:
            return list[start:finish][::-1] + list[finish:]
        else:
            return list[:start] + list[start:finish][::-1]



    def rotate(self, nums, k: int) -> None:

        length_num = len(nums)
        k = k % length_num

        nums = self.reverse(nums, None, None)
        nums = self.reverse(nums, 0, k - 1)
        nums = self.reverse(nums, k, length_num)

        return nums

ans = Solution()
list_of_num = [1,2,3,4,5]
ans.rotate(list_of_num, 1)