num = int(input("Enter any decimal number"))  # asks user input
if num == 0 :
    result =0                           # the binary form of zero is zero 
    print("It's binary form is " , result)
else :
    result = ''
    while num > 0 :    # loops runs until the user input is positive
        result = str(num%2) + result       # the remainder of the user input divided by 2 is concatenated to the left of the result variable which is initialized as an empty string
        num = num//2                    # divides the number by 2 and assigns the quotient to the variable num 
    print(f"The binary form of the decimal number is {result}") # print


