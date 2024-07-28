import collections 

class Solution:
    def __init__(self, tasks, durations, dependencies):
        self.tasks = tasks
        self.durations = durations
        self.dependencies = dependencies
        self.graph = collections.defaultdict(list)
        self.in_deg = {task: 0 for task in tasks}
        self.EFT = {task: 0 for task in tasks}
        self.LFT = {task: float('inf') for task in tasks}
        self.EST = {task: 0 for task in tasks}
        self.LST = {task: 0 for task in tasks}
        
        for task, dependent in dependencies:
            self.graph[task].append(dependent)
            self.in_deg[dependent] += 1

    def topological_sort(self):
        order = []
        queue = collections.deque([task for task in self.tasks if self.in_deg[task] == 0])
        
        while queue:
            current = queue.popleft()
            order.append(current)
            for neighbor in self.graph[current]:
                self.in_deg[neighbor] -= 1
                if self.in_deg[neighbor] == 0:
                    queue.append(neighbor)
        
        return order
    
    def calculate_times(self):
        order = self.topological_sort()
        
        for task in order:
            self.EFT[task] = self.EST[task] + self.durations[task]
            for neighbor in self.graph[task]:
                self.EST[neighbor] = max(self.EST[neighbor], self.EFT[task])
        
        project_EFT = max(self.EFT.values())
        for task in order:
            if not self.graph[task]:
                self.LFT[task] = project_EFT
        for task in reversed(order):
            for neighbor in self.graph[task]:
                self.LFT[task] = min(self.LFT[task], self.LST[neighbor])
            self.LST[task] = self.LFT[task] - self.durations[task]
        
        return project_EFT, max(self.LFT.values())
    

tasks = ['A', 'B', 'C', 'D', 'E']
durations = {'A': 2, 'B': 4, 'C': 3, 'D': 1, 'E': 2}
dependencies = [( 'A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'E')]

scheduler = Solution(tasks, durations, dependencies)
earliest_finish_time, latest_finish_time = scheduler.calculate_times()
print(f"Earliest time all tasks will be completed: {earliest_finish_time}")
print(f"Latest time all tasks will be completed: {latest_finish_time}")

#Time Complexity: O(V+E) where V is the number of tasks and E is the number of dependencies
#Space Complexity: O(V+E)