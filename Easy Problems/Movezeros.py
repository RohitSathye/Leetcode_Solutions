class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        for i in nums:
            if i == 0:
                nums.append(i)
                nums.remove(i)
            else:
                continue