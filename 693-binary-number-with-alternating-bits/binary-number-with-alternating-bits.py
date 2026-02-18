class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b=bin(n)[2:]
        cnt=1
        for i in range(len(b)-1):
            if b[i]!=b[i+1]:
                cnt+=1
        return cnt==len(b)