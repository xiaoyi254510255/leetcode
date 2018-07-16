class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.length = len(candidates)
        self.candidates = candidates
        if self.length == 0:
            return [[]]
        
        self.ret_list = []
        self.getCombinations(0, target, [])
        return self.ret_list
        
        
    def getCombinations(self, index, target, tmp_list):
        if target == 0:
            self.ret_list.append(tmp_list[:])
            return
        
        for i in range(index, self.length):
            if target >= self.candidates[i]:
                tmp_list.append(self.candidates[i])
                self.getCombinations(i, target-self.candidates[i], tmp_list)
                tmp_list.pop()
                
        return  
