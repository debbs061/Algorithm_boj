class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = [0] * 26  # Initialize a list of size 26 with all zeros
        for char in s:
            freq[ord(char) - ord('a')] += 1  # Increment the frequency
        for i, char in enumerate(s):
            if freq[ord(char) - ord('a')] == 1:
                return i  # Return the index if frequency is 1
        return -1  # Return -1 if no unique character is found
