class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
            Question Link: https://leetcode.com/problems/group-anagrams/
            Intuition: It employs a defaultdict with keys as tuples representing the frequency of characters in each string and values as lists of strings. 
            It iterates through all the substrings in strs and calculates the frequency of each character in them. 
            The character frequencies are stored in a tuple to be used as keys in the defaultdict. 
            Strings with the same character frequencies are grouped together under the same key. Finally, the function returns the values of the defaultdict, 
            where each value represents a group of anagrams.
        """
        # Create a defaultdict with keys as frequency tuples and values as lists of strings
        char_freq_map = collections.defaultdict(list)

        # Iterate over all substrings 
        for sub_str in strs:
            # Create a list to count the frequency of each character in the substring
            char_freq = [0] * 26
            for char in sub_str:
                char_freq[ord(char) - ord('a')] += 1

            # Convert the list to a tuple as lists cannot be used as keys in dictionaries
            char_freq_tuple = tuple(char_freq)
            char_freq_map[char_freq_tuple].append(sub_str)
        
        # Return the values of char_freq_map as anagrams are grouped together in values
        return char_freq_map.values()
