'''
9. Palindrome Number

Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

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
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Base condition
        if x < 0:
            return False
        # Store the number in a variable
        number = x
        # This will store the reverse of the number
        reverse = 0
        while number:
            reverse = reverse * 10 + number % 10
            number //= 10
        return x == reverse
