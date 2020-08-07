class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.wordDict = dict()
        

    def addWord(self, word):
        
        if len(word) in self.wordDict:
            self.wordDict[len(word)].add(word)
        else:
            self.wordDict[len(word)] = set([word])
        
        
    def filter(self, wordPool, index, char = "."):
        if char == ".":
            return wordPool
        
        return [word for word in wordPool if word[index] == char]
        
    def search(self, word):
        
        if len(word) not in self.wordDict:
            return False
        elif word in self.wordDict[len(word)]:
            return True
        
        
        wordPool = list(self.wordDict[len(word)])
        
        for i, char in enumerate(word):
            wordPool = self.filter(wordPool, i, char)
            if wordPool == []:
                return False
            
        return True