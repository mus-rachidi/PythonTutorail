class Solution:
    def twoSum(self, nums, target):
        nums_with_indices = [(num, i) for i, num in enumerate(nums)] # list of tuple 
        
        print("nums_with_indices:", nums_with_indices)

        n = len(nums)
        for i in range(n):
            print(i)
            for j in range(i + 1, n):
                # print(j)
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []  

s = Solution()
print(s.twoSum([3, 5, 1, 4], 6)) 
