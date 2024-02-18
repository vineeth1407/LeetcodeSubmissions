class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2==1:
            return False
        
        flip ,close,op = 0,0,0
        
        for i in range(len(s)):
            if locked[i]=='0':
                flip+=1
            elif s[i]=='(':
                 op+=1
            elif s[i]==')':
                close+=1
            
            if flip+op <close:
                return False
        flip ,close,op = 0,0,0
        for i in range(len(s)-1,-1,-1):
            if locked[i]=='0':
                flip+=1
            elif s[i]=='(':
                 op+=1
            elif s[i]==')':
                close+=1
            
            if flip+close <op:
                return False
        return True
                
        