class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Question Link: 
        Intuition:It iterates through t to populate char_freq_t.
        It iterates through s using a sliding window approach, with pointers i and j defining the window.
        For each character encountered, it updates char_freq_s and checks if the character is required from t and if its frequency matches.
        If all characters from t are found in the window, it shrinks the window from the left until the requirement is met.
        During this process, it updates min_length and sub_str accordingly.
        After iterating through s, it returns the resulting substring that contains all characters from t or an empty string if no such substring exists.
        """
        # Create a defaultdict to store the frequency of characters in t
        char_freq_t = collections.defaultdict(int)
        for char in t:
            char_freq_t[char] += 1
        
        # Initialize variables to track the characters needed and characters available
        need = len(char_freq_t)
        have, i = 0, 0
        
        # Initialize variables to track the minimum length of the substring and the resulting substring
        min_length = len(s)
        sub_str = ''
        
        # Create a defaultdict to store the frequency of characters in the current window
        char_freq_s = collections.defaultdict(int)
        
        # Iterate through s using a sliding window approach
        for j, char in enumerate(s):
            char_freq_s[char] += 1
            
            # Update the count of characters available if the current character is in t and its frequency matches
            if char_freq_t[char] != 0 and char_freq_t[char] == char_freq_s[char]:
                have += 1
            
            # Shrink the window if all characters in t are found in the current window
            while have == need:
                # Update the minimum length and the resulting substring
                min_length = min(min_length, j - i + 1)
                if j - i + 1 == min_length:
                    sub_str = s[i:j + 1]
                
                # Remove the leftmost character from the window
                char_freq_s[s[i]] -= 1
                
                # Update the count of characters available if the removal breaks the requirement
                if char_freq_s[s[i]] < char_freq_t[s[i]]:
                    have -= 1
                i += 1
        
        return sub_str
