class Solution(object):
    def minOperations(self, nums, k):
        return sum(nums)%k
        # count=0
        
        # for i in nums:
        #     while i>ans and ans>0:
        #         i-=1
        #         ans-=1
        #         count+=1
        #     if sum(nums)%k==0:
        #         return count
        # return count    
        

        
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        