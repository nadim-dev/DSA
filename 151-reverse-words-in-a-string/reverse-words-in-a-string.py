class Solution:
    def reverseWords(self, s: str) -> str:
        words=""
        arr=[]
        revstring=""
        for i in range(0,len(s)):
          if(s[i]==" "):
            if(len(words)):
              arr.append(words)
              words=""
          elif(i== len(s)-1):
            words+=s[i]
            arr.append(words)
          else:
            words+=s[i]
  

        i=0
        j=len(arr)-1
        while(i<j):
          arr[i],arr[j]=arr[j],arr[i]
          i+=1
          j-=1
        for i in range(0,len(arr)):
          if(len(arr)-1 == i):
            revstring+=arr[i]
          else:
            revstring+=arr[i]+" "
        return revstring