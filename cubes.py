"""
There is a horizontal row of n cubes. The length of each cube is given.
You need to create a new vertical pile of cubes. The new pile should
follow these directions: if cube_i  is on top of cube_j then sideLength_j >= sideLength_i.

When stacking the cubes, you can only pick up either the leftmost or the
rightmost cube each time. Print "Yes" if it is possible to stack the cubes.
Otherwise, print "No". Do not print the quotation marks.

Input Format

The first line contains a single integer T, the number of test cases. 
For each test case, there are 2 lines. 
The first line of each test case contains n, the number of cubes. 
The second line contains n space separated integers, denoting the sideLengths of each cube in that order.

Output Format

For each test case, output a single line containing either "Yes" or "No" without the quotes.

Sample Input:
2
6
4 3 2 1 3 4
3
1 3 2

Sample Output:
Yes
No

Explanation

In the first test case, pick in this order: left - 4, right - 4, left -3 , right -3 , left -2 , right -1 . 
In the second test case, no order gives an appropriate arrangement of vertical cubes. 3 will always come after either 1 or 2.
"""

import unittest
from collections import deque

# when would you not be able to stack 2 cubes.. basically never. because you can stack them if they are the same length
# a cube like this 4 1 2 3

def stackability(sidelengths):
    # while loop version
    leftmost = sidelengths[0]
    rightmost = sidelengths[-1]
    
    if leftmost >= rightmost:
        previous_cube = leftmost
        sidelengths.popleft()
    elif rightmost >= leftmost:
        previous_cube = rightmost
        sidelengths.pop()
        
    #print("previous_cube before while loop: {}".format(previous_cube))
    #print("sidelengths before while loop: {}".format(sidelengths))
    while len(sidelengths):
        leftmost = sidelengths[0]
        rightmost = sidelengths[-1]
        
        if leftmost >= rightmost and leftmost <= previous_cube:
            previous_cube = leftmost
            sidelengths.popleft()
        elif rightmost >= leftmost and rightmost <= previous_cube:
            previous_cube = rightmost
            sidelengths.pop()
        else:
            return "No"
        
        #print("previous_cube before next while loop iteration: {}".format(previous_cube))
        #print("sidelengths: {}".format(sidelengths))
    return "Yes"
        
        
    

"""

def stackability(stack, sidelengths):
    
    if len(sidelengths) == 1:
        return "Yes"
        
    # check the outer cubes and take the biggest one
    # left >= right
    leftmost = sidelengths[0]
    rightmost = sidelengths[-1]
    if leftmost >= rightmost:
        if len(stack) == 0:
            stack.append(leftmost)
        elif leftmost <= stack[0]:
            stack.pop()
            stack.append(leftmost)
        else:
            return "No"
        return stackability(stack, sidelengths[1:])
    
    elif rightmost >= leftmost:
        if len(stack) == 0:
            stack.append(rightmost)
        elif rightmost <= stack[0]:
            stack.pop()
            stack.append(rightmost)
        else:
            return "No"
        return stackability(stack, sidelengths[:len(sidelengths) - 1])
    else:
        return "No"

def stackability(stack, sidelengths, startIndex, endIndex):
   
    if startIndex == endIndex:
        return "Yes"
    
    leftmost = sidelengths[startIndex]
    rightmost = sidelengths[endIndex]

    # the bigger one is first in stack
    if leftmost >= rightmost:
        # if stack is empty just append
        if len(stack) == 0:
            stack.append(leftmost)
            # check stackability of rest of cubes
            startIndex += 1
            return stackability(stack, sidelengths, startIndex, endIndex)
        # if stack is not empty, see if leftmost is <= than the top item in stack
        # if it is, then add it to the stack and continue
        # if it's not, return "no"
        elif leftmost <= stack[-1]:
            stack.pop()
            stack.append(leftmost)
            # CONTINUE
            startIndex += 1
            return stackability(stack, sidelengths, startIndex, endIndex)
        else:
            return "No"
    elif rightmost >= leftmost:
        # if stack is empty just append
        if len(stack) == 0:
            stack.append(rightmost)
            endIndex -= 1
            return stackability(stack, sidelengths, startIndex, endIndex)
        
        elif rightmost <= stack[-1]:
            stack.pop()
            stack.append(rightmost)
            #CONTINUE
            endIndex -= 1
            return stackability(stack, sidelengths, startIndex, endIndex)
        else:
            return "No"

"""

class TestStackability(unittest.TestCase):
    
    def test_one_cubes(self):
        self.assertEqual(stackability([1]), "Yes")
    
    def test_equal_cubes(self):
        self.assertEqual(stackability([4,4,4]*50), "Yes")
        
    def test_correct_cubes(self):
        self.assertEqual(stackability([4, 3, 2, 1, 3, 4]), "Yes")
        
    def test_wrong_cubes(self):
        self.assertEqual(stackability([1, 3, 2]), "No")
        
    def test_random_cubes(self):
        self.assertEqual(stackability([3, 3, 5, 1, 2]), "No")
        
    def test_cubes(self):
        self.assertEqual(stackability([1, 1, 1, 10, 1, 1, 1]), "No")
        
    def test_cubes1(self):
        self.assertEqual(stackability([10,10,10, 1, 10, 10, 10]), "Yes")
    
    def test_cubes2(self):
        self.assertEqual(stackability([5,4,3,2,1]), "Yes")
    
    def test_cubes3(self):
        self.assertEqual(stackability([1, 2, 3, 4, 5]), "Yes")
    
    #def test_cubes4(self):
    #    self.assertEqual(stackability([], "")
    
    
if __name__ == "__main__":
    print(stackability(deque([3, 3, 5, 1, 2])))

    #unittest.main()
    
    #for _ in range(int(input())):
    #    num_cubes = int(input())
    #    sidelengths = input().split(" ")
    #    print(stackability(sidelengths))
