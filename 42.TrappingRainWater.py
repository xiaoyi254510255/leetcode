class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        if length <= 2:
            return 0
        #解题思路：先求出最大的高度，如果最大高度只有一个，那分别计算左边和右边的雨水和，
        #如果最大高度有多个，计算最左边最大高度左边部分，再计算最右边最大高度右边的部分，中间的部分，只要比最大高度小，都加入
        total = 0
        max_height = max(height)
        max_indexs = []
        for i,h in enumerate(height):
            if h == max_height:
                max_indexs.append(i)
       
        if max_indexs[0] > 1:
            tmp_max = height[0]
            for i in range(max_indexs[0]-1):
                if height[i+1] < tmp_max:
                    total += (tmp_max - height[i+1])
                else:
                    tmp_max = height[i+1]
        if max_indexs[-1] < length - 2:
            tmp_max = height[-1]
            for i in range(length-1,max_indexs[-1],-1):
                if height[i-1] < tmp_max:
                    total +=  (tmp_max - height[i-1])
                else:
                    tmp_max = height[i-1]
        if len(max_indexs) > 1:
            for i in range(max_indexs[0],max_indexs[-1]):
                if height[i] < max_height:
                    total += (max_height - height[i])
        return total
