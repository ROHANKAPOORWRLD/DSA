class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Question Link: https://leetcode.com/problems/two-sum/
        Intution: It utilizes a dictionary, num_index_map, to store each number along with its index in the dict.
        It iterates through the list, calculating the complement of each number with respect to the target.
        If the complement exists in the dictionary, the function returns the indices of the current number and its complement,
        which sum up to the target. If no solution is found after iterating through the list,
        the function returns [-1, -1] as an indicator of failure to find such numbers.
        """
        # Creates a dictionary to map numbers to their indices
        num_index_map = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_index_map:
                # Return the indices of the two numbers that sum up to the target
                return [num_index_map[complement], index]
            # Update the dictionary with the current number and its index
            num_index_map[num] = index
        # If no solution is found, return [-1, -1]
        return [-1, -1]
