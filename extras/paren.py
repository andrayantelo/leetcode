"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
 determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Input: "()"
Output: true

Input: "()[]{}"
Output: true

Input: "(]"
Output: false

Input: "([)]"
Output: false

Input: "{[]}"
Output: true


"""

class Solution:
    def isValid(self, s):
        
        stack = []
        for i in range(0, len(s)):
            stack.append(s[i])
            if s[0] in [')', '}', ']']:
                return false
            print("i: {}".format(i))
            if stack[-1] == '(' and s[i] == ')' or stack[-1] == '{' and s[i] == '}' or stack[-1] == '[' and s[i] == ']':
                stack.pop()
                i + 1
                continue
            else:
                stack.append(s[i])
        print(stack)
        if len(stack) == 0:
            return True
            
            
if __name__ == "__main__":
    solution = Solution()
    
    s = "()"
    print(solution.isValid(s))
    
    
    s = "()[]{}"
    print(solution.isValid(s))
    
    """
    
    s = "(]"
    print(solution.isValid(s))
    
    s = "([)]"
    print(solution.isValid(s))
    
    s = "{[]}"
    print(solution.isValid(s))
    """
