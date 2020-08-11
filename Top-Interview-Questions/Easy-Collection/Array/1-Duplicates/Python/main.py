class Solution:
    def removeDuplicates(self, numbers) -> int:

        i = 0
        while i < len(numbers) - 1:
            if numbers[i] == numbers[i+1]:
                numbers.pop(i)
            else:
                i += 1

        #default
        #return len(numbers), numbers

        #accepted
        return len(numbers)
    
ans = Solution()
input_nums = [1,2,3,3,3,3,3,3,4,5,6]

print(ans.removeDuplicates(input_nums))

    