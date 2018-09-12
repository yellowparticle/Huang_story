""" 
Write a program that will take a number (intergers only) and 
return a statement that will let the user know if it is even or odd
"""
x = int(input("Enter a number: "))
if (x%2==0):
    print("The number you entered is even")
if (x%2==1):
    print("The number you entered is odd")
