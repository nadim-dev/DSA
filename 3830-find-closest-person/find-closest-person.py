class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        distXtoZ=abs(z-x)
        distYtoZ=abs(z-y)

        if(distXtoZ<distYtoZ):
            return 1
        elif(distXtoZ>distYtoZ):
            return 2
        else:
            return 0
        