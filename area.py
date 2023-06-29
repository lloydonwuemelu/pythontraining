import math

#Explain the purpose of the program
print('This program is an Area Calculator')

#Display the shapes menu
menu = int(input('What shape do you want to find the area of?' + 
                 '\n1. Triangle' +
                 '\n2. Square' +
                 '\n3. Circle' +
                 '\nPlease choose a shape: '))

#Find the area of the shape circle
if (menu == 1):
    print('Area of a Triangle')
elif(menu == 2):
    print('Area of a Square')
elif(menu == 3):
    print('Area of a Circle')
else:
    print('Invalid Selection')

