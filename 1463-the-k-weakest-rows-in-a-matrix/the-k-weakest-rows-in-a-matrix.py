class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dic={}
        for i in range(len(mat)):
            cnt=0
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    cnt+=1
            dic[i]=cnt
        n_dic=sorted(dic.items(), key=lambda x: x[1])
        # print(n_dic)
        res=[]
        for i in range(k):
            res.append(n_dic[i][0])
        return res