register={.01: 'PENNY',
.05:'NICKEL',
.10:'DIME',
.25:'QUARTER',
.50:'HALF DOLLAR',
1.00:'ONE',
2.00:'TWO',
5.00:'FIVE',
10.00:'TEN',
20.00:'TWENTY',
50.00:'FIFTY',
100.00:'ONE HUNDRED'}

def calculate(pp,ch):
    #left_cash=float("{0:.2f}".format(ch-pp))
    left_cash=float(ch)-float(pp)
    print(left_cash)
    result=[]
    while(left_cash>0.01):
        if(left_cash>=100.00):
            result.append(register[100.00])
            left_cash=float("{0:.2f}".format(left_cash-100.00))
            print(result)
            print(left_cash)
        elif(left_cash>=50.00):
            result.append(register[50.00])
            left_cash=float("{0:.2f}".format(left_cash-50.00))
            print(result)
            print(left_cash)
        elif(left_cash>=20.00):
            result.append(register[20.00])
            left_cash=float("{0:.2f}".format(left_cash-20.00))
            print(result)
            print(left_cash)
        elif(left_cash>=10.00):
            result.append(register[10.00])
            left_cash=float("{0:.2f}".format(left_cash-10.00))
            print(result)
            print(left_cash)
        elif(left_cash>=5.00):
            result.append(register[5.00])
            left_cash=float("{0:.2f}".format(left_cash-5.00))
            print(result)
            print(left_cash)
        elif(left_cash>=2.00):
            result.append(register[2.00])
            left_cash=float("{0:.2f}".format(left_cash-2.00))
            print(result)
            print(left_cash)
        elif(left_cash>=1.00):
            result.append(register[1.00])
            left_cash=float("{0:.2f}".format(left_cash-1.00))
            print(result)
            print(left_cash)
        elif(left_cash>=0.50):
            result.append(register[0.50])
            left_cash=float("{0:.2f}".format(left_cash-0.50))
            print(result)
            print(left_cash)
        elif(left_cash>=0.25):
            result.append(register[0.25])
            left_cash=float("{0:.2f}".format(left_cash-0.25))
            print(result)
            print(left_cash)
        elif(left_cash>=0.10):
            result.append(register[0.10])
            left_cash=float("{0:.2f}".format(left_cash-0.10))
            print(result)
            print(left_cash)
        elif(left_cash>=0.5):
            result.append(register[0.5])
            left_cash=float("{0:.2f}".format(left_cash-0.5))
            print(result)
            print(left_cash)
        elif(left_cash>=0.1):
            result.append(register[0.1])
            left_cash=float("{0:.2f}".format(left_cash-0.1))
            print(result)
            print(left_cash)
    return(sorted(result))
#import pdb
#pdb.set_trace()
user_input=input()
seperated_input=user_input.split(';')
output=""
pp=seperated_input[0]
ch=seperated_input[1]
if(ch<pp):
    print("ERROR")
elif(ch==pp):
    print("ZERO")
else:
    result=calculate(pp,ch)
    for x in result:
        output=','.join(x)
    print(output)
