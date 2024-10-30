n = int ( input (" Enter a number n: ") )
first_fibonacci = 0
second_fibonacci = 1

for i in range ( n ):
    
    print( first_fibonacci , end=" , ")
    next_fibonacci = first_fibonacci + second_fibonacci #calculate the next fibonacci number
    first_fibonacci = second_fibonacci #update the first fibonacci to the current one
    second_fibonacci = next_fibonacci  #update the second fibonacci to the next fibonacci number