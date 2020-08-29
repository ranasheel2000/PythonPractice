def solution(A, B, K):
    start=0
    end=0
    if(A%K==0):
        start=int(A/K)
    else:
        start=int(A/K) +1
    end=int(B//K)
    result=end-start+1
    return(result)

print(solution(3,21,2))
