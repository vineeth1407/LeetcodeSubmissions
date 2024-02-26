class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i =0
        j =0
        if not s:
            return True
        
        while i<len(s) and j<len(t):
            if s[i]== t[j]:
                if i==len(s)-1:
                    return True
                i+=1
                j+=1
               
            else:
                j+=1
        return False
    