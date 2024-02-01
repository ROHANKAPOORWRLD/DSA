class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
            Question Link:
            Intution:It iterates through s1 to calculate the frequency of characters in s1 and initializes the sliding window.
            It iterates through s2 using a sliding window approach.
            For each character in s2, it updates the frequency of the character in char_freq_s2 and adjusts the sliding window if its size exceeds the length of s1.
            It checks if the frequency arrays char_freq_s1 and char_freq_s2 match.
            If they match at any point, it returns True, indicating that s1 is a permutation of a substring in s2.
            If no match is found after iterating through s2, it returns False, indicating that s1 is not a permutation of any substring in s2.
        """
        if len(s1) > len(s2):
            return False
        
        # Initialize arrays to store the frequency of characters in s1 and a sliding window in s2
        char_freq_s1 = [0] * 26
        char_freq_s2 = [0] * 26
        i = 0
        
        # Calculate the frequency of characters in s1
        for char in s1:
            char_freq_s1[ord(char) - ord('a')] += 1
        
        # Iterate through s2 using a sliding window approach
        for j, char in enumerate(s2):
            char_freq_s2[ord(char) - ord('a')] += 1
            
            # Adjust the sliding window
            if j - len(s1) >= 0:
                char_freq_s2[ord(s2[i]) - ord('a')] -= 1
                i += 1
            
            # Check if the frequency arrays match
            if char_freq_s1 == char_freq_s2:
                return True
        
        return False
