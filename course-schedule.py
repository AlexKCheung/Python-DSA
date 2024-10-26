def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    prereq_map = {i:[] for i in range(numCourses)}

    for course, prereq in prerequisites:
        prereq_map[prereq].append(course)
    
    visit = set()

    def dfs(course):
        if course in visit:
            return False
        if prereq_map[course] == []:
            return True
        
        visit.add(course)
        for prereq in prereq_map[course]:
            if not dfs(prereq):
                return False
        visit.remove(course)
        prereq_map[course] = []
        return True
    
    for i in range(numCourses):
        if not dfs(i):
            return False
    return True