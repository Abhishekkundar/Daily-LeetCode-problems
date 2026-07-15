class Solution(object):
    def mapWordWeights(self, words, weights):
        
        ans=[]
        for word in words:
            total=0
            for _ in word:
                
                total+=weights[ord(_)-ord('a')]
                num=total%26
                
            ans.append(chr(ord('z')-num))
            
       
        return "".join(ans)
            
                
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        