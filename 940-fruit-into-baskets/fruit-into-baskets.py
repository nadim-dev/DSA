class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        low=0
        high=0
        n=len(fruits)
        result=float("-inf")
        dict={}
        while high < n:
            fruit=fruits[high]
            if fruit not in dict:
                dict[fruit]=1
            else:
                dict[fruit]+=1

            if len(dict) <= 2:
                max_fruit=high-low+1
                result=max(result,max_fruit)
            
            while len(dict) > 2:
                fruit=fruits[low]
                dict[fruit]-=1
                if dict[fruit] == 0:
                   del dict[fruit]
                low+=1
            high+=1
        return result