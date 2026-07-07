binary = int(input("Enter any binary number"))  # asks user input 
mysum=0
digits = [int(d) for d in str(binary)]          # first converts the binary number to string an then converts each digit to integer and stores it in a list called digits
for i, d in enumerate(digits):                  # enumerate function is used to get the index and the value of each digit in the list digits
    mysum += d * (2 ** (len(digits) - 1 - i))   # the value of each digit is multiplied by 2 raised to the power of its index in the list digits and added to mysum
print(f"The decimal value of the binary number is {mysum}")  # print
