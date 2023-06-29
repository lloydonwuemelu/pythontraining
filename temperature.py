#Explain the purpose of the program
print(' Hello This is a Temperature Converter')

#Display a menu for the temperature conversions
menu = int(input( 'What conversion do you want to perform?' +
                  '\n1. Celsius to Fahrenheight' +
                  '\n2. Fahrenheit to Celcius' + 
                  '\nPlease make a choice: '))

#Convert from Celcius to Fahrenheight
if (menu == 1):
    celcius = float(input('Please enter a value in Celcius: '))
    fahrenheight = ((celcius * 9) / 5)  + 32
    print(str(celcius) + chr(176) + 'C',
           'is',str(round(fahrenheight, 2)) + chr(176) + 'F')                  

#Convert from Fahrenheight to Celcius
elif (menu == 2):
     fahrenheight = float(input('Please enter a value in Fahrenheight: '))
     celcius = ((fahrenheight -32) * 5) /9
     print(str(round(fahrenheight,2)) + chr(176) + 'F',
            'is', str(celcius) + chr(176) + 'C')

else:
    print('Invalid Selection')
