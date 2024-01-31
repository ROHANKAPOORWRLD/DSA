class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Question Link: https://leetcode.com/problems/valid-anagram/
        Intution:The code first checks if the lengths of both strings are equal, as an anagram requires the same number of characters.
        It then creates a dictionary, char_Freq, to store the frequency of characters in both strings. It iterates over each character in the strings,
        incrementing the count for characters in s and decrementing for characters in t. Finally, it verifies if all character frequencies
        are zero using length of set, returning True if so, and False otherwise.
        """
        # Check if length is not equal it can't be Valid Anagram
        if len(s) != len(t):
            return False

        # To store the freq of the characters
        char_Freq = {}

        # To iterate over every character in the string
        for index in range(len(s)):
            char_Freq[s[index]] = char_Freq.get(s[index], 0) + 1
            char_Freq[t[index]] = char_Freq.get(t[index], 0) - 1

        # If Freq of all characters is 0 len of set should be 1 as it should have only 0 as value else False
        return True if len(set(char_Freq.values())) == 1 else False
