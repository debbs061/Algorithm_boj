class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []  # [val,curMin] , monotonic decreasing stack
        curMin = nums[0]

        for n in nums[1:]:
            while stack and stack[-1][0] <= n:
                stack.pop()
            if stack and stack[-1][1] < n:
                return True
            stack.append([n, curMin])
            curMin = min(curMin, n)
        return False
