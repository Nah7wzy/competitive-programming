class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        #use line sweep then change keys to a list and perform binary search
        sweeper = defaultdict(int)
        for start, end in flowers:
            sweeper[start] += 1
            sweeper[end + 1] -= 1
            
        blooms = list(sweeper.keys())
        blooms.sort()
        total = 0
        for time in blooms:
            total += sweeper[time]
            sweeper[time] = total
        
        res = [0] * len(persons)
        for i, arrival in enumerate(persons):
            l, r = 0, len(blooms) - 1
            while l <= r:
                mid = (l + r) // 2
                if blooms[mid] > arrival:
                    r = mid - 1
                else:
                    l = mid + 1
            
            res[i] = sweeper[blooms[r]]
            
        return res
        
            