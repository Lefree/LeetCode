import functools
import string
import re


class Solution:
    def mySqrt(self, x):
        """
        Implement int sqrt(int x).
        Compute and return the square root of x, 
        where x is guaranteed to be a non-negative integer.
        Since the return type is an integer, the decimal digits are truncated 
        and only the integer part of the result is returned.
        :type x: int
        :rtype: int
        """
        a_side = 1
        b_side = x
        eps = 1e-5
        while abs(a_side - b_side) >= eps:
            square = a_side * b_side
            a_side = (a_side + b_side) / 2.0
            b_side = square / a_side
        return int(a_side)
    

    def romanToInt(self, s):
        """
        Given a roman numeral, convert it to an integer. 
        Input is guaranteed to be within the range from 1 to 3999.
        :type s: str
        :rtype: int
        """
        roman_symbols = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500,
            'M': 1000,
        }
        prev_number = ''
        sum = 0
        for elem in s:
            sum += roman_symbols[elem]
            if elem != prev_number:
                if prev_number and roman_symbols[prev_number] < roman_symbols[elem]:
                    sum -= 2 * roman_symbols[prev_number]
                prev_number = elem
        return sum
    

    def isNumberPalindrome(self, x):
        """
        Determine whether an integer is a palindrome. 
        An integer is a palindrome when it reads the same backward as forward.
        :type x: int
        :rtype: bool
        """
        if x < 0: 
            return False
        right = list()
        while x != 0:
            right.append(x % 10)
            x = x // 10
        for x in range(len(right)):
            if right[x] != right[len(right) - x - 1]:
                return False
        return True

    
    def reverse(self, x):
        """
        Given a 32-bit signed integer, reverse digits of an integer.
        :type x: int
        :rtype: int
        """
        sign = False
        if x < 0:
            sign = True
            x = -x
        reverse_number = int(''.join(list(str(x))[::-1]))
        if reverse_number > 2147483648:
            return 0
        else:
            return -reverse_number if sign else reverse_number

    
    def singleNumber(self, nums):
        """
        Given a non-empty array of integers, every element 
        appears twice except for one. Find that single one.
        :type nums: List[int]
        :rtype: int
        """
        return functools.reduce(lambda a, x: a ^ x, nums)

    
    def isPalindrome(self, s):
        """
        Given a string, determine if it is a palindrome, 
        considering only alphanumeric characters and ignoring cases.
        :type s: str
        :rtype: bool
        """
        s = re.sub('['+string.punctuation+']', '', s.replace(' ', '').lower())
        if len(s):
            for ind in range(len(s) // 2 + 1):
                if (s[ind].isalpha() or s[ind].isdigit()) and s[ind] != s[len(s) - ind - 1]:
                    return False
        return True


    def removeElement(self, nums, val):
        """
        Given an array nums and a value val, remove all instances 
        of that value in-place and return the new length.
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for elem in nums[::]:
            if elem == val:
                nums.remove(elem)
        return len(nums)
    

    def removeDuplicates(self, nums):
        """
        Given a sorted array nums, remove the duplicates in-place 
        such that each element appear only once and return the new length.
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            privious = nums[0]
            for elem in nums[1::]:
                if privious == elem:
                    nums.remove(elem)
                else:
                    privious = elem
        return len(nums) 


    def numJewelsInStones(self, J, S):
        """
        You're given strings J representing the types of stones that are jewels, 
        and S representing the stones you have.  
        Each character in S is a type of stone you have.  
        You want to know how many of the stones you have are also jewels.
        :type J: str
        :type S: str
        :rtype: int
        """
        return functools.reduce(lambda a, x: a + int(x in J), S, 0)


    def toLowerCase(self, str):
        """
        Implement function ToLowerCase() that has a string parameter str,
        and returns the same string in lowercase
        :type str: str
        :rtype: str
        """
        return ''.join([chr(ord(c) + 32) if c.isupper() else c for c in str])


    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code = [
            ".-","-...","-.-.","-..",".","..-.",
            "--.","....","..",".---","-.-",".-..","--",
            "-.","---",".--.","--.-",".-.","...","-",
            "..-","...-",".--","-..-","-.--","--.."
        ]
        morse_code = {chr(letter + ord('a')):morse_code[letter] for letter in range(0, 26)}
        result = set()
        for word in words:
            morse_word = ''
            for letter in word:
                morse_word += morse_code[letter]
            result.add(morse_word)
        return len(result)


    def sortArrayByParity(self, A):
        """
        Given an array A of non-negative integers, 
        return an array consisting of all the even elements of A, 
        followed by all the odd elements of A.
        You may return any answer array that satisfies this condition.
        :type A: List[int]
        :rtype: List[int]
        """

