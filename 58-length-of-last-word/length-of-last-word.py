class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        count=0
        for i in range(len(s)-1,-2,-1):
            if i<0:
                return count

            elif(s[i]!=" "):
                count+=1
            
            

            else: 
                return count
            