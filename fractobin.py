fraction = float(input("Enter any fractional value in decimal form"))
result = ''
power = 0 
while fraction%1 != 0 :
    power += 1
    if fraction < 1 :
        fraction = fraction * 2 
        if fraction < 1 :
            result = result + str(0) 
        else :
            result = result + str(1)
    else :
        fraction = fraction - 1
        fraction = fraction * 2
        if fraction < 1:
            result = result + str(0)
        else :
            result = result + str(1) 
print(f"The binary form the number is { int(result) / (10 ** power)}")
        
        

    
