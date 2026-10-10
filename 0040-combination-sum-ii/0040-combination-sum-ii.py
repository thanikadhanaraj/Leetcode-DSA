class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, current, total):
            if total == target:
                result.append(current[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):

                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current.append(candidates[i])

                # i + 1 because each number can be used only once
                backtrack(i + 1, current, total + candidates[i])

                current.pop()

        backtrack(0, [], 0)

        return result