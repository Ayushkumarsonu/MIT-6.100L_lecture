num = int(input("Enter any number to find its square root"))
guess = 0.0                      # initializing the guess to zero 
epsilon = 0.01                   # sets a range on both side of the ideal answer , the soon it touches the range it will stop the loop and print the answer
num_of_guesses = 0               # to count number of guesses the computer made
increment = 0.00001              # this defines how short the increment will be , the smaller the increment , the more accurate the answer will be but it will take more time to find the answer
while abs(guess**2 - num) >= epsilon and guess**2 <= num:     # loop will run until the square of the guessed number is within the range of the user input and the square of the guessed number is less than or equal to the user input
    guess += increment    
    num_of_guesses += 1
print(f"The number of guesses is {num_of_guesses}")
if abs(guess**2 - num) >= epsilon:     # if the square of the guessed number is not within the range of the user input , then this block will run
    print(f"The square root of the number is not found")
else:
    print(f"{guess} is close to square root of {num}")  # if found , then this block prints the closest value
