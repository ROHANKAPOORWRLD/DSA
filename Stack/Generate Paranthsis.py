from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Question Link: https://leetcode.com/problems/generate-parentheses/
        Intuition:It utilizes a recursive approach to construct valid combinations by adding open and closed parentheses.
        It maintains a stack to keep track of the current combination being generated.
        It recursively explores all possible combinations by adding open parentheses if the count of open parentheses is less 
        than n and adding closed parentheses if the count of closed parentheses is less than the count of open parentheses.It 
        terminates when the count of closed parentheses equals n, indicating a complete valid combination, and appends the combination
        to the result list.After generating all valid combinations, it returns the list of generated parentheses combinations.
        """
        # Initialize a list to store generated parentheses combinations
        parenthesis = []
        stack = []
        
        # Define a recursive function to generate valid parentheses combinations
        def parenthesisGenerator(open, closed):
            # Base case: if the number of closed parentheses equals n, add the current combination to the result list
            if closed == n:
                parenthesis.append("".join(stack))
            
            # If the number of open parentheses is less than n, add an open parenthesis and recurse
            if open < n:
                stack.append('(')
                parenthesisGenerator(open + 1, closed)
                stack.pop()
            
            # If the number of closed parentheses is less than open parentheses, add a closed parenthesis and recurse
            if closed < open:
                stack.append(')')
                parenthesisGenerator(open, closed + 1)
                stack.pop()
        
        # Start the recursive generation process with 0 open and 0 closed parentheses
        parenthesisGenerator(0, 0)
        
        return parenthesis
