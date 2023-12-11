class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        temp = set()

        for i in nums:
            if i in temp:
                return True
            else:
                temp.add(i)
        else:
            return False
      