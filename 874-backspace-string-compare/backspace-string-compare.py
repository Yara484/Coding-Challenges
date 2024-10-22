class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Using Stack
        stack_s = []
        stack_t = []

        for char in s:
            if char == '#' and len(stack_s) != 0:
                stack_s.pop()
            else:
                if char != '#': 
                    stack_s.append(char)   

        for char in t:
            if char == '#' and len(stack_t) != 0:
                stack_t.pop()
            else:
                if char != '#': 
                    stack_t.append(char) 

        return ''.join(stack_t) == ''.join(stack_s)                