class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        i = 0
        n = len(s)
        result = 0
        sign = 1

        while i < n and s[i] == ' ':
            i += 1

        if i < n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1

        while i < n and s[i].isdigit():
            digit = int(s[i])

            if result > (INT_MAX - digit) // 10:
                return INT_MIN if sign == -1 else INT_MAX

            result = result * 10 + digit
            i += 1

        return sign * result

obj = Solution()

print(obj.myAtoi("-2147483649"))  


print(obj.myAtoi("   -42"))  
print(obj.myAtoi("4-2"))           # Output: 42
     # Output: -42
print(obj.myAtoi("4193 with words"))  # Output: 4193
print(obj.myAtoi("words and 987"))    # Output: 0
print(obj.myAtoi("-2147483649"))     # Output: -2147483648 (clamped)
