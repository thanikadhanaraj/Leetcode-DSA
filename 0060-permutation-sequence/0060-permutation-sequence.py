class Solution:
    def getPermutation(self, n, k):
        nums = list(range(1, n + 1))
        result = ""

        fact = 1
        for i in range(1, n):
            fact *= i

        k = k - 1

        while n > 0:
            index = k // fact
            result += str(nums[index])
            nums.pop(index)

            k = k % fact
            n = n - 1

            if n > 0:
                fact = fact // n

        return result