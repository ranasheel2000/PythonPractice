bills = {.01:'PENNY',
        .05:'NICKEL',
        0.10:'DIME',
        0.25:'QUARTER',
        0.50:'HALF DOLLAR',
        1.00:'ONE',
        2.00:'TWO',
        5.00:'FIVE',
        10.0:'TEN',
        20.00:'TWENTY',
        50.00:'FIFTY',
        100.00:'ONE HUNDRED'}

 

changes1=[]
def changes(change_value):
    #print(change_value)
    #changes1=[]
    if(change_value>=100.00):
        changes1.append(bills[100.00])
        value=float("{0:.2f}".format(change_value-100.00))
        return changes(value)
    elif(change_value>=50.00):
        changes1.append(bills[50.00])
        value=float("{0:.2f}".format(change_value-50.00))
        return changes(value)
    if(change_value>=20.00):
        changes1.append(bills[20.00])
        value=float("{0:.2f}".format(change_value-20.00))
        return changes(value)
    elif(change_value>=10.00):
        changes1.append(bills[10.00])
        value=float("{0:.2f}".format(change_value-10.00))
        return changes(value)
    elif(change_value>=5.00):
        changes1.append(bills[5.00])
        value=float("{0:.2f}".format(change_value-5.00))
        return changes(value)
    if(change_value>=2.00):
        changes1.append(bills[2.00])
        value=float("{0:.2f}".format(change_value-2.00))
        return changes(value)
    elif(change_value>=1.00):
        changes1.append(bills[1.00])
        value=float("{0:.2f}".format(change_value-1.00))
        return changes(value)
    elif(change_value>=0.50):
        changes1.append(bills[0.50])
        value=float("{0:.2f}".format(change_value-0.50))
        return changes(value)
    if(change_value>=0.25):
        changes1.append(bills[0.25])
        value=float("{0:.2f}".format(change_value-0.25))
        return changes(value)
    elif(change_value>=0.10):
        changes1.append(bills[0.10])
        value=float("{0:.2f}".format(change_value-0.10))
        return changes(value)
    elif(change_value>=0.05):
        changes1.append(bills[0.05])
        value=float("{0:.2f}".format(change_value-0.05))
        return changes(value)
    elif(change_value>=0.01):
        changes1.append(bills[0.01])
    return changes1

 

def cash_register(pp,ch):
    change_value=float("{0:.2f}".format(ch-pp))
    changes(change_value)
    return(change_value)

 

while(True):
    print("Please enter PP and CH values separated by semicolon")
    print("Please enter 0;0 to exit")
    customer_input =input()
    inputs=customer_input.split(";")
    #if(len(inputs)!=2 or input[1] is ""):
    #    print("wrong input")
    pp = float(inputs[0])
    ch = float(inputs[1])
    #print(pp)
    #print(ch)
    if(ch==pp==0):
        exit()
    if(ch<pp):
        print("ERROR")
    elif(ch==pp):
        print("ZERO")
    else:

        print(cash_register(pp,ch))
