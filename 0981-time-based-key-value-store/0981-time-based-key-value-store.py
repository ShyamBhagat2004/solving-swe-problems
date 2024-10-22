class TimeMap:
    def __init__(self):
        self.hashMap = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
    
        self.hashMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashMap:

            tlist = self.hashMap[key]
            L, R = 0, len(tlist) - 1

            closest = -1
            while L <= R:
                M = (L + R) // 2
                if tlist[M][0] > timestamp:
                    R = M - 1
                else:
                    closest = M
                    L = M + 1
            if closest == -1:
                return ""
            return tlist[closest][1]
        else:
            return ""


            
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)