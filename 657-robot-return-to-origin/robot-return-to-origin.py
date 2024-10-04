class Solution:
    def judgeCircle(self, moves: str) -> bool:
        directions = {
            'U' : [0,1],
            'D' : [0,-1],
            'R' : [1,0],
            'L' : [-1,0]
        }
        origin = [0,0]
        for char in moves:
            move = directions[char]
            origin[0] += move[0]
            origin[1] += move[1]

        if origin[0] == 0 and origin[1] == 0:
            return True
        return False

        
        