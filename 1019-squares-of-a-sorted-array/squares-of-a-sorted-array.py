class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
             
          result=[]
          positive_arr=[]
          negative_arr=[]
          for i in range(0,len(nums)):
            if nums[i]<0:
               negative_arr.append(nums[i])
            else:
              positive_arr.append(nums[i])
                    
          positive_arr=list(map(lambda x:x**2,positive_arr))
          negative_arr=list(map(lambda x:x**2,negative_arr))
          negative_arr.reverse()

          if len(negative_arr)==0:
            return positive_arr
          elif len(positive_arr)==0:
            return negative_arr
          else:
            i=0
            j=0
            
            while i<len(positive_arr) and j<len(negative_arr):
              if positive_arr[i]<negative_arr[j]:
                result.append(positive_arr[i])
                i+=1
              else:
                result.append(negative_arr[j])
                j+=1
            
            while i<len(positive_arr):
              result.append(positive_arr[i])
              i+=1
            while j<len(negative_arr):
              result.append(negative_arr[j])
              j+=1
          
            return result