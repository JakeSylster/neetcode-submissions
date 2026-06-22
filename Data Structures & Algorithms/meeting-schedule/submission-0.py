"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

#Couldn't solve, video explaination use, Solved without looking next day
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.start)

        for i in range(1,len(intervals)):
            obj1 = intervals[i-1]
            obj2 = intervals[i]

            if obj1.end > obj2.start:
                return  False
        
        return True