class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
         sum=0
         result=[]
         for i in range(len(digits)):
             sum+=digits[len(digits)-1-i]* 10**(i)
         sum+=1
         while (sum>0):
             lastDig=sum%10
             result.append(lastDig)
             sum=sum//10
         result.reverse()
         return result
                 
                 

       