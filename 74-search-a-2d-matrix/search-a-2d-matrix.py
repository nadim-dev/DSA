class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        columns=len(matrix[0])
        l=0
        r=rows*columns-1
        while(l<=r):
            mid=(l+r)//2
            i=mid//columns
            j=mid%columns
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                 r=mid-1
            else:
                l=mid+1
        return False


