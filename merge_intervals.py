def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort the intervals based on the starting point
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged[-1]
        
        # Check if there is an overlap
        if current[0] <= last_merged[1]:
            # Merge the two intervals
            merged[-1] = (last_merged[0], max(last_merged[1], current[1]))
        else:
            # No overlap, add the current interval to the list
            merged.append(current)

    return merged

# Example usage:
input_intervals = [(1, 3), (2, 6), (8, 10)]
output = merge_intervals(input_intervals)
print(output)  # Output: [(1, 6), (8, 10)]
