even_num=0   # initialize the count of even integers to 0
for i in range(5,15,2):  # iterate through numbers 5 to 15 with a step of 2 (i.e., 5, 7, 9, 11, 13) 
    if i%2==0:   #selection of even integers 
     even_num +=1   # increment the count of even integers
print(even_num)   # print the count of even numbers