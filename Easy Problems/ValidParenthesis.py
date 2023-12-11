class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        correctness = False
        if s[-1] == '(' or s[-1] == '{' or s[-1] == '[':
            return correctness
        for i in s:
            if i =='(' or i =='{' or i =='[':
                stack.append(i)
            if i == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    correctness = True
                    stack.pop()
                else:
                    correctness = False
                    return correctness
            if i == '}':
                if len(stack) > 0 and stack[-1] == '{':
                    correctness = True
                    stack.pop()
                else:
                    correctness = False
                    return correctness
            if i == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    correctness = True
                    stack.pop()
                else:
                    correctness = False
                    return correctness
        if (len(stack) > 0):
            correctness = False
            return correctness
                    
        return correctness

            