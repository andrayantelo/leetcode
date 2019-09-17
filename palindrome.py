"""
Palindrome 
Determine whether an integer is a palindrome. An integer is a palindrome
when it reads the same backward as forward.

Example 1:
Input : 121
Output : true

Example 2:
Input : - 121
Output : false
Explanation: From left to right, it reads -121. From right to left,
it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:

Coud you solve it without converting the integer to a string?
"""

class Solution:
    def isPalindrome(self, x):
        
        s = str(x)
        return s[::-1] == s
    
    def noStringPalindrome(self, k):
        if k == 0:
            return True
        if k%10 == 0:
            return False
            
        x, y = k, 0
        print("k: {}".format(k))
        while y< x:
            y *= 10  
            y += x%10
            x = x//10
            
        print("x : {}".format(x))
        print("y: {}".format(y))
        if x == y:
            return True
        elif x == y//10:
            return True
        return False
        
    def mySolution(self, num):
        # if your num is negative return false
        if num < 0:
            return False
        # if num is zero return true, (otherwise you get false in the next
        # conditional)
        if num == 0:
            return True
        # also if num ends with a zero return false, it won't be a palindrome
        # because you wouldn't start a number with zero
        if num%10 == 0:
            return False
        # we are going to construct the backwards version of our num
        reverse_num = 0
        
        # we are looping until we have gotten half of what reverse_num 
        # would be if we had constructed the entire reverse of num
        # we don't need the rest because of symmetry
        while reverse_num < num:
            # multiple reverse_num by 10 so that you add one digit to it
            # do this at the beginning so that the last time you go through this 
            # loop you don't end up with a 0 at the end of your reverse number
            reverse_num *= 10
            # get last digit of num and add it to reverse_num
            reverse_num += num%10
            # get rid of tens place digit in num
            num = num//10
            
        # so now you check if your reverse num is the same as your num
        # then you know it is a palindrome

        return num == reverse_num or num == reverse_num//10
        
    def myStringSolution(self, num):
        s = str(num)
        return s == s[::-1]
            
        
if __name__ == ('__main__'):
    palindrome = Solution()
    
    #print(palindrome.noStringPalindrome(121))
    #print(palindrome.noStringPalindrome(-121))
    #print(palindrome.noStringPalindrome(10))
    #print(palindrome.mySolution(121))
    #print(palindrome.mySolution(-121))
    #print(palindrome.mySolution(10))
    #print(palindrome.mySolution(0))
    
    print(palindrome.myStringSolution(121))
    print(palindrome.myStringSolution(-121))
    print(palindrome.myStringSolution(10))
    print(palindrome.myStringSolution(0))
    
# tuple is immutable, list is not
# what does immutable mean?
# when would you use a tuple and when would you use a list?
