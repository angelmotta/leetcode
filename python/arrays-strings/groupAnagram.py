# https://leetcode.com/problems/group-anagrams/description/
from typing import List

# Time O(n * m) where `n` is list's length strs and `m` is the average length of each word in the list strs
# Space O(n) where n is the lenght of strs
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapGroupAnagrams = {}
        for str in strs:
            counterWord = [0] * 26 # a-z chars
            for c in str:
                idx = ord(c) - ord('a')
                counterWord[idx] += 1
            keyCounterWord = tuple(counterWord) # making list unmutable (for hashing)
            if keyCounterWord in mapGroupAnagrams:
                mapGroupAnagrams[keyCounterWord].append(str)
            else:
                mapGroupAnagrams[keyCounterWord] = [str]
        return list(mapGroupAnagrams.values())


solver = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
out = [["bat"],["nat","tan"],["ate","eat","tea"]]
ans = solver.groupAnagrams(strs)
print(ans)
