class MyCalendar:

    def __init__(self):
        self.schedule = []

    def book(self, start: int, end: int) -> bool:
        if len(self.schedule) == 0:
            self.schedule.append((start, end))
            return True
        for s, e in self.schedule: # i = (x, y)
            if start < e and end > s:
                return False
        self.schedule.append((start, end))
        # self.schedule.sort()
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)