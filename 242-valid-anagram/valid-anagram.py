class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dist={}
        for i in range(0,len(s)):
            if s[i] not in dist:
               dist[s[i]]=1
            else:
               dist[s[i]]+=1
        
        for i in range(0,len(t)):
            if t[i] in dist:
                dist[t[i]]-=1
            else:
                return False
        
        for value in dist.values():
            if value !=0:
               return False
        return True