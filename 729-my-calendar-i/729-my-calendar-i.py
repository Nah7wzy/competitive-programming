class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        for i in range(len(self.events)):
            if (self.events[i][0] <= start < self.events[i][1]) or (start <= self.events[i][0] and end > self.events[i][0]):
                return False
        self.events.append((start, end))
        self.events.sort()
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)