# This code gives value for any positive number , negative number as well as number with decimal values .i.e, REAL NUMBERS
cube = float(input("Enter any number to find its cube root")) 
epsilon = 0.01              # decides how close the answer should be to the actual cube root , the more the epsilon , the more accurate the answer will be but it will take more time to find the answer

if cube >0:                 # for any positive number , the boundaries are set , as for positive number ,
                            # the cube root will always be less than the number itself and greater than zero , so the low boundary is set to zero and the high boundary is set to the number itself
   low = 0
   high = cube
else :                      # for any negative number , the boundaries are set , as for negative number ,
                            # the cube root will always be greater than the number itself and less than zero , so the low boundary is set to the number itself and the high boundary is set to zero
    low = cube
    high = 0 
guess = (high + low )/2.0    
no_of_guesses = 0

while abs(guess**3-cube) > epsilon:   # condition for loop to run is within the range of epsilon 
    if guess **3 > cube:              # for guessed number greater than the actual number
        high = guess
    else:                             # for guessed number lower  than the actual number 
        low = guess
    guess = (high + low )/2.0
    no_of_guesses +=1
print(f"The number of guesses is {no_of_guesses}")      
    
print(f"{guess} is close to cube root of {cube}") 