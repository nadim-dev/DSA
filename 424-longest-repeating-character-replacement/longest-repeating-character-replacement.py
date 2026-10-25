class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low=0
        high=0
        n=len(s)
        result=float("-inf")
        freq={}
        while high < n:
            char=s[high]
            freq[char] = freq.get(char, 0) + 1
            lenght=high-low+1
            max_value=max(freq.values())
            diff=lenght-max_value
            while diff > k:
                freq[s[low]]-=1
                if freq[s[low]] == 0:
                    del freq[s[low]]
                low=low+1
                lenght=high-low+1
                max_value=max(freq.values())
                diff=lenght-max_value
            
            result=max(result,lenght)
            high=high+1
            if high == n:
                break
            
        return result
            