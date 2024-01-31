class Solution:
    """
    Question Link: https://www.lintcode.com/problem/659/
    Intuition:For each string in the input list, it appends the length of the string followed by a '#' character and then the string itself.
    The decode method reverses the encoding process. It iterates through the encoded string, extracting the length of each string by locating the '#' character.
    It then reads the substring of the encoded string based on the extracted length and appends it to the list of decoded strings.
    Using delimeter '#' if length is greater than 10 and string contains numeric values so delimeter will tell exactly where to stop. 
    """
    def encode(self, strs: List[str]) -> str:
        # Initialize an empty string to store the encoded string
        encoded_string = ""
        
        # Iterate through each string in the list
        for s in strs:
            # Append the length of the string followed by "#" and the string itself
            encoded_string += str(len(s)) + "#" + s
        
        # Return the encoded string
        return encoded_string

    def decode(self, encoded_string: str) -> List[str]:
        # Initialize an empty list to store the decoded strings
        decoded_string = []
        i = 0
        
        # Iterate until the end of the encoded string
        while i < len(encoded_string):
            # Set j to i initially
            j = i
            
            # Find the index of "#" in the encoded string
            while encoded_string[j] != "#":
                j += 1
            
            # Extract the length of the string
            length = int(encoded_string[i:j])
            
            # Move the pointer i to the next character after "#"
            i = j + 1
            
            # Calculate the end index of the substring
            j = i + length
            
            # Append the decoded substring to the list
            decoded_string.append(encoded_string[i:j])
            
            # Move the pointer i to the next position after the decoded substring
            i = j + 1
        
        # Return the list of decoded strings
        return decoded_string