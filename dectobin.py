binary = int(input("Enter any binary number"))
mysum=0
digits = [int(d) for d in str(binary)]
for i, d in enumerate(digits):
    mysum += d * (2 ** (len(digits) - 1 - i))
print(f"The decimal value of the binary number is {mysum}")