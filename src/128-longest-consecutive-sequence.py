def longestConsecutive(nums):
    # 특정 원소가 존재하는지를 검사하는 연산의 시간 복잡도 O(1)
    # set 은 특정한 데이터가 이미 등장한 적이 있는지 여부를 체크할 때 매우 효과적
    # in python, set is implemented as a hash table. so you can expect lookup/insert/delete in o(1) average
    numSet = set(nums)
    longest = 0

    for n in nums:
        # check if it is the start of a sequence
        if (n - 1) not in numSet:
            length = 0
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest
