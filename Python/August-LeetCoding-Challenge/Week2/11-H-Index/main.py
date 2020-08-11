class Solution:
    def hIndex(self, citations):
        citations.sort(reverse = True)
        # print(citations)
        ret = 0
        for i, cit in enumerate(citations, 1):
            if cit >= i:
                ret = i
        return ret

citations = [3,0,6,1,5]
ans = Solution()
ans.hIndex(citations)

        