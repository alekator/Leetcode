# 67. Add Binary

# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# Answer:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=int(a,2)
        b=int(b,2)
        ans=a+b
        if(a==0 and b==0):
            return "0"
        mod= ""
        while(ans >= 1):
            mod += str(int(ans%2))
            ans = ans//2
        return mod[::-1]
