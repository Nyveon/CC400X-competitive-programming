# Did this one following NeetCode's video
# But not a fan of the tree not being self-balancing...


class ScheduleTree:
    def __init__(self, start, end):
        self.left = None
        self.right = None
        self.start = start
        self.end = end

    def insert(self, start, end):
        current = self
        while True:
            if start >= current.end:
                if not current.right:
                    current.right = ScheduleTree(start, end)
                    return True
                current = current.right
            elif end <= current.start:
                if not current.left:
                    current.left = ScheduleTree(start, end)
                    return True
                current = current.left
            else:
                return False


class MyCalendar:
    def __init__(self):
        self.schedule = None

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.schedule:
            self.schedule = ScheduleTree(startTime, endTime)
            return True

        return self.schedule.insert(startTime, endTime)
