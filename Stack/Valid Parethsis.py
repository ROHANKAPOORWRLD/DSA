class Solution:
    def isValid(self, s: str) -> bool:
        """
        Question Link: https://leetcode.com/problems/valid-parentheses/
        Intuition:It iterates through the string s character by character.
        If the character is an opening parenthesis ('(', '{', '['), it pushes the corresponding closing parenthesis onto the stack.
        If the character is a closing parenthesis, it checks if it matches the top element of the stack. If they match, 
        it pops the top element from the stack.If the stack is empty or the characters don't match, it returns False immediately, 
        indicating invalid parentheses.After iterating through the entire string, it checks if the stack is empty. 
        If the stack is empty, all parentheses are matched, and it returns True; otherwise, it returns False.
        """
        stack = []  # Initialize a stack to store opening parentheses
        
        # Iterate through the string
        for char in s:
            # If the character is an opening parenthesis, push the corresponding closing parenthesis onto the stack
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            # If the character is a closing parenthesis, check if it matches the top element of the stack
            elif stack and stack[-1] == char:
                stack.pop()  # Pop the top element if it matches
            else:
                return False  # If the stack is empty or the characters don't match, return False
        
        # Return True if the stack is empty (all parentheses matched), otherwise return False
        return len(stack) == 0
