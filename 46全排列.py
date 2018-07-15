class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length == 0:
            return [[]]
        
        ret_list = []
        
        
        used = [False for i in range(length)]
        def findCombition(nums, index, tmp_list):
            if index == len(nums):
                ret_list.append(tmp_list[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    tmp_list.append(nums[i])
                    used[i] = True
                    findCombition(nums, index + 1, tmp_list)
                    tmp_list.pop()
                    used[i] = False
            return
        findCombition(nums, 0, [])
        return ret_list
