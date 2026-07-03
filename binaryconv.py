num = int (input("Give a number"))
result =''
if num == 0:
    result = 0
while num >0 :
    result = (str(num%2)+ result) 
    num = num //2
print ( "It's binary conversion is " , result)