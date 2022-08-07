class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leads, self.times, votes = [], times, Counter()
        #keep count of each persons vote then register leader for each time
        leader = -1
        for p in persons:
            votes[p] += 1
            if votes[p] >= votes[leader]: 
                leader = p
            self.leads.append(leader)

    def q(self, t: int) -> int:
        #binary search on times to find it in log(n) time and map it to leaderss array
        l, r = 1, len(self.times)
        while l < r:
            mid = (r + l) // 2
            if self.times[mid] > t:
                r = mid
            else:
                l = mid + 1
        return self.leads[l - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)