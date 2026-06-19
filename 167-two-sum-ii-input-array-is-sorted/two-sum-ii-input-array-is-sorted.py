class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict={}
        for i in range(0,len(numbers)):
            currentElement=numbers[i]
            rem=target-currentElement
            if rem in dict:
                return [dict[rem]+1,i+1]
            else:
                dict[currentElement]=i