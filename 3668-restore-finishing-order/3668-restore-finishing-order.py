class Solution(object):
    def recoverOrder(self, order, friends):
        friends=set(friends)
        a=[]
        for i in order:
            if i in friends:
                a.append(i)
        return a
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        