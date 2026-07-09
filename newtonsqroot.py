num = int(input("Enter any number to find its square root"))
epsilon = 0.01
guess = num/2
no_guesses = 0
while (guess**2-num) >= epsilon :
    no_guesses+=1
    guess = guess - (((guess**2 - num) / ( 2 * guess)))
print (f"The number of guesses is {no_guesses}")
print (f"{guess} is close to square root of {num}")


