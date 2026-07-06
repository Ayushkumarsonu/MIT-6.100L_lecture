cube = int(input("Enter any number to find its cube root "))
for guess in range(abs(cube) +1):
    if guess ** 3  >= abs(cube):
        break
if guess ** 3 != abs(cube):
    print ("The number is not a perfect cube and the cube root of the number lies between " , guess-1 , "and" , guess ) 
else :
    print ("The cube root of the number is exists")
    if cube < 0:
        guess = -guess
        print ( f"The cube root of the number is {guess}" )
    else :
        print ( f"The cube root of the number is {guess}" )

