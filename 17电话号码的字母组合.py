class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        length = len(digits)
        if length == 0:
            return []
        #将2-9数字对应的字母放在字典中，方便访问
        def get_num2char_dict():
            n = 0
            num2char = dict()
            for i in range(2,10):
                tmp = (n+4) if (i == 7 or i == 9) else (n+3) # 7和9有四个字母
                tmp_list = []
                for j in range(n, tmp):
                    tmp_list.append(chr(j + ord('a')) )
                num2char[str(i)] = tmp_list
                n = tmp
            return num2char
        num2chr = get_num2char_dict()
        ret_list = []   
        def findCombination(digits, index, s):
            if index == length:
                ret_list.append(s)
                return
            letters = num2chr[digits[index]]
            for letter in letters:
                findCombination(digits, index + 1, s + letter)
            return
        findCombination(digits, 0, '')
        return ret_list
