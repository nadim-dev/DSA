class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict={}
        maxlen=0
        
        i=0
        j=0
        
        while(j<len(s)):
          if  s[j] not in dict:
            dict[s[j]]=j
            
              
          else: 
            if(dict[s[j]] >= i):
              i=dict[s[j]]+1
            dict[s[j]]=j
          j+=1
          maxlen=max(maxlen,j-i)      
        return maxlen