class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        res = list(s)
        for i in range(len(s)):
            if s[i]=='(':
                st.append(i)
            elif s[i]==')':
                if not st:
                    res[i]=''
                else:
                    st.pop()
        
        while st:
            i = st.pop()
            res[i]=''
        
        return ''.join(res)
        