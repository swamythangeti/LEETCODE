from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Adjacency list
        graph = [[] for _ in range(numCourses)]

        # Indegree of every course
        indegree = [0] * numCourses

        # Build graph
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        # Courses with no prerequisites
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        count = 0

        # BFS
        while queue:

            course = queue.popleft()
            count += 1

            for neighbor in graph[course]:

                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If all courses are processed, no cycle
        return count == numCourses