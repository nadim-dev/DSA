class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        newStr=""
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]]=1
            else:
                freq[s[i]]+=1
        
        freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        for key,value in freq:
            newStr+=key*value
        return newStr