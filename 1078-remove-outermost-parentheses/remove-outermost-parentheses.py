class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count=0
        result=""
        for ch in s:
            if ch=="(":
                count+=1
                if count>1:
                    result+=ch
            else:
                count-=1
                if count!=0:
                    result+=ch
        return result
            