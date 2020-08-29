class Records():
    def __init__(self, x, position):
        self.x = x
        self.position = position

def solution(A):
    discRecords = []
    for i in range(len(A)):
        discRecords.append(Records(i - A[i], 1))
        discRecords.append(Records(i + A[i], -1))
    discRecords.sort(key=lambda d: (d.x, -d.position))
    intersections = 0
    current_intersections = 0
    for log in discRecords:
        current_intersections += log.position
        if log.position > 0:
            intersections += current_intersections - 1
        if intersections > 10000000:
            return -1
    return intersections

print(solution([5,1,2,6,2,0,4,3]))
