"""
Given two binary trees and imagine that when you put one of
them to cover the other, some nodes of the two trees are overlapped
while the others are not.

You need to merge them into a new binary tree.
The merge rule is that if two nodes overlap,
then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of new tree.

Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, t1, t2):
        pass

if __name__ == "__main__":
    t1 = TreeNode(1, TreeNode(3, 5), TreeNode(2))
    t2 = TreeNode(2, TreeNode(1, None, 4), TreeNode(3, None, 7))
    solution = Solution()
    t3 = solution.mergeTrees(t1, t2)
    