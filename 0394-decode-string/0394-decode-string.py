class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ''
        i = 0
        val = ''
        while i<len(s):
            if ord('0')<=ord(s[i])<=ord('9'):
                val+=s[i]
            elif s[i]=='[':
                 stack.append(int(val))
                 stack.append("[")
                 val=''
            elif ord('a')<=ord(s[i])<=ord('z'):
                stack.append(s[i])
            elif s[i]==']':
                tmp = ''
                while stack and stack[-1]!='[':
                    tmp = stack[-1]+tmp
                    stack.pop()
                
                stack.pop()
                c = stack.pop()
               
                if stack:
                    stack.append(c*tmp)
                else:
                     res+=c*tmp
            i+=1
            #print(stack,res)
        return res+''.join(stack)            
                   