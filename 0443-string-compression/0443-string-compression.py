class Solution:      
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        
        while i < len(chars):
            grp_len = 1
            while (i+grp_len) < len(chars) and chars[i+grp_len]==chars[i]:
                 grp_len+=1
            
            chars[res] = chars[i]
            res+=1
            if grp_len > 1:
                str_rep = str(grp_len)
                chars[res:res+len(str(str_rep))] = list(str_rep)
                res+= len(str_rep)
        
            i+=grp_len
        
        return res
        
                
                    
                    
                
                
        