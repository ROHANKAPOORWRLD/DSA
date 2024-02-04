class MinStack:
    """
    Intuition:During each push operation, it pushes the element onto the main stack and 
    updates the minimum stack with the new minimum value.
    For each pop operation, it removes the top elements from both the main stack and the minimum stack.
    """
    def __init__(self):
        # Initialize the main stack and the auxiliary stack to track the minimum elements
        self.stack = []  # Main stack to store elements
        self.min_stack = []  # Auxiliary stack to store minimum elements

    def push(self, val: int) -> None:
        # Push the value onto the main stack
        self.stack.append(val)
        # Update the minimum stack with the new minimum value
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        # Pop the top elements from both stacks
        self.min_stack.pop()  # Remove the corresponding element from the minimum stack
        self.stack.pop()  # Remove the top element from the main stack

    def top(self) -> int:
        # Return the top element of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the top element of the minimum stack, representing the current minimum value in the stack
        return self.min_stack[-1]
