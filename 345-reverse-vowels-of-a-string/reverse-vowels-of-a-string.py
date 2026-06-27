class Solution:

    def isVowel(self,letter):
        letter=letter.lower()
        if letter == "a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
            return True
        else:
            return False

    def reverseVowels(self, s: str) -> str:
        s=list(s)
        i=0
        j=len(s)-1
        while i<j:
            if not self.isVowel(s[i]):
                i+=1
            elif not self.isVowel(s[j]):
                j-=1
            else:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return "".join(s)
