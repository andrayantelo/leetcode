# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Input: "()"
# Output: true

# Input: "([)]"
# Output: false

""" pseudocode:
if your string is empty just return true
irl, i would look at the string character by character (maybe make it into 
an array, then check if the next character in the array is the closing pair 
for the character we are looking at. if it isn't return false immediately 
without looking at the rest of the characters. 
Maybe have a pair dictionary to draw from?"""

pairs = {
    '(': ')',
    '{': '}',
    '[': ']'
}

def isValid(s: str) -> bool:
    if s == "":
        return False
    print("length of s: {}".format(len(s)))
    
    # iterate over string s
    for i in range(len(s)):
        print("s[i] : {}".format(s[i]))
        print("i + 1: {}".format(i + 1))
        if i + 1 > len(s):
            i += 1
            break;
        
        elif pairs[s[i]] and s[i + 1] != pairs[s[i]]:
            return False
    return True
        
# other people's solutions:

def check_brackets(to_check):
    if to_check == "":
        return True
    paren, curly, sqr_ = 0, 0, 0
    
    for char in to_check:
        if char == "(":
            paren += 1
        if char == ")":
            paren -= 1
        if char == "{":
            curly += 1
        if char == "}":
            curly -= 1
        if char == "[":
            sqr_ += 1
        if char == "]":
            sqr_ -= 1
        if paren < 0 or curly < 0 or sqr_ < 0:
            return False
    if paren != 0 or curly != 0 or sqr_ != 0:
        return False
    return True
    
# use a stack
#stack = []
#if char in ['(', '[', '{']:
#    stack.append(char)
#else: 
#    if stack[-1]

def is_valid_pair(open_bracket, closed_bracket):
    pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    print("pair: {} and {}:".format(open_bracket, closed_bracket))
    return pairs.get(open_bracket) == closed_bracket
     
    
def is_valid_sequence(input_str):
    stack = []
    for bracket in input_str:
        if not stack:
            stack.append(bracket)
        else:
            if is_valid_pair(stack[-1], bracket):
                stack.pop()
                
            else:
                stack.append(bracket)
    return not stack
    
if __name__ == "__main__":
    
    s = "()[]{}"
    print(is_valid_sequence(s))
    
    s1 = "([)]"
    print(is_valid_sequence(s1))
    
    s2 = "()"
    print(is_valid_sequence(s2))
