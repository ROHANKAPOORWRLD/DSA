class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
            Question Link: 
            Intuition:It iterates through the string using the pointer j to expand the window.
            For each character, it updates the frequency of the character in max_length and updates max_count with the maximum frequency encountered so far.
            If the length of the window minus the maximum count of a character is greater than k (the number of replacements allowed), it adjusts the window by moving the start pointer i and decrementing the frequency of the character at i.
            It updates the result length with the current window size.
            After iterating through the entire string, it returns the maximum result length, which represents the longest substring with repeating characters that can be replaced to make all characters the same.
        """
        # Initialize an array to store the frequency of characters
        max_length = [0] * 26
        # Initialize variables to track the maximum count of a character, the result length, and the start index of the window
        result = 0
        max_count, i = 0, 0
        
        # Iterate through the string using two pointers, j and i
        for j, char in enumerate(s):
            # Update the frequency of the current character
            max_length[ord(char) - ord('A')] += 1
            # Update the maximum count of a character seen so far
            max_count = max(max_count, max_length[ord(char) - ord('A')])
            
            # If the length of the window minus the maximum count is greater than k, adjust the window
            if (j - i + 1 - max_count) > k:
                max_length[ord(s[i]) - ord('A')] -= 1
                i += 1
            
            # Update the result length with the current window size
            result = max(result, j - i + 1)
        
        # Return the maximum result length
        return result
