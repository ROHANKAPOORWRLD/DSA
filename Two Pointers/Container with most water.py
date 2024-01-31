class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Question Link: https://leetcode.com/problems/container-with-most-water/
        Intuition:The area between the two pointers is calculated as the minimum of the heights at the pointers multiplied by the distance between them.
        It updates the max_area variable with the maximum of the current area and the previous maximum area encountered.
        The pointer with the smaller height moves towards the other pointer as moving the pointer with greater height will not yield a larger area.
        """
        i, j = 0, len(height) - 1
        max_area = 0

        while i < j:
            # Calculate the area between the two pointers
            area = min(height[i], height[j]) * (j - i)

            # Update the maximum area if the current area is greater
            max_area = max(max_area, area)

            # Move the pointer with smaller height towards the other pointer
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return max_area
