class TimeMap:

    def __init__(self):
        self.hashMap = {}  # val : [(time, val), (time2, val2)..]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = [(timestamp, value)]
            return
        self.hashMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap:
            return ""

        arr = self.hashMap[key]
        l, r = 0, len(arr) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if arr[m][0] == timestamp:
                return arr[m][1]
            if arr[m][0] < timestamp:
                res = arr[m][1]
                l = m + 1
            else:
                r = m - 1
        return res

        # Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
