class Solution:
    def __init__(self):
        self.directions: List[List[int, int]] = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 1],
            [1, -1], [1, 0], [1, 1]
        ]

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 1. neighbors < 2 = die
        # 2. 2 <= neighbors <= 3 live
        # 3. neighbors = 3 revive
        # 4. 3 < neighbors die

        # Original  Change  New
        # 0         None    0
        # 0         Live    2
        # 1         None    1
        # 1         Dead    -1
        self.width: int = len(board[0])
        self.height: int = len(board)

        for row in range(self.height):
            for column in range(self.width):
                value = board[row][column]
                neighbors = self._sum_neighbors(row, column, board)
                if value == 0:
                    if neighbors == 3:
                        board[row][column] = 2
                else: # value == 1
                    if neighbors < 2:
                        board[row][column] = -1
                    elif neighbors > 3:
                        board[row][column] = -1
                    
        for row in range(self.height):
            for column in range(self.width):
                value = board[row][column]
                if value == 2:
                    board[row][column] = 1
                elif value == -1:
                    board[row][column] = 0
        

    def _sum_neighbors(self, row: int, column: int, board: List[List[int]]) -> int:
        sum: int = 0
        for (j, i) in self.directions:
            y = row + j
            x = column + i
            if self.height > y >= 0 and self.width > x >= 0:
                value = board[y][x] 
                if value == -1:
                    sum += 1
                elif value == 2:
                    continue
                else:
                    sum += value
        return sum
