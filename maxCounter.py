def solution(N, A):
    counter= [0]*N
    start_line = 0
    current_max = 0
    for index in A:
        x = index - 1
        if index > N:
            start_line = current_max
        elif counter[x] < start_line:
            counter[x] = start_line + 1
        else:
            counter[x] += 1
        if index <= N and counter[x] > current_max:
            current_max = counter[x]
    for index in range(0, len(counter)):
        if counter[index] < start_line:
            counter[index] = start_line
    return counter

print(solution(5, [1,5,2,7,4,7,2]))
