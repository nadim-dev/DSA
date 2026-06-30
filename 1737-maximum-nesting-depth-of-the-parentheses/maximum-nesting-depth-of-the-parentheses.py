class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        max_nesting=0
        for i in s:
            if i =="(":
                count+=1
            elif i ==")":
                count-=1
            max_nesting=max(count,max_nesting)
        return max_nesting