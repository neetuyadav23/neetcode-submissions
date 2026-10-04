class Solution:
    def isPalindrome(self, s: str) -> bool:
        # study functions n their TC - strip, replace , isalnum()

        s="".join(char.lower() for char in s if char.isalnum())

        s_copy=s[::-1]
        s_copy=s_copy.lower()
        
        if s==s_copy:
            return True
        return False        