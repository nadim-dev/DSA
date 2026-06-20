class Solution:

    def sortString(self,s):
            list1=list(s)
            list1.sort()
            return "".join(list1)



    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in range(0,len(strs)):
            sortedString=self.sortString(strs[i])
            if sortedString not in dict:
                dict[sortedString]=[strs[i]]
            else:
                dict[sortedString].append(strs[i])

        arr=[]
        for values in dict.values():
            arr.append(values)
        return arr

            


