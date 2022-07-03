class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        nums.sort()
        ans = []
        if n <= 3: return ans

        for i in range(n-3):
            for j in range(i+1,n-2):
                left, right = j + 1, n - 1
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum < target:
                        left += 1
                    elif sum > target:
                        right -= 1
                    else:
                        ans.append([nums[i],nums[j],nums[left],nums[right]])
                        left += 1
                        right -= 1
        myset = set(tuple(row) for row in ans)
        return list(myset)
