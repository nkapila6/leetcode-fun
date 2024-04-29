class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_list = list(enumerate(nums))
        sorted_list.sort(key=lambda x: x[1])
        p1 = 0 #left pointer
        p2 = len(nums)-1 #right pointer
        
        for _ in range(len(nums)):
            check = sorted_list[p1][1] + sorted_list[p2][1]
            if (check == target):
                return [sorted_list[p1][0], sorted_list[p2][0]]
            elif (check>target):
                p2 = p2 - 1
            else:
                p1 = p1 + 1