class Solution:
    """
    Question Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
    Intuition:It initializes two pointers, i and j, at the start and end of the list, respectively.
    At each iteration, it calculates the sum of the numbers at pointers i and j.
    If the sum equals the target, it returns the indices of the numbers.
    If the sum is less than the target, it moves pointer i to the right to increase the sum.
    If the sum is greater than the target, it moves pointer j to the left to decrease the sum.
    If no solution is found after iterating through the list, it returns [-1, -1] to indicate the absence of a valid pair.
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize pointers i and j
        i, j = 0, len(numbers) - 1

        # Iterate until i is less than j
        while i < j:
            # Calculate the sum of numbers at pointers i and j
            _sum = numbers[i] + numbers[j]

            # If the sum equals the target, return the indices
            if _sum == target:
                return [i + 1, j + 1]
            # If the sum is less than the target, move pointer i to the right
            elif _sum < target:
                i += 1
            # If the sum is greater than the target, move pointer j to the left
            else:
                j -= 1

        # If no solution is found, return [-1, -1]
        return [-1, -1]
