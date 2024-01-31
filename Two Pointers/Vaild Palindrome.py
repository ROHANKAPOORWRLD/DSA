class Solution:
    """
    Question Link: https://leetcode.com/problems/valid-palindrome/
    Intuition:It initializes two pointers, i and j, at the beginning and end of the string, respectively.
    It iterates through the string, moving the pointers towards each other while skipping non-alphanumeric characters keeping i<j in mind.
    At each step, it checks if the characters at the pointers are equal.
    If a mismatch is found, it returns False, indicating that the string is not a palindrome.
    If the iteration completes without finding any mismatches, it returns True, indicating that the string is a palindrome.
    The isAlphaNumeric method checks whether a given character is alphanumeric, which helps in skipping non-alphanumeric characters during palindrome checking.
    """

    def isPalindrome(self, s: str) -> bool:
        # Initialize pointers i and j
        i, j = 0, len(s) - 1
        # Convert the string to lowercase
        s = s.lower()

        # Iterate until i < j
        while i < j:
            # Skip non-alphanumeric characters from the left
            while i < j and not self.isAlphaNumeric(s[i]):
                i += 1
            # Skip non-alphanumeric characters from the right
            while i < j and not self.isAlphaNumeric(s[j]):
                j -= 1
            # Check if characters at pointers i and j are equal
            if s[i] != s[j]:
                return False
            # Move the pointers
            i += 1
            j -= 1

        return True

    def isAlphaNumeric(self, s: str) -> bool:
        # Check if the character is alphanumeric
        return ("a" <= s <= "z") or ("0" <= s <= "9")
