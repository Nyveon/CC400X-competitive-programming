import heapq
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        task_counts = Counter(tasks)

        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        cooling_queue = deque()  # Stores (task_frequency, ready_time)

        time = 0

        while max_heap or cooling_queue:
            time += 1

            if cooling_queue and cooling_queue[0][1] == time:
                heapq.heappush(max_heap, cooling_queue.popleft()[0])

            if max_heap:
                current_task = heapq.heappop(max_heap)
                if current_task + 1 < 0:
                    cooling_queue.append((current_task + 1, time + n + 1))

        return time
