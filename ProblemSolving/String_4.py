class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
            
        for char in s:
            if char.isalnum():
                if char.isupper():
                    char = char.lower()
                stack.append(char)
                
        last = len(stack) - 1
        first = 0
        print(stack)
        while first < last:
            if stack[first] != stack[last]:
                return False
            first+=1
            last-=1
        return True

        
obj = Solution()
print(obj.isPalindrome("dA, b ! c: cbad"))