class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        while matrix:
            spiral+=matrix[0]
            matrix.pop(0)
            [row.reverse() for row in matrix]
            matrix = [list(y) for y in zip(*matrix)]
        return spiral
        
