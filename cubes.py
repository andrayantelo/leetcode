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

# when would you not be able to stack 2 cubes.. basically never. because you can stack them if they are the same length
# a cube like this 4 1 2 3

def determine_stackability(sidelenghts):
    # start by checking if leftmost is less than or equal to the rightmost
    # if yes, it goes on top of rightmost, and our next block, pop off the one you used
    # maybe use recursion, our base case is that we have 2 cubese
    print("working with sidelengths: {}".format(sidelengths))
    if len(sidelengths) == 0:
        return "No"
    if len(sidelengths) == 1 or len(sidelengths) == 2:
        return "Yes"
    
    if sidelengths[0] >= sidelengths[-1]:
        print(sidelengths[1:])
        return determine_stackability(sidelengths[1:])
    elif sidelengths[-1] >= sidelengths[0]:
        print(sidelengths[:len(sidelengths) - 1])
        return determine_stackability(sidelengths[:len(sidelengths) - 1])
    return "No"
    
if __name__ == "__main__":
    #num_testcases = int(input())
    #for i in range(num_testcases):
        
    #    num_sides = int(input())
    #    sidelengths = [int(x) for x in input().split(" ")]
    
    #    print(determind_stackability(sidelengths))
    #sidelengths = [4, 3, 2, 1, 3, 4]
    sidelengths = [1, 3, 2]
    #sidelengths = []
    print(determine_stackability(sidelengths))
