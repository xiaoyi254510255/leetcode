class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        num_dict = {nums[k]:k for k in range(length)}
        
        for i in range(length):
            if (target-nums[i]) in num_dict:
                if i == num_dict[target-nums[i]]:
                    continue
                if nums[i] == nums[num_dict[target-nums[i]]]:
                    for j in range(i+1,length):
                        if nums[j] == nums[i]:

                            return [i,j]
                else:
                    return [i,num_dict[target-nums[i]]]
