class MyHashSet:

    def __init__(self):
        self.buckets = [[]] * 10000

    def add(self, key: int) -> None:
        bucketIdx = key % 10000
        if key not in self.buckets[bucketIdx]:
            self.buckets[bucketIdx].append(key)

    def remove(self, key: int) -> None:
        bucketIdx = key % 10000
        if key in self.buckets[bucketIdx]:
            self.buckets[bucketIdx].remove(key)

    def contains(self, key: int) -> bool:
        bucketIdx = key % 10000
        return key in self.buckets[bucketIdx]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
