def solution(numbers, target):
    answer = 0
    cache = {}

    def dfs(i, sum):
        if i == len(numbers):
            if sum == target:
                return 1
            return 0
        if (i, sum) in cache:
            return cache[(i, sum)]

        cnt = dfs(i + 1, sum - numbers[i])
        cnt += dfs(i + 1, sum + numbers[i])

        cache[(i, sum)] = cnt
        return cache[(i, sum)]

    answer = dfs(0, 0)
    return answer
