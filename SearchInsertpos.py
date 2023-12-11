class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if len(nums) == 1:
                if target < nums[0]:
                    return 0
                else:
                    return 1
            else:                   
                for i in range(0,len(nums)-1):
                    if (target < nums[0]):
                        return 0
                    if (nums[i] < target and target < nums[i+1]):
                        return i + 1
                    else:
                        i = i + 1
        return i + 1
