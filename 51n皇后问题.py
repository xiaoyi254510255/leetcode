class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        col = [False for _ in range(n)]
        #row = [False for _ in range(n)]
        dia1 = [False for _ in range(2 * n - 1)] #从右上到左下的45度对角线是否被占用  使用i+j标识是第几条对角线
        dia2 = [False for _ in range(2 * n - 1)] #从左上到右下135度对角线是否被占用， 使用i-j+n-1标识是把一条对角线
        ret_list = []
        
        def generateBoard(n,row):
            ret_str_list = []
            for i in range(n):
                tmp_str = ''
                for j in range(n):
                    tmp_str += 'Q' if (j==row[i]) else '.'
                ret_str_list.append(tmp_str)
            return ret_str_list
            #return [['Q' if (j==row[i]) else '.' for j in range(n)] for i in range(n)]
        
        #index表示在处理第index行，row存放每一行的皇后拜访在第几列的位置
        def putQueen(n, index, row):
            if index == n :
                ret_list.append(generateBoard(n, row))
                return
            for i in range(n):
                if (not col[i]) and (not dia1[index + i]) and (not dia2[index -i + n -1]):
                    row.append(i)
                    col[i] = True
                    dia1[index + i] = True
                    dia2[index -i + n -1] = True
                    putQueen(n, index + 1, row)
                    col[i] = False
                    dia1[index + i] = False
                    dia2[index -i + n -1] = False
                    row.pop()
            return
                
        putQueen(n, 0, [])
        return ret_list
