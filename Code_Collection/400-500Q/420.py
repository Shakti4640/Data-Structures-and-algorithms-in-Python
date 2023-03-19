'''
420. Strong Password Checker

A password is considered strong if the below conditions are all met:

It has at least 6 characters and at most 20 characters.
It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
It does not contain three repeating characters in a row (i.e., "Baaabb0" is weak, but "Baaba0" is strong).
Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

In one step, you can:

Insert one character to password,
Delete one character from password, or
Replace one character of password with another character.
 

Example 1:

Input: password = "a"
Output: 5
Example 2:

Input: password = "aA1"
Output: 3
Example 3:

Input: password = "1337C0d3"
Output: 0
 

Constraints:

1 <= password.length <= 50
password consists of letters, digits, dot '.' or exclamation mark '!'.
'''

class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        n = len(s)
        chars = list(s)
        missing = self.getMissing(chars)
        replaces = 0
        oneSeq = 0
        twoSeq = 0

        i = 2
        while i < n:
            if chars[i] == chars[i - 1] and chars[i - 1] == chars[i - 2]:
                length = 2
                while i < n and chars[i] == chars[i - 1]:
                    length += 1
                    i += 1
                replaces += length // 3
                if length % 3 == 0:
                    oneSeq += 1
                if length % 3 == 1:
                    twoSeq += 1
            else:
                i += 1

        if n < 6:
            return max(6 - n, missing)
        if n <= 20:
            return max(replaces, missing)

        deletes = n - 20
        replaces -= min(oneSeq, deletes)
        replaces -= min(max(deletes - oneSeq, 0), twoSeq * 2) // 2
        replaces -= max(deletes - oneSeq - twoSeq * 2, 0) // 3
        return deletes + max(replaces, missing)

    def getMissing(self, chars):
        missing = 3
        for c in chars:
            if c.isupper():
                missing -= 1
                break
        for c in chars:
            if c.islower():
                missing -= 1
                break
        for c in chars:
            if c.isdigit():
                missing -= 1
                break
        return missing




