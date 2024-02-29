nums = [100,4,200,1,3,2]
def longestConsecutive(nums) -> int:
    # Return 0 if the list is empty
    if not nums:
        return 0


    # Convert the list to a set to remove duplicates and allow for O(1) lookups
    nums = set(nums)
    # Initialize the longest streak to 0
    longest_streak = 0

    # Iterate through each number in the set
    for num in nums:
        # Check if the current number is the start of a sequence
        if num - 1 not in nums:
            # Set the current number as the start of a potential sequence
            current_num = num
            # Initialize the current streak to 1
            current_streak = 1

            # Continue the sequence while consecutive numbers are found
            while current_num + 1 in nums:
                # Move to the next number in the sequence
                current_num += 1
                # Increment the current streak
                current_streak += 1

            # Update the longest streak if the current streak is longer
            longest_streak = max(longest_streak, current_streak)

    # Return the length of the longest consecutive sequence
    return longest_streak
longestConsecutive(nums)