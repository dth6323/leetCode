class Solution(object):
    def twoSum(self, nums, targer):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == targer:
                    return i,j


print(Solution().twoSum([3,2,4],6))