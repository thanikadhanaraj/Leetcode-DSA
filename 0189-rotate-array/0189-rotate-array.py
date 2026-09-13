class Solution:
    def rotate(self, nums: list[int], k: int):
        n = len(nums)
        k %= n

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        return nums
