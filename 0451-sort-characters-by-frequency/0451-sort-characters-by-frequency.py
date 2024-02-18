import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        chr_dict = {}
        for i in range(len(s)):
            chr_dict[s[i]]=chr_dict.get(s[i],0)+1
        
        chr_freq = [(value,key) for key,value in chr_dict.items()]
        
        chr_freq.sort(key=lambda x:(x[0],x[1]),reverse=True)
        res = ''
        for i in chr_freq:
            res+=i[1]*i[0]
        return res
        
        