class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(c.lower() for c in s if c.isalnum())
        i = 0
        j = len(clean) - 1
        while i < j:
            if clean[i]!=clean[j]:
                return False
            i+=1
            j-=1
        return True
        