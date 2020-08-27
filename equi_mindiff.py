def sol(A):
    # use sum and abs builtins
    leftSum=A[0]
    rightSum=sum(A)-A[0]
    diff=abs(rightSum-leftSum)
    for i in range(1,len(A)-1):
        rightSum=rightSum-A[i]
        leftSum=leftSum+A[i]
        newDiff=abs(rightSum-leftSum)
        if(newDiff < diff):
            diff=newDiff
    return(diff)

A=[2,10,5,11,5,9,10,1,2]
diff=sol(A)
print("minimum diff is = {0}".format(diff))
