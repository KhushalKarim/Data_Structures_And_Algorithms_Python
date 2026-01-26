class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=0
        right=k-1
        result=float("inf")

        while right< len(nums):
            result=min(result, nums[right]-nums[left])
            left=left+1
            right=right+1
        return result


#[1,4,7,9]

#[9,4,1,7]
        