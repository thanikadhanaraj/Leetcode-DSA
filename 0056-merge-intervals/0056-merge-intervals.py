from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Handle edge case where the list is empty
        if not intervals:
            return []
        
        # 1. Sort the intervals by their start times
        intervals.sort(key=lambda x: x[0])
        
        # Initialize the result array with the first interval
        merged = [intervals[0]]
        
        # 2. Iterate through the remaining intervals
        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            last_merged_end = merged[-1][1]
            
            # If the current interval overlaps with the last merged one
            if current_start <= last_merged_end:
                # Merge them by updating the end time to the maximum value
                merged[-1][1] = max(last_merged_end, current_end)
            else:
                # No overlap, safely append the current interval to the list
                merged.append(intervals[i])
                
        return merged
