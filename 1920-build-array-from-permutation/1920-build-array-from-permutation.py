class Solution(object):
    def buildArray(self, nums):
        a=[0]*len(nums)
        k=0
        for i in nums:
            a[k]=nums[i] 
            k+=1   
        return a
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        