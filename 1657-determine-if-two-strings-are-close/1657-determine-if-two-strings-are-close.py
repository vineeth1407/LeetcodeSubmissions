class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1 = {}
        dict2 = {}
        if len(word1)!=len(word2):
            return False
        for i in word1:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        for i in word2:
            if i in dict2:
                dict2[i]+=1
            else:
                dict2[i]=1
                
        for key,value in dict1.items():
            if key not in dict2:
                return False
        wv1 = list(dict1.values())
        wv2 = list(dict2.values())
        wv1.sort()
        wv2.sort()
        
        return wv1==wv2
        
        
        