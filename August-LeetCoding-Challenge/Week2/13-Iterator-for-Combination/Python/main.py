class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        from itertools import combinations
        self.combs = list(combinations(characters, combinationLength))
        
    def next(self) -> str:
        str_return = self.combs[0]
        self.combs.pop(0)
        return ''.join(str_return)

    def hasNext(self) -> bool:
        return bool(len(self.combs))

ans = CombinationIterator('gkosu', 3)
print(ans.next())
print(ans.next())
print(ans.hasNext())
