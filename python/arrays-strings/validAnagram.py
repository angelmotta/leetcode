# Sol2: Using Hash Map - Time O(n) | Space O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hm_s = {}
        hm_t = {}
        for idx in range(len(s)):
            val = hm_s.get(s[idx], 0)
            val += 1
            hm_s[s[idx]] = val
            val = hm_t.get(t[idx], 0)
            val += 1
            hm_t[t[idx]] = val

        for key in hm_s:
            if hm_s.get(key) != hm_t.get(key):
                return False
        return True

# Sol1: Using Array - Time O(n) | Space O(n)
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         counter = [0] * 26
#         for x in range(len(s)):
#             idx = ord(s[x]) - ord('a')
#             counter[idx] += 1
#             idx = ord(t[x]) - ord('a')
#             counter[idx] -= 1
        
#         for val in counter:
#             if val != 0:
#                 return False
#         return True

