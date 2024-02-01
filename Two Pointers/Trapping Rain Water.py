class Solution:
    def trap(self, height: List[int]) -> int:
        """
            Question Link: https://leetcode.com/problems/trapping-rain-water/
            Intuition:
            - At each step, it determines which side (left or right) has a smaller maximum height.
            - If the maximum height from the left (max_left) is smaller or equal to the maximum height from the right (max_right), it processes the left side.
            - It calculates the trapped water based on the difference between the maximum height from the left and the height at the current position (height[left]).
            - It updates the maximum height from the left (max_left) to the maximum of its current value and the height at the current position.
            - It moves the left pointer to the right.
            - Similar steps are followed for the right side
            The loop terminates when the left and right pointers meet.
            After traversing all blocks, the method returns the total trapped water.
        """
        # Initialize variables to track the maximum height on the left and right sides
        max_left, max_right = 0, 0
        # Initialize variable to track the total trapped water
        max_height = 0
        # Initialize pointers for the left and right ends of the array
        left, right = 0, len(height) - 1

        # Iterate until the pointers meet
        while left <= right:
            # Determine which side (left or right) has a smaller maximum height
            if max_left <= max_right:
                # Calculate the trapped water based on the maximum height from the left
                max_height += max(0, max_left - height[left])
                # Update the maximum height from the left
                max_left = max(max_left, height[left])
                # Move the left pointer to the right
                left += 1
            else:
                # Calculate the trapped water based on the maximum height from the right
                max_height += max(0, max_right - height[right])
                # Update the maximum height from the right
                max_right = max(max_right, height[right])
                # Move the right pointer to the left
                right -= 1

        # Return the total trapped water
        return max_height