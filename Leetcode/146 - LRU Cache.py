# Simple because it uses the fact that Python dicts are ordered, but
# for educational reasons I should probably attemtp this with a linked list at some point.


class LRUCache:
    def __init__(self, capacity: int):
        self.keys = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.keys:
            value = self.keys.pop(key)
            self.keys[key] = value
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            del self.keys[key]
            self.keys[key] = value
            return

        self.keys[key] = value

        if len(self.keys) > self.capacity:
            first_key = None
            for x in self.keys:
                first_key = x
                break
            del self.keys[first_key]
