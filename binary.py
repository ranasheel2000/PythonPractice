def BinaryConversion(num):
   if num > 1:
       BinaryConversion(num//2)
   print(num%2, end="")

num=int(input("Enter decimal number for binary conversion"))
BinaryConversion(num)
