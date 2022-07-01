class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        
        slow, fast = 0, 0
        while fast < len(intervals):
            start, end = intervals[slow][0], intervals[slow][1]
            
            while fast < len(intervals) and end >= intervals[fast][0]:
                end = max(end, intervals[fast][1])
                fast += 1
            
            res.append([start, end])
            
            slow = fast
            
        return res