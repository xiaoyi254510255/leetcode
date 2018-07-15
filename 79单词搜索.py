class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        direct = [[-1,0], [0,1], [1,0],[0,-1]]
        def inAera(indexX, indexY):
            return (indexX >= 0) and (indexX < m) and (indexY>=0) and (indexY < n)
        
        def searchWord(board, word, index, startx, starty):
            if index == len(word) -1 :
                return board[startx][starty] == word[index]
            if board[startx][starty] == word[index]:
                visited[startx][starty] = True
                for i in range(4):
                    newx = startx + direct[i][0]
                    newy = starty + direct[i][1]
                    if inAera(newx, newy) and (not visited[newx][newy]):
                        if searchWord(board, word, index+1, newx, newy):
                            return True
                visited[startx][starty] = False
            return False
                        
                    
                
            return
        for i in range(m):
            for j in range(n):
                if searchWord(board, word, 0, i, j):
                    return True
        
        return False
