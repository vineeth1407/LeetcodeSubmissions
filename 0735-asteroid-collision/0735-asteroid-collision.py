class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids: 
            a_exist=True 
            while stack and stack[-1] > 0 > a and a_exist :  # collision! 
                if stack[-1]<abs(a): #  a survive 
                    stack.pop()
                elif stack[-1]==abs(a):  # both killed
                    stack.pop()
                    a_exist=False
                else:    # top one survive
                    a_exist=False
            if a_exist:
                stack.append(a)

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
            
        