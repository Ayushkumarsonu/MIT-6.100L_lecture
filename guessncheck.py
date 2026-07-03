secret =4
guess = 0 
while guess <= 10 :
    guess+=1
    if guess == secret :
        print( "You have found the number", secret)
        break
    if guess != secret :
        print("It didn't find it")

     