class Solution:
    def threeSum(self, nums):
        n = len(nums)
        if n <= 2: return []
        triplets = []
        
        nums.sort()
        
        for i in range(n-2):
            right = n - 1
            left = i + 1
            while right > left:
                total = nums[i] + nums[right] + nums[left]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    triplets.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
        myset = set(tuple(row) for row in triplets)

        return list(myset)
        

        
