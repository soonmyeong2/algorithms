class Solution(object):
    def decodeString(self, s):
        stack = list()
        
        for char in s:
            if char == "]":
                substr = ""
                while stack[-1] != "[":
                    substr += stack.pop()
                stack.pop()
                repeat = ""
                while stack and stack[-1].isdigit():
                    repeat += stack.pop()
                stack.append(int(repeat[::-1]) * substr)
            else:
                stack.append(char)
        return "".join([x[::-1] for x in stack])
