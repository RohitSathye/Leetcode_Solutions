class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0 and x < 10:
            return True
        if x < 0:
            return False
        unit = x % 10
        print(unit)
        nos = len(list(str(x)))
        first = int(x / pow(10,nos-1))
        print(first)
        if((unit == first) and (x % 11 == 0)):
            return True
        else:
            return False
