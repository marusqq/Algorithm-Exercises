class Solution:
    def longestPalindrome(self, s: str) -> int:
        first = []
        length = 0
        for letter in s:
            if letter not in first:
                first.append(letter)
                pass
            else:
                first.remove(letter)
                length += 2
        
        if len(first) > 0:
            print('first is not none')
            length += 1

        return length

ans = Solution()
palindrome = "bb"
print(ans.longestPalindrome(palindrome))