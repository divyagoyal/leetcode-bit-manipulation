# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        number = len(nums)
        for i,j in enumerate(nums):
            number^=i^j
        return number
        
