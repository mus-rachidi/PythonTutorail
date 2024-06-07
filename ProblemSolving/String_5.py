class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        len_haystack = len(haystack)
        len_needle = len(needle)
        
        if len_haystack < len_needle:
            return -1
        for i, char in enumerate(haystack):
            if char == needle[0] and haystack[i:i + len_needle] == needle[:len_needle]:
                return i
        return -1      
            
obj = Solution()
print(obj.strStr("sadbutsad", "sad"))
