class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict={}
        freq={}
        for i in range(len(s)):

            if s[i] not in dict:
                dict[s[i]]=t[i]
            else:
                if dict[s[i]]!=t[i]:
                    return False
            if t[i] not in freq:
                freq[t[i]]=s[i]
            else:
                if freq[t[i]]!=s[i]:
                    return False

        return True