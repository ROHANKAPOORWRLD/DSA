from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Question Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
        Intuition:It utilizes a stack to store operands and perform arithmetic operations based on the operators encountered.
        It iterates through the tokens and evaluates the expression accordingly.
        For each token, it performs the corresponding operation based on the token ('+', '-', '*', '/').
        If the token is a number, it directly pushes it onto the stack.
        After processing all tokens, it returns the top element of the stack, which represents the result of the RPN expression.
        """
        # Initialize a stack to perform the operations
        stack = []
        
        # Iterate through the tokens
        for token in tokens:
            ans = token  # Default answer is the token itself
            
            # Perform the corresponding operation based on the token
            if token == '*':
                ans = stack.pop() * stack.pop()
            elif token == '+':
                ans = stack.pop() + stack.pop()
            elif token == '/':
                val = stack.pop()
                ans = stack.pop() / val
            elif token == '-':
                val = stack.pop()
                ans = stack.pop() - val
            
            # Convert the answer to an integer and push it onto the stack
            stack.append(int(ans))
        
        # Return the result, which is the top element of the stack
        return stack[-1]
