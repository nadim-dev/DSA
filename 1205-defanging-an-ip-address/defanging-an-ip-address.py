class Solution:
    def defangIPaddr(self, address: str) -> str:
        newIpAddress=""
        for i in address:
            if(i == "."):
                newIpAddress+="[.]"
            else:
                newIpAddress+=i
        return newIpAddress