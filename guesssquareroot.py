guess=0
check_flag = False
x = int (input ("Enter any number to find its square root "))
if x < 0:
    check_flag = True
while guess**2< x:
    guess+=1
if guess**2 == x :
    print ("The square root of the number is " , guess) 
else :
    print ("The square root of the number is in between " , guess-1 , "and" , guess )
    if check_flag == True :
        print (" Are you sure you want to find the square root of " , x ,"intead of its absolute value")
