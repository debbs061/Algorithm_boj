from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        minIdxofChunkEnd = 0
        chunk = 0
        for i in range(len(arr)):
            minIdxofChunkEnd = max(minIdxofChunkEnd, arr[i])
            if minIdxofChunkEnd == i:
                chunk += 1
        return chunk
