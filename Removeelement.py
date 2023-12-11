class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        j=0
        for v in nums:
            if v!=val:
                nums[j] = v
                j+=1
        return j


        
        