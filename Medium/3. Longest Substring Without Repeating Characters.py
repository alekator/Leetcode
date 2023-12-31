# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:
# 1. 0 <= s.length <= 5 * 104
# 2. s consists of English letters, digits, symbols and spaces.

# Answer(the easiest possible solution without using hash map):
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        ans = 1
        tmp = ""
        for i in range(len(s)):
            while s[i] in tmp:
                tmp = tmp[1:]
            tmp += s[i]
            ans = max(ans, len(tmp))
        return ans
