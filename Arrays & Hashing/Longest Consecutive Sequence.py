class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Question Link: https://leetcode.com/problems/longest-consecutive-sequence/
        Intution: To avoid redundant iterations, the list nums is converted into a set.It iterates through each element in the set.
        For each element, it checks if the previous element (num - 1) exists in the set. If not, it signifies the start of a new consecutive sequence.
        It then iterates forward to find consecutive elements and counts them.
        The function keeps track of the maximum count encountered, which represents the length of the longest consecutive sequence and return the max value.
        """
        # To avoid duplicate iterations, convert nums to a set
        nums_set = set(nums)
        max_count = 0

        for num in nums_set:
            val = num - 1
            # If the previous element does not exist, it can't be part of the longest sequence
            if val not in nums_set:
                val = num
                count = 0
                # Check if val exists in nums_set, increment the counter
                while val in nums_set:
                    count += 1
                    val += 1
                max_count = max(max_count, count)

        return max_count
