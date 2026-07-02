class Solution(object):
    def concatWithReverse(self, nums):
        n=len(nums)
        rev=nums[::-1]
        b=[0]*(2*n)
        for i in range(n):
            b[i]=nums[i]
            b[i+n]=rev[i]
        return b



        """
        :type nums: List[int]
        :rtype: List[int]
        """
        