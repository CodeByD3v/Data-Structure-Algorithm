"""
9. Palindrome Number

Hint
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
Constraints:

-231 <= x <= 231 - 1

"""

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False 
        return str(x) == str(x)[::-1]  

# Another solution that can be used
class Solution(object):
    def isPalindrome(self, x):

        if  x < 0 :
            return False

        sums = 0 
        copy = x

        while copy > 0 :
            last = copy % 10 
            sums = sums * 10 + last 
            copy = copy // 10

        return sums == x
