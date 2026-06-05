import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # create a hashmap of all 26 types of CPU tasks
        # create a max heap based on the freqency of the tasks
        # prioritize the most freq(thats why max heap) task
        # process the task, then add it to a queue with time at which it will be available again
        hmap = {}
        for task in tasks:
            hmap[task] = hmap.get(task,0) + 1 
        maxheap = [-count for count in hmap.values()]
        heapq.heapify(maxheap)
        queue = deque()
        time = 0
        while maxheap or queue:
            time+=1
            if maxheap:
                task_count = 1 + heapq.heappop(maxheap)
                if task_count: # it can get processed out
                    queue.append([task_count,time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(maxheap,queue.popleft()[0])
        return time
                