class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_dict = dict()
        for i in range(len(arr)):
            if arr[i] in hash_dict:
                hash_dict[arr[i]]+=1
            else:
                hash_dict[arr[i]]=1
        values = set(hash_dict.values())
        return len(values)==len(hash_dict.keys())
        
        