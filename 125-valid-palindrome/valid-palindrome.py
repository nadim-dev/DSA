class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=""
        for i in s:
          if "A"<=i<="Z":
            cleaned+=chr(ord(i)+32)
          if "a"<=i<="z":
            cleaned+=i
          if '0'<= i<='9':
            cleaned+=i
        i=0
        j=len(cleaned)-1
        while(i<j):
          if cleaned[i]!=cleaned[j]:
            return False
          i+=1
          j-=1
        return True