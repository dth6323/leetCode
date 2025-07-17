class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,j=1,1
        if len(nums) == 0:
            return 0
        if len(nums) ==1:
            return 1
        while i < len(nums):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j+=1
            i+=1
        return j
nums = [1,1]
solution = Solution()
k = solution.removeDuplicates(nums)
print(k)