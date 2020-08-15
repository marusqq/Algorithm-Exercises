class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        intervals.sort(key=lambda x: x[1])
        
        answer = 0
        prev = intervals[0]
        
        for i in range(1, len(intervals)):
            if prev[1] > intervals[i][0]:
                answer += 1
            else:
                prev = intervals[i]
        
        return answer

intervals = [[1,2],[2,3],[3,4],[1,3]]
ans = Solution()
ans.eraseOverlapIntervals(intervals = intervals)
        