class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq = { course:[] for course in range(numCourses )}
        for course, prereq in prerequisites:
            preq[course].append(prereq)
        
        visited = set()
        completed = set()
        res = []
        def dfs(course):
            if course in visited: return False
            if course in completed: return True
            visited.add(course)
            for pre in preq[course]:
                if not dfs(pre): return False
            res.append(course)
            visited.remove(course)
            completed.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course): return []
        return res