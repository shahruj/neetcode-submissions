class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operand = ["+","-","*","/"]
        for token in tokens:
            if token in operand:
                A = int(stack.pop())
                B = int(stack.pop())
                if token == "+":
                    output = B + A
                elif token == "-":
                    output = B - A
                elif token == "*":
                    output = B * A
                else:
                    output = B/A
                
                stack.append(output)
            else:
                stack.append(token)
            # print(stack)
        return int(stack[0])