class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        low=0
        high=0
        n=len(fruits)
        result=float("-inf")
        dict={}
        while high < n:
            fruit=fruits[high]
            dict[fruit]=dict.get(fruit,0)+1
            
            while len(dict) > 2:
                fruit=fruits[low]
                dict[fruit]-=1
                if dict[fruit] == 0:
                   del dict[fruit]
                low+=1
                
            max_fruit=high-low+1
            result=max(result,max_fruit)
            high+=1
        return result