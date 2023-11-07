from typing import List

class Solution:
    # Time O(n) | Space O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for elem in nums:
            if elem in hashSet: 
                return True
            hashSet.add(elem)
        
        return False


sol = Solution()
ans = sol.containsDuplicate([3,2,1,3])
print(ans)