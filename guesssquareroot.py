guess=0  # intialize guess to 0 ,  starting point of the loop 
check_flag = False #  setting a boolean flag to false to check if the user entered a negative value or not
x = int (input ("Enter any number to find its square root ")) # asling input from the user 
if x < 0:                  # # checking if the user entered a negative value or not 
    check_flag = True      # if yes , then boolean flag will change to True 
while guess**2< x:         # loop will run until the square of the the guessed number is leass than the user input , this will restricts the lopp to run only until the square of the guessed number is less than the user input    
    guess+=1               # increment
if guess**2 == x :         # cchecking if the square of the guessed number isequal to the user input or not 
    print ("The square root of the number is " , guess) # print 
else :                     # if the number is not a perfect sqaure , then the else block will run
    print ("The square root of the number is in between " , guess-1 , "and" , guess )  # prints the estimated possible result
    if check_flag == True :     # if the user entered a negative value , then this block will run 
        print (" Are you sure you want to find the square root of " , x ,"intead of its absolute value")  # reassuring the user if he/she wants to find the square root of a negative number or not
