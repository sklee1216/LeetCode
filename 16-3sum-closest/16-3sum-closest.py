class Solution:
    def threeSumClosest(self, nums, target):
        n = len(nums)
        nums.sort()
        sub = 1e9
        ans = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            left = i + 1
            right = n - 1
            
            while right > left:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return total
                if abs(total-target) < abs(ans-target):
                    ans = total
                if total < target:
                    left += 1
                else:
                    right -= 1
        return ans
                    
