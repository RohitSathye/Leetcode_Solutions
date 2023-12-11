class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        log = {}
        
        for i,n in enumerate(nums):
            if n in log and abs(i-log[n]) <= k:
                return True
                
            else:
                log[n] = i

        return False
        