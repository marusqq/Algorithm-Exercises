class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        s = ''.join([i for i in s if i.isalpha() or i.isnumeric()])
        s = s.lower()

        could_be_palindome = False
        if len(s) in [0, 1]:
            could_be_palindome = True

        if len(s) % 2:
            middle = len(s) // 2 + 1
            first_word_end = middle - 1
            second_word_start = middle
            #print(first_word_end, second_word_start, 'nelyginis')
            
        else:
            first_word_end = len(s) // 2 
            second_word_start = len(s) // 2
            #print(first_word_end, second_word_start, 'lyginis')

        
        first_word = self.cutWord(s, 0, first_word_end)
        second_word = self.cutWord(s, second_word_start, (len(s)), reverse = True)
        print('checking', first_word, second_word)

        if first_word == second_word and ((len(first_word) != 0 and len(second_word) != 0) or could_be_palindome):
            return True
        else:
            return False


    def cutWord(self, word, start, finish, reverse = False):
        if reverse:
            return word[start:finish][::-1]
        else:
            return word[start:finish] 

ans = Solution()
palindrome = "0P"
print(ans.isPalindrome(palindrome))