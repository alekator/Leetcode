# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Answer:

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        n=len(strs)
        strs.sort()
        for i in range(len(strs[0])):
            if strs[0][i]==strs[n-1][i]:
                ans+=strs[0][i]
            else:
                break
        return ans
