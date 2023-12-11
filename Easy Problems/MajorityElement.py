class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        log = {}

        for i in nums:
            if i not in log:
                log[i] = 1
            else:
                log[i] = log[i] + 1
        
        return(max(log.items(), key=lambda k: k[1])[0])
        