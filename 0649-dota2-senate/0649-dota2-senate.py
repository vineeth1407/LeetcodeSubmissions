from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad = deque()
        dire = deque()
        
        for i in range(len(senate)):
            if senate[i]=='R':
                rad.append(i)
            else:
                dire.append(i)
        
        i = len(senate)
        while rad and dire:
            if rad[0]<dire[0]:
                dire.popleft()
                rad.popleft()
                rad.append(i)
                i+=1
            else:
                dire.popleft()
                rad.popleft()
                dire.append(i)
                i+=1
        
        
        if rad:
            return 'Radiant'
        else:
            return 'Dire'
                