class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        res = []

        for i in range(0,len(nums)):
            search = target - nums[i]
                        
            if search in mapping:
                return [mapping[search],i]
            
            mapping[nums[i]] = i
            
        return


        
        

            
