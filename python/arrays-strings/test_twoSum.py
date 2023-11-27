# Problem: https://leetcode.com/problems/two-sum/description/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if hm.get(complement, -1) != -1:
                return [i, hm.get(complement)]
            else:
                hm[nums[i]] =  i


def test_solution():
    s = Solution()
    ans = s.twoSum([2,7,11,15], 9)
    assert ans == [0,1] or ans == [1,0]


test_solution()