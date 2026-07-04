class Solution(object):
    def buildArray(self, nums):
        a=[0]*len(nums)
        for i in range(len(nums)):
            a[i]=nums[nums[i]]
        return a
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        