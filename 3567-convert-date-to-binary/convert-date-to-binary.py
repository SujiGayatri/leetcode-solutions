class Solution:
    def convertDateToBinary(self, date: str) -> str:
        res=date.split("-")
        nres=[]
        for i in res:
            nres.append(bin(int(i))[2:])
        return "-".join(nres)
