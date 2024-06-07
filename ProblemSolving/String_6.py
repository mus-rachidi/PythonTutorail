from typing import List 

class Solution:
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_length = min(len(s) for s in strs)
        
        common_prefix = ""
        print(min_length)
        for i in range(min_length):
            current_char = strs[0][i]
            
            if all(s[i] == current_char for s in strs):
                common_prefix += current_char
            else:
                break
    
        return common_prefix

strs1 = ["fliwer", "foli", "flight"]
obj = Solution()
print(obj.longestCommonPrefix(strs1))  # Output: "fl"

strs2 = ["dog", "racecar", "c"]
print(obj.longestCommonPrefix(strs2))  # Output: ""
