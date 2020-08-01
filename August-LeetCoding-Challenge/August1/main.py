class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        
        elif word.islower():
            return True
            
        elif word.istitle() and word[1:].lower(): 
            return True

        else:
            return False

ans = Solution
input_word = 'USA'
print(ans.detectCapitalUse(ans, word = input_word))