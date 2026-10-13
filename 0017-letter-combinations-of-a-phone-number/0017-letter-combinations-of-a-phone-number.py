class Solution:
    def letterCombinations(self, digits):
        if digits == "":
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def generate(index, current):
            if index == len(digits):
                result.append(current)
                return

            for ch in phone[digits[index]]:
                generate(index + 1, current + ch)

        generate(0, "")

        return result