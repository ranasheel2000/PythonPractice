def decimalToBinary(n):
    return bin(n).replace("0b","")

 

def binaryToDecimal(n):
    return int(n, 2)

 

def leadingZero(mb,nb):
    if(len(nb)<len(mb)):
        return str(nb).zfill(len(mb))
    else:
        return str(mb).zfill(len(nb))

 

def solution(mb, nb):
    xor = ""
    lennb=len(nb)
    lenmb=len(mb)
    #if(lennb!=lennb):

 

 

    for i in range(lennb):
        if (mb[i] == nb[i]):
            xor += "0"
        else:
            xor += "1"
    return xor

 


if __name__ == '__main__':
    m=10
    n=200
    product=1
    while m<n:
        mb=decimalToBinary(m)
        nb=decimalToBinary(n)
        lenmb=len(mb)
        lennb=len(nb)
        if(lenmb<lennb):
            mb=leadingZero(mb,nb)
        else:
            nb=leadingZero(nb,mb)
        product=product*binaryToDecimal(solution(mb,nb))
        m=m+1
        #product=product*solution(mb,nb))
    print(product)
