import functools
import string
import re


class Solution:
    def mySqrt(self, x):
        """
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
    

    def isPalindrome(self, x):
        """
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
        :type nums: List[int]
        :rtype: int
        """
        return functools.reduce(lambda a, x: a ^ x, nums)

    
    def isPalindrome(self, s):
        """
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
