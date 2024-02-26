class Solution:
    def is_vowel(self,c):
        return c in ['a','e','i','o','u']
    
    def maxVowels(self, s: str, k: int) -> int:
        vowel_count = None
        max_count = 0

        for i in range(0, len(s) - k + 1):
            if vowel_count is None:
                g = 0
                for j in range(i, i + k):
                    if self.is_vowel(s[j]):
                        g += 1
                vowel_count = g
                max_count = vowel_count
            else:
                if self.is_vowel(s[i - 1]):
                    vowel_count -= 1
                if self.is_vowel(s[i + k - 1]):
                    vowel_count += 1
                max_count = max(max_count, vowel_count)
        return max_count

                    
                    
            
        