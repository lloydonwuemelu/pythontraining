#Assign variables for the PIN and account balance
PIN = 2003
account_balance = 1000000

#Welcome the user
print('Welcome to TrustBnk')

#Ask the user to enter a PIN
input_pin = int(input('Please enter your PIN: '))

#Ensure the PINs match as the input_pin
while (input_pin ==PIN):

#If the PINs don't match come here
else:
    print('This PIN is Invalid')

print('\nPlease have a good day.')    

# Ensure the PINs match as the looping condition
while (input_pin == PIN):
    
#Display a menu of options
    menu = int(input('\nWhat do you want to do?' +
                     '\n1. Withdraw N20,000' +
                     '\n2. Check Account Balance' +
                     '\n3. End Transaction' +
                     '\nPlease select an entry: '))
    #Withdraw 20000
    if (menu == 1):
        #Subtract 20000 from account balamce
        account_balance = account_balance - 20000
