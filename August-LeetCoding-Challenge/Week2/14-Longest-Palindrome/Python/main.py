from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        word_list = list(s)
        word_list.sort()
        print(word_list)
        length = 0
        last_letter = ''
        for i in range(0, len(word_list)):
            if word_list[i] == last_letter:
                print(word_list, 'i', word_list)
                length += 2
                i += 1
            try:
                last_letter = word_list[i]
            except:
                break

            
        # for letter in s:
        #     if letter not in first:
        #         first.append(letter)
        #         pass
        #     else:
        #         first.remove(letter)
        #         length += 2
        
        # if len(first) > 0:
        #     length += 1

        return length
        

ans = Solution()
palindrome = "abccccdd"
print(ans.longestPalindrome(palindrome))