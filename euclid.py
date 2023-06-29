#Ask the user for the first number
first_number = int(input('Please enter the first number: '))

#Ask the user for the second number
second_number = int(input('Please enter the second number: '))
print(first_number,second_number)
#Swap the numbers if the second number is greater than the first
if (second_number > first_number):
    temp = second_number
    second_number = first_number
    first_number = temp

#Print out the numbers to check the swap
print(first_number, second_number)    

#Find the remainder
remainder = first_number % second_number

# Loop until the remainder is 0
while (remainder > 0):
    remainder = first_number % second_number
    first_number = second_number
    second_number = remainder

print('The HCF is:',first_number)




















