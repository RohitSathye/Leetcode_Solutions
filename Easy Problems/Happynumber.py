class Solution:
    def isHappy(self, n: int) -> bool:
        done = set()

        while (n>0):
            temp = 0
            while(n>0):
                i = n%10
                temp = temp + i**2
                n = n//10

            if temp in done:
                return False
            else:
                done.add(temp)
            
            if temp==1:
                return True
            
            n = temp
        
        return False
