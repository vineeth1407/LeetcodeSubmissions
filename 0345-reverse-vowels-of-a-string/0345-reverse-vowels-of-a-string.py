class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for i in s:
            if i in ['a','e','i','o','u','A','E','I','O','U']:
                vowels.append(i)
        
        res = ''
        c=0
        rev = vowels[::-1]
        for i in s:
            if i in ['a','e','i','o','u','A','E','I','O','U']:
                res+=rev[c]
                c+=1
            else:
                res+=i
        return res
            
                
            
            
        
        