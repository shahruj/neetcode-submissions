class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bmap = {
            "{":"}",
            "[":"]",
            "(":")"
        }

        for bracket in s:
            if bracket not in bmap:
                if len(stack)>0 and stack[-1] in bmap and bmap[stack[-1]] == bracket:
                        stack.pop()
                else:
                    stack.append(bracket)
            else:
                stack.append(bracket)
            
        print(stack)
        if len(stack) == 0:
            return True
        else:
            return False
