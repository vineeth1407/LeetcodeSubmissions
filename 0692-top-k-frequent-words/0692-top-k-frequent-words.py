import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_dict = dict()
        for i in range(len(words)):
            word_dict[words[i]] = word_dict.get(words[i],0)+1
        
        word_fre = []
        for word,count in word_dict.items():
            heapq.heappush(word_fre,(-count,word))
        
        res = []
        while k:
            res.append(heapq.heappop(word_fre)[1])
            k-=1
        return res
        