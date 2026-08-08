from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Create adjacency list
        graph = [[] for _ in range(numCourses)]

        # Calculate indegree
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        # Add courses with 0 prerequisites
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        result = []

        # Kahn's Algorithm
        while queue:

            course = queue.popleft()
            result.append(course)

            for neighbor in graph[course]:

                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Cycle exists
        if len(result) != numCourses:
            return []

        return result