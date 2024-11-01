# Luna Perez
# UWYO COSC 1010
# 10/31/2024
# Lab 07
# Lab Section: 13
# Sources, people worked with, help given to:  https://stackoverflow.com/questions/35467303/write-factorial-with-while-loop-python for help on what/how to do a factorial 
# https://www.w3schools.com/python/ref_string_split.asp for how to split strings, https://stackoverflow.com/questions/63760633/replace-expected-at-least-2-arguments-got-1-error for help with replace errors
# Lecture 10 Powerpoint slides



# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered
stored_number = input("Give me a  number and ill give you the factorial:  ")
while stored_number.isnumeric() == False:
    stored_number= input("that wasnt an integer please try again: ")
else:
    stored_number = int(stored_number)
# I used the Internet to help come up with a python friendly formula for factorials.
print(stored_number)
factorial = 1
while stored_number > 1:
    factorial= factorial * stored_number
    stored_number= stored_number - 1

print(f"The result of the factorial based on the given bound is {factorial}")

print("*"*75)
# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 
prompt = "Give me Numbers and ill add them all together, type exit to leave: "
num_sum = 0 

while True:
    num_storage = input(prompt)
    if num_storage.lower() == "exit":
        break
    if num_storage[0] == "-":
        num_storage = num_storage.replace('-','') 
        num_sum -= int(num_storage)
    elif num_storage.isdigit():
        num_sum += int(num_storage)
    else:
        print("that is not an integer")
   
print(f"Your final sum is {num_sum}")

print("*"*75)
# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 

calc_prompt ="Give me a simple calculation and type exit to end: "
calc_op = None
operand1 = ""
operand2 = ""
calc_output = 0
while True:
    calc_input= input(calc_prompt)
    if calc_input.lower() == "exit":
        break
# Go through a loop to strip the operator from the opends and give it a variable
    for char in calc_input:
        if char in ("+","/","-",'*','%'):
            calc_op = char
            operand1, operand2 = calc_input.split(calc_op)
            break
    operand1 = int(operand1)
    operand2 = int(operand2)
    #use the  Operator variable to "do" the calculations 
    if calc_op == '+':
        calc_output = operand1 +  operand2
    elif calc_op == '/':
        calc_output = operand1 / operand2
    elif calc_op == '-':
        calc_output = operand1 - operand2
    elif calc_op == '*':
        calc_output = operand1 * operand2
    elif calc_op == '%':
        calc_output = operand1 % operand2
    else:
        print('Invaild Operator.')
    print("Output: ", calc_output)

print("Thanks, goodbye")
            
                
       
            
    
        