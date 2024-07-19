def longest_consecutive(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Check if this number is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Check for the next elements in the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# Example usage:
input_nums = [100, 4, 200, 1, 3, 2]
output = longest_consecutive(input_nums)
print(output)  # Output: 4 (sequence: [1, 2, 3, 4])
