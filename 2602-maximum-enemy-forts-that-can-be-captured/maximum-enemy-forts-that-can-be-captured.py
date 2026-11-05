class Solution:
    def captureForts(self, forts: list[int]) -> int:
        low=0
        maxCaptured=0
        n=len(forts)
        while  forts[low] == 0:
            low=low+1
            if low == len(forts):
                break
          
        high=low
        
        
        while high<n:
            
            if forts[low]!=0 and forts[high]!=0 and forts[low]!=forts[high]:
                  maxCaptured=max(maxCaptured,high-low-1)
                  low=high
            if forts[low] == forts[high]:
                low=high
               
            high=high+1
        return maxCaptured