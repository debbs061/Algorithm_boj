from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = 1e9
        seen = {}

        for r in range(len(cards)):
            card_value = cards[r]
            if card_value in seen:
                res = min(r - seen[card_value] + 1, res)
            seen[card_value] = r  # update the index to latest

        return res if res != 1e9 else -1
