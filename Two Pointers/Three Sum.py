from typing import List


class Solution:
    """
    Question Link: https://leetcode.com/problems/3sum/
    Intuition: It first sorts the list to efficiently apply the two-pointer approach.
    While iterating, it skips duplicate elements by checking if the current element is equal to the previous one.
    For each unique element nums[i], it initializes two pointers, j and k, using a two-pointer approach.
    If the sum equals zero, it adds the triplet [nums[i], nums[j], nums[k]] to the result list and moves pointers j and k accordingly.
    It also skips duplicate elements for j to avoid redundant solutions.
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the list to apply two-pointer approach efficiently
        res = []

        # Iterate through the list
        for i in range(len(nums)):
            
            # All nums are greater than 0 so sum can't be zero
            if nums[i] > 0:  # Optimization Step
                break

            # Skip duplicate elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize two pointers: j and k
            j = i + 1
            k = len(nums) - 1

            # Apply two-pointer approach
            while j < k:
                # If the sum of three elements is zero, add them to the result list
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # Skip duplicate elements for j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                # If the sum is greater than zero, decrement k
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                # If the sum is less than zero, increment j
                else:
                    j += 1

        return res
