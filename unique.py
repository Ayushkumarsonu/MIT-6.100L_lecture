s= 'abchbscajiscuha'
seen =''
letter =0 
for char in s:
    if char not in seen :
       seen = seen + char  
       letter+=1
print (letter)
