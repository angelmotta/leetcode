# https://leetcode.com/problems/valid-palindrome/

#Solution 1
# Time O(n) | Space O(n)

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         theInput = s.lower()
#         myalnum = ""
#         for letter in theInput:
#             if letter.isalnum():
#                 myalnum += letter
#         for i in range(len(myalnum)):
#             j = len(myalnum) - i - 1
#             if i > j: break
#             if myalnum[i] != myalnum[j]:
#                 return False
        
#         return True



# Solution 2
# Time O(n) | Space O(1)
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         i = 0
#         j = len(s) - 1
#         while i <= j:
#         # check if chars are alpha-num and compare both in place
#             lChar = ""
#             rChar = ""
#             if s[i].isalnum():
#                 lChar = s[i].lower()
#                 print("lChar: " +  lChar)
#             else:
#                 while not s[i].isalnum():
#                     i += 1
#                     print("avanza i: " + str(i))
#                     if i > len(s) - 1:
#                         return True
#                 lChar = s[i].lower()
#                 print("..lChar: " +  lChar + " at idx: " + str(i))

#             if s[j].isalnum():
#                 rChar = s[j].lower()
#                 print("rChar: " +  rChar)
#             else:
#                 while not s[j].isalnum():
#                     j -= 1
#                     print("avanza j: " + str(j))
#                     if j < 0:
#                         return True
#                 rChar = s[j].lower()
#                 print("rChar: " +  rChar)
#             print("Compare chars:")
#             print("lChar: " + lChar + " at Index: " + str(i) + " - rChar: " + rChar + " at Index: " + str(j))
#             if i >= j:
#                 return True
#             if lChar != rChar:
#                 return False
#             i += 1
#             j -= 1
#             # END While
#         return True

# Solution 2 (Refactor)
# Time O(n) | Space O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            # Get i and j positions
            while i < j and not s[i].isalnum():
                i += 1
            while j > i and not s[j].isalnum():
                j -= 1
            print("i: " + str(i) + " char: " + s[i].lower() + " vs j: " + str(j) + " char: " + s[j].lower())
            if s[i].lower() != s[j].lower():
                print("FALSE!!!")
                return False
            i += 1
            j -= 1
        return True

s = "A man, a plan, a canal: Panama"
#s = "aa"
#s = "Marge, let's \"[went].\" I await {news} telegram."

sol = Solution()
ans = sol.isPalindrome(s)
print(ans)