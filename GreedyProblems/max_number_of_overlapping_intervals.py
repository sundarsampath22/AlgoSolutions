class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        sorted_intervals = sorted(points, key=lambda x: x[0])
        num_arrows = 1
        previous_interval = sorted_intervals[0]
        for i in range(1, len(sorted_intervals)):
            current_interval = sorted_intervals[i]
            if not self.overlaps(previous_interval, current_interval):
                num_arrows += 1
                previous_interval = current_interval
            else:
                previous_interval = self.mergeIntervals(previous_interval, current_interval)
        return num_arrows

    def overlaps(self, interval_1, interval_2):
        start_1, end_1 = interval_1
        start_2, end_2 = interval_2
        if start_2 >= start_1 and start_2 <= end_1:
            return True
    
    def mergeIntervals(self, interval_1, interval_2):
        start_1, end_1 = interval_1
        start_2, end_2 = interval_2
        return [max(start_1, start_2), min(end_1, end_2)]