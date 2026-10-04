class Solution:
    def isPalindrome(self, s: str) -> bool:
        # APPROACH 3--- NOW--> TC = O(n) and SC = O(1) 
        i=0
        j=len(s)-1

        while i <= j:
            while i <= j and not s[i].isalnum():  # used while to handle s="," 
                i+=1             # where both i,j=o=, & i++ will give index error
                
            while i <= j and not s[j].isalnum():
                j-=1             # same her also index error

            if i > j:
                break

            if s[i].lower() == s[j].lower():
                i+=1
                j-=1
            else:
                return False
        return True
        # APPROACH 2 
        '''i=0
        s="".join(char.lower() for char in s if char.isalnum())

        j=len(s)-1 # we calc j after join op because s ki length will decrease
        
        while i <= j:
            if s[i] != s[j]:
                return False

            i+=1
            j-=1

        return True'''
        # APPROACH 1--THIS APPROACH IS OPTIMAL IN TC BUT NOT IN SPACE COMPLEXITY 

        # study functions n their TC - strip, replace , isalnum()

        # TC = O(n) and SC = O(m) → worst case O(n)

        '''s="".join(char.lower() for char in s if char.isalnum())

        s_copy=s[::-1]
        
        if s==s_copy:
            return True
        return False '''       

# char.isalnum() → O(1) for each character
# char.lower() → O(1) for each character
# looping through s → O(n)
# "".join(...) → O(m) to create/copy the cleaned string
# Overall → TC = O(n), SC = O(m)


# s[::-1] → O(m) to reverse/copy the string
# s_copy → O(m) extra space


# s == s_copy → O(m) in worst case to compare
# Extra space → O(1)