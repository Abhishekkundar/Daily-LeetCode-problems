class Solution(object):
    def minOperations(self, boxes):
        ans=[]
        count=0
        for target in range(len(boxes)):
            total=0
            for current in range(len(boxes)):
                if boxes[current]=="1":
                    total+=abs(current-target)
            ans.append(total)
        return ans


        """
        :type boxes: str
        :rtype: List[int]
        """
        