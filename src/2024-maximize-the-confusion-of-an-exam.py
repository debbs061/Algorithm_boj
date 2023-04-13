class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res = left = 0
        count = {"T": 0, "F": 0}
        for right in range(len(answerKey)):
            count[answerKey[right]] += 1
            while min(count["T"], count["F"]) > k:
                count[answerKey[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res
