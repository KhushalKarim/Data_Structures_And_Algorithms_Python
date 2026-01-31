class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')
        n = len(nums)

        for size in range(l, r + 1):
            if size > n:
                break

            # first window
            s = sum(nums[:size])
            if s > 0:
                ans = min(ans, s)

            # slide
            for i in range(size, n):
                s += nums[i] - nums[i - size]
                if s > 0:
                    ans = min(ans, s)

        return -1 if ans == float('inf') else ans
        