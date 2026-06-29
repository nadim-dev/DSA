class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=""
        base=strs[0]
        for i in range(len(base)):
            for j in range(1,len(strs)):
                word=strs[j]
                if  i==len(word) or base[i]!=word[i]:
                    return result
            result+=base[i]

        return result




