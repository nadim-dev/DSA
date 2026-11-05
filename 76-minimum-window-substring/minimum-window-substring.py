class Solution:

    def minWindow(self, s: str, t: str) -> str:
        m=len(s)
        n=len(t)
        if n > m :
            return ""

        low=0
        high=0
        output_str=""
        result=float("inf")
        need={}
        have={}

        for char in t:
            need[char]=need.get(char,0)+1

        def isConditionSatisfied(have,need):
            for key in need:
                if have.get(key,0)   < need.get(key,0):
                    return False
            return True
        
        while high < m:
            char=s[high]
            have[char]=have.get(char,0)+1
            
            while isConditionSatisfied(have,need):
                length=high-low+1
                if result > length:
                    result=length
                    output_str=s[low:low+length]

                have[s[low]]-=1
                low=low+1


            high=high+1
            if high == m:
                break
        return output_str
