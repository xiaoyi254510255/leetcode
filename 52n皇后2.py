class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        self.sort_n = 0
        
        self.n = n
        self.col = [False for _ in range(n)]
        self.dia1 = [False for _ in range(2 * n - 1)]
        self.dia2 = [False for _ in range(2 * n - 1)]
        self.search(n , 0)
        return self.sort_n
        

    def search(self, n, index):
        if n == index:
            self.sort_n += 1
            return
            
        for i in range(n):
            if (not self.col[i]) and (not self.dia1[ i + index]) and (not self.dia2[index - i + n -1]):
                self.col[i] = True
                self.dia1[i + index] = True
                self.dia2[index - i + n -1] = True
                self.search(n , index + 1)
                self.col[i] = False
                self.dia1[i + index] = False
                self.dia2[index - i + n -1] = False
        return
