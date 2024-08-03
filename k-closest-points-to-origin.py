def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

    # distance from origin
    def distance(x, y): 
        return (x*x + y*y)
    
    ranks = []

    for i in range(len(points)):
        dist = distance(points[i][0], points[i][1])

        ranks.append([i, dist])
    
    ranks.sort(key = lambda x: x[1])
    
    output = []
    for i in range(k):
        output.append(points[ranks[i][0]])
    return output
    
    # runtime: nlog(n) from sort
    # space: n 
        