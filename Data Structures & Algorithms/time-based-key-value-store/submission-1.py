class TimeMap:

    def __init__(self):
        self.hashStore = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashStore:
            self.hashStore[key] = {}
        if timestamp not in self.hashStore[key]:
            self.hashStore[key][timestamp] = []
        self.hashStore[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashStore:
            return ''
        seen = 0
        for time in self.hashStore[key]:
            if time <= timestamp:
                seen = max(seen,time)
        return '' if seen == 0 else self.hashStore[key][seen][-1]