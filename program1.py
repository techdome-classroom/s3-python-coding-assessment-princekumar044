class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to map closing brackets to opening brackets
        bracket_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        # Stack to hold opening brackets
        stack = []
        
        # Iterate through each character in the string
        for char in s:
            if char in bracket_map:
                # Pop the top element from stack if it's not empty, otherwise set a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the popped element doesn't match the current closing bracket, return False
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # In the end, the stack should be empty if all brackets were matched
        return not stack

# Test cases
solution = Solution()
print(solution.isValid("()"))       # Output: True
print(solution.isValid("()[]{}"))   # Output: True
print(solution.isValid("(]"))       # Output: False
print(solution.isValid("([)]"))     # Output: False
print(solution.isValid("{[]}"))     # Output: True


    



  

