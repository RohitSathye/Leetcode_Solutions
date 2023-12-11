class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        cols = {}
        count = len(columnTitle)
        temp = 0
        for i in range(65,91):
            cols[chr(i)] = i - 64
        
        if count == 1:
            return cols[columnTitle]
        else:
            for s in columnTitle:
                temp = temp + (pow(26,count-1))*cols[s]
                count -= 1
            return temp
