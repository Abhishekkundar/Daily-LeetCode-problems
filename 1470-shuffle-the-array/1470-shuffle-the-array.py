class Solution(object):
    def shuffle(self, nums, n):
        a=[0]*len(nums)
        b=0
        for i in range(0,len(nums),2):
            a[i]=nums[b]
            b+=1
            a[i+1]=nums[n]
            n+=1
           
        return a
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        