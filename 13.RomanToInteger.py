class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        i = 0
        char_dict = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        ret_num = 0
        while i<s_len:
            if s_len - i >= 2:
                if char_dict[s[i]] < char_dict[s[i+1]]:
                    ret_num += char_dict[s[i+1]]- char_dict[s[i]]
                    i += 2
                else:
                    ret_num += char_dict[s[i]]
                    i += 1
            else:
                ret_num += char_dict[s[i]]
                i += 1
        return ret_num
