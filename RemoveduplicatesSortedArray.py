class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i,j = 0,1
        while i<=j and j < len(nums):
            if nums[i]==nums[j]:
                j = j + 1
            else:
                nums[i+1]=nums[j]
                i = i + 1
        return i + 1
        
        