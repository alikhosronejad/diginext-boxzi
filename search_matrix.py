def search_matrix(matrix, target):
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Binary search to find the row where target might be located
    left, right = 0, rows - 1
    while left <= right:
        mid = left + (right - left) // 2
        if matrix[mid][0] <= target <= matrix[mid][cols - 1]:
            # Found potential row, now perform binary search in this row
            row = matrix[mid]
            left_row, right_row = 0, cols - 1
            while left_row <= right_row:
                mid_row = left_row + (right_row - left_row) // 2
                if row[mid_row] == target:
                    return True
                elif row[mid_row] < target:
                    left_row = mid_row + 1
                else:
                    right_row = mid_row - 1
            return False
        elif target < matrix[mid][0]:
            right = mid - 1
        else:
            left = mid + 1
    
    return False

# Example usage:
matrix = [
    [1, 3, 5],
    [7, 8, 10],
    [12, 15, 18]
]
target = 8
print(search_matrix(matrix, target))  # Output: True
