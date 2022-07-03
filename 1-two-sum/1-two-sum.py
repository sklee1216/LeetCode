class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, num in enumerate(nums):
            
            remainder = target-num
            
            if remainder in hash_map:
                return hash_map[remainder], index
            else:
                hash_map[num] = index