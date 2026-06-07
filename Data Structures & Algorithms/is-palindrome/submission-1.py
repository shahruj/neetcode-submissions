class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = clean_string(s)
        
        left = 0
        right = len(s)-1

        while left<=right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        
        return True




    



def clean_string(s):
    return "".join(c.lower() for c in s if c.isalpha() or c.isdigit())
        
