class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Question Link: https://leetcode.com/problems/largest-rectangle-in-histogram/
        Intuition:It iterates through the heights, maintaining a stack of indices and heights of bars.It compares the current height
        with the height of the bar at the top of the stack. If the current height is less than or equal to the height of the bar at
        the top of the stack, it calculates the area of the rectangle formed by the popped bar and updates the maximum
        rectangle area accordingly. After processing all bars, it calculates the areas of the remaining rectangles in the stack
        and updates the maximum rectangle area.
        """
        stack = []  # Initialize a stack to track the indices and heights of the bars
        max_height = 0  # Initialize the maximum rectangle area

        # Iterate through the heights
        for i, height in enumerate(heights):
            start_index = i  # Initialize the start index of the rectangle

            # While the stack is not empty and the height of the current bar is less than or equal to the height of the bar at the top of the stack
            while stack and stack[-1][1] >= height:
                index, h = stack.pop()  # Pop the top of the stack
                # Calculate the area of the rectangle formed by the popped bar
                max_height = max(h * (i - index), max_height)
                start_index = index  # Update the start index

            stack.append((start_index, height))  # Append the current bar to the stack

        # Calculate the remaining rectangles' areas in the stack
        for index, height in stack:
            max_height = max(max_height, height * (len(heights) - index))

        return max_height
