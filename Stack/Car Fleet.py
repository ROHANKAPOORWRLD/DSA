from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Question Link: https://leetcode.com/problems/car-fleet/
        Intution:It represents cars as tuples containing their positions and speeds and sorts them based on positions in descending order.
        It then iterates through the sorted cars and calculates the time required for each car to reach the target position.
        It maintains a stack to track the time-to-target for each car and compares the current car's time-to-target with the preceding car's time-to-target.
        If the current car's time-to-target is less than or equal to the preceding car's time-to-target, it indicates that both cars will form a fleet.
        Therefore, it removes the preceding car from the stack to ensure that only the leading car of each fleet remains in the stack.
        After processing all cars, the length of the stack represents the number of car fleets that can reach the target position.
        This approach efficiently determines car fleets by considering the positions and speeds of cars, providing an optimal solution to the problem.
        """
        # Combine positions and speeds into a list of tuples
        cars = [(position[i], speed[i]) for i in range(len(speed))]
        stack = []  # Initialize a stack to track time-to-target for each car
        cars.sort(reverse=True)  # Sort cars by position in descending order
        
        # Iterate through the sorted cars
        for p, s in cars:
            stack.append((target - p) / s)  # Calculate time-to-target for each car
            # If there are at least two cars and the current car's time-to-target is less than or equal to the preceding car's time-to-target
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  # Remove the preceding car from the stack
        
        # The length of the stack represents the number of car fleets
        return len(stack)
