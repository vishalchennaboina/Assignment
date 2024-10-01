def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged[-1]
        # Check  overlap
        if current[0] <= last_merged[1]:
            # Merge 
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged.append(current)

    return merged

#Example
intervals1 = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals1)) 

intervals2 = [[1,4],[4,5]]
print(merge_intervals(intervals2))