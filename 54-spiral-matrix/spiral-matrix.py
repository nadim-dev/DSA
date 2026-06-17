class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #no of rows
        n=len(matrix)
        #no of columns
        m=len(matrix[0])
        #initialize variable
        rowst=0
        rowend=n-1
        colst=0
        colend=m-1
        ans=[]
        total=n*m
        count=0
        while(count< total):
            #printting first row
            for i in range(colst,colend+1):
                ans.append(matrix[rowst][i])
                count+=1
            
            rowst+=1

            if count==total:
                break

            #printing first column
            for i in range(rowst,rowend+1):
                ans.append(matrix[i][colend])
                count+=1
            colend-=1

            if count==total:
                break

            #printing last row


            for i in range(colend,colst-1,-1):
                ans.append(matrix[rowend][i])
                count+=1

            rowend-=1

            if count==total:
                break

            #printing first  column in reverse manner
            for i in range(rowend,rowst-1,-1):
                ans.append(matrix[i][colst])
                count+=1

            colst+=1

            if count==total:
                break

        return ans
            
