class Solution:
    
    def get_count(self,vowel_dict):
        c =0
        for key,value in vowel_dict.items():
            c+=value
        return c
    
    
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        vowel_dict= {"a":0,"e":0,"i":0,"o":0,"u":0}
        for i in range(k):
            if s[i] in vowel_dict:
                vowel_dict[s[i]]+=1
        
        res = max(res,self.get_count(vowel_dict))
        
        for i in range(k,len(s)):
            if s[i-k] in vowel_dict:
                vowel_dict[s[i-k]]-=1
            if s[i] in vowel_dict:
                vowel_dict[s[i]]+=1
                res = max(res,self.get_count(vowel_dict))
        return res
            
            
            
        