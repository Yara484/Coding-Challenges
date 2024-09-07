class Solution:
    def isValid(self, s: str) -> bool:
        # Create a dict to store values
        mymap = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []

        for char in s:
            if char in mymap:
                if stack and stack[-1] == mymap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False                    