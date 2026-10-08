# setting values
a = 4617
b = 9428

# conditionals on the odd or even start/finish
if b%2 == 1 :
    end = b+1
else : 
    end = b
if a%2 == 1 :
    start = a
else :
    start = a+1

# creating the list of all odds integer in between and summing them 
integer_list = list(range(start, end, 2))
sum_integer_list = sum(integer_list)

# printing the answer
print(sum_integer_list)