class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Question Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
        Intution: It iterates through the string using the pointer j to expand the window.
        For each character, if it already exists in the set, it removes characters from the start of the substring until it's unique.
        It updates the maximum length of the substring by comparing the current length of the substring (j - i + 1) with max_length.
        Finally, it adds the current character to the set.
        After iterating through the entire string, it returns the maximum length of the substring without repeating characters.
        """
        # Initialize a set to store unique characters in the current substring
        chars = set()
        # Initialize variables to track the maximum length of the substring and the start index of the substring
        max_length, i = 0, 0

        # Iterate through the string using two pointers, j and i
        for j, char in enumerate(s):
            # If the character is already in the set, remove characters from the start of the substring until it's unique
            while char in chars:
                chars.remove(s[i])
                i += 1
            # Update the maximum length of the substring
            max_length = max(max_length, j - i + 1)
            # Add the current character to the set
            chars.add(char)

        # Return the maximum length of the substring
        return max_length
