class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        res=[]
        for i in range(left,right+1 ):
            flag = True
            for j in str(i):
                if j !='0':
                    if i % (int(j)) != 0:
                        flag = False
                else:
                    flag = False
                    break   
            if (flag):
                res.append(i)

        return res