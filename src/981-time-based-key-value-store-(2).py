import collections


class TimeMap:

    def __init__(self):
        self.time = collections.defaultdict(list)  # key: string , value: [time, val]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time:
            return ""

        timeMap = self.time[key]
        l, r = 0, len(timeMap) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if timestamp >= timeMap[m][0]:
                res = timeMap[m][1]
                l = m + 1
            elif timestamp < timeMap[m][0]:
                r = m - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
