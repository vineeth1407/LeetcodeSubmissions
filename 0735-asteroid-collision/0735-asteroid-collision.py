class Solution:
    def asteroidCollision(self, astr: List[int]) -> List[int]:
        stack = []
        i= 0
        
        while i<len(astr):
            if astr[i]>0:
                stack.append(astr[i])
            else:
                while stack and stack[-1]>0:
                    if stack[-1]< -astr[i]:
                        stack.pop()
                    elif stack[-1] == -astr[i]:
                        stack.pop()
                        break
                    else:
                        break
                
                else:
                    stack.append(astr[i])
            i+=1
        
        return stack
                
        
        
        
        
        
        
        
        
        
        
        
#         for i in range(len(asteroids)):
#             if not stack:
#                 stack.append(asteroids[i])
#             else:
#                  top = stack[-1]
#                  if top * asteroids[i]<0:
#                     if abs(stack[-1])<abs(asteroids[i]):
#                         stack.pop()
#                         stack.append(asteroids[i])
#                     elif abs(stack[-1])==abs(asteroids[i]):
#                         stack.pop()
                    
                    
#                  else:
#                     stack.append(asteroids[i])
        
#         return stack
            
        