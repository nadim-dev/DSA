class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict={}
        for i in range(0,len(s)):
            currentStr=s[i]
            if currentStr in dict:
                dict[currentStr]+=1  
            else:
                dict[currentStr]=1
        a=True
        for key,value in dict.items():
           if value==1:
            a=False
            return s.index(key)

        if a:
            return -1

            