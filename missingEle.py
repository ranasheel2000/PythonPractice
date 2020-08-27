def solution(A):
    # find sum of 1 to A
    l=len(A)+1
    #print(l)
    sumval=int((l*(l+1))/2)
    #print(sumval)
    for i in range(0,l-1):
        sumval=sumval-A[i]
    return(sumval)


A=[1,2,4,5]
missing=solution(A)
print(missing)
