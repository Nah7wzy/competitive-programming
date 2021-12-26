from typing import Deque


class RecentCounter:

    def __init__(self):
        self.requests=Deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        r=[t-3000, t]
        # count=len(self.requests)
        while self.requests[0]<r[0]:
            self.requests.popleft()
            
        return len(self.requests)