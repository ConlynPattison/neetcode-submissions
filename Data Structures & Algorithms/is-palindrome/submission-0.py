class Solution:
    def isPalindrome(self, s: str) -> bool:
        # case insensitive
        # ignore non-alphanumeric (special characters)

        # sanitize the input to consist of only (A-Z, a-z, 0-9)
        s_clean = "".join(char for char in s if char.isalnum())
        s_clean = s_clean.lower()
        
        return s_clean == s_clean[::-1]