class Solution:
    def titleToNumber(self, s: str) -> int:
        value = 0
        times_to_add = len(s) - 1
        for letter in s:
            letter_value = ord(letter) - 64
            if times_to_add:
                for _ in range(times_to_add):
                    letter_value *= 26
                times_to_add -= 1
                
            value += letter_value
        return value


title = 'YA'
ans = Solution()
print(ans.titleToNumber(title))