#比较笨的方法
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        if length < 2:
            return True
        
        i = 0
        j = length -1
        s = s.lower()
        char_set = set([chr(i) for i in range(97,123)] + [str(j) for j in range(10)])
        while True:
            while s[i] not in char_set:
                i += 1
                if i > j :
                    return True
            while s[j] not in char_set:
                j -= 1
                if j < i:
                    return True
            
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
            if i >= j:
                return True
#简洁的方法
class Solution2:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(filter(str.isalnum, s.lower()))
        return True if s == s[::-1] else False
