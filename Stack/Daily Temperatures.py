class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Question Link: https://leetcode.com/problems/daily-temperatures/
        Intuition:It iterates through the temperatures, maintaining a stack of indices.For each temperature, it compares it with the 
        temperature at the index at the top of the stack.If the current temperature is higher than the temperature at the index at 
        the top of the stack, it calculates the difference in indices, representing the number of days until the warmer temperature,
        and updates the result list accordingly.By using a stack, it ensures that the indices in the stack represent temperatures in 
        non-decreasing order, allowing for efficient determination of days until warmer temperatures.
        """
        # Initialize a list to store the result
        res = [0] * len(temperatures)
        # Initialize a stack to store the indices of temperatures
        stack = []

        # Iterate through the temperatures
        for index, temperature in enumerate(temperatures):
            # While the current temperature is higher than the temperature at the index at the top of the stack
            while stack and temperatures[stack[-1]] < temperature:
                # Pop the index at the top of the stack
                val = stack.pop()
                # Calculate the difference in indices and update the result list
                res[val] = index - val
            # Append the current index to the stack
            stack.append(index)

        return res
