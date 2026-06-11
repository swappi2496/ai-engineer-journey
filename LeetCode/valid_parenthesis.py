def is_valid(s):
    stack = []
    pairs = {')': '(' , ']':'[', '}': '{'}

    for char in s:
        if char in '({[':
            stack.append(char)

        else:
            if not stack or stack.pop() != pairs[char]:
                return False
            
    return len(stack) == 0

print(is_valid("()"))
print(is_valid("{}[]"))
print(is_valid(")}["))
print(is_valid("([){}"))

## Leetcode style solution

# class solution:
#     def is_valid(self, s:str) -> bool:
#         stack = []
#         pairs = {')': '(' , ']':'[', '}': '{'}

#         for char in s:
#             if char in "({[":
#                 stack.append(char)

#             else:
#                 if not stack or stack.pop != pairs[char]:
#                     return False
                
#         return len(stack) == 0
    
