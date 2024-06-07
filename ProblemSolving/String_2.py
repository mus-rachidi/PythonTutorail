class Solution:
    def reverse(self, x: int) -> int:
        str1 = str(x)
        
        if str1[0] == '-':
            str2 = str1[:0:-1]
            result = -int(str2)
        else:
            str2 = str1[::-1]
            result = int(str2)
        
        if result < -2**31 or result > 2**31 - 1:
            return 0
        
        return result

s = Solution()
print(s.reverse(1234))    # Output: 4321
print(s.reverse(-1234))   # Output: -4321
print(s.reverse(1534236469))  # Output: 0 (overflow case)
