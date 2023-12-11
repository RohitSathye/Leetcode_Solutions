class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = 0
        for i in range(0,len(digits)):
            num = num + digits[i]*pow(10,len(digits)-1-i)
        num = num + 1
        res = [int(x) for x in str(num)]
        return res