from collections import deque
class RecentCounter:

    def __init__(self):
        self.request_counter = deque()
        

    def ping(self, t: int) -> int:
        self.request_counter.append(t)
        
        while self.request_counter[0]<t-3000:
            self.request_counter.popleft()
            
        return len(self.request_counter)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)