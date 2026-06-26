class Solution:

    def can_koko_eat_all_banana(self,piles,speed,h):
        total_hour=0
        for i in piles:
            total_hour=total_hour+(i+speed-1)//speed
        return total_hour<=h
           

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        k=piles[0]
        while(l<=r):
            #speed of koko to eat banana's
            mid=(l+r)//2 
            canEatBanana=self.can_koko_eat_all_banana(piles,mid,h)
            if canEatBanana:
                k=mid
                r=mid-1
            else:
                l=mid+1

        
        return k