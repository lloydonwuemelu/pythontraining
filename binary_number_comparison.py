#Ask the user to enter a number
input_number = int(input('PLEASE ENTER A NUMBER: '))

#Declare an empty string
answer = ""

#Find the whole number value of integer division
while(input_number//2>=0):
    #Find the remainder of the input number %2
    remainder = input_number%2
  
    #Add the remainder to the outside string
    answer = str(remainder) + answer

    #Find the whole number value again ,if it is >0 go to step 4 or else end the loop   
    input_number=input_number//2

    if(input_number == 0):
        break

#Print out the value of the binary number
print(answer)
  

    

