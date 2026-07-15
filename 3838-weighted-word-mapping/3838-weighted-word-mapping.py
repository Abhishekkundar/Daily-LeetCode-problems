class Solution(object):
    def mapWordWeights(self, words, weights):
        
        ans=[]
        for word in words:
            total=0
            for _ in word:
                index=ord(_)-ord('a')
                total+=weights[index]
                num=total%26
                
            ans.append(chr(ord('z')-num))
            print(ans)
        print(ans)
        return "".join(ans)
            
                
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        