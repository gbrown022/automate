# GCB 3/31/2020
#
# Questions
# 1. Why are functions advantageous to have in your programs?
#    A. Functions are advantageous to reuse code, making it easier to
#    debug and trace
# 
# 2. When does the code in a function execute: when the function is 
#    defined or when the function is called?
#    A. Function code executes when the function is called.
#
# 3. What statement creates a function?
#    A. "def" creates a function
#
# 4.  What is the difference between a function and a function call?
#    A. The difference between a function and a function call is
#    the function contains the code, while the function call
#    intitates the code written in the function.
# 
# 5. How many global scopes are there in a Python program? How many 
#    local scopes? 
#    A. There is one global scope and one local scope per function.
#
# 6. What happens to variables in a local scope when the function
#    call returns? They are destroyed.
#
# 7. What is a return value? Can a return value be part of an expression?
#    A. A return value is a value passed back to the caller of a
#    function. Yes, a return value can be part of an expression. An
#    example of this would be a function returning True or False that 
#    would influence following on program code.
#
# 8. If a function does not have a return statement, what is the
#    return value of a call to that function?
#    "None"
# 
# 9. How can you force a variable in a function to refer to the
#    global variable?
#    A. By using the variable before defining it within the 
#    function using the "var" keyword.
#
# 10. What is the data type of "None"?
#     A. Data type of None in NoneType.
#
# 11. What does the import (allyourpetsarenamederic) statement do?
#     A. Imports a module called "allyourpetsarenamederic" for
#     availabily to reference and execute.
# 
# 12. If you had a function named bacon() in a module named 
#     spam, how would you call it after importing spam?
#     spam.bacon()
#
# 13. How can you prevent a program from crashing when it gets an error?
#     A. By implementing a try-catch block for exception handling of
#     anticipated runtime errors.
#
# 14. What goes in the try clause? What goes in the except clause?
#     A. The code that would would potentially have an error goes in
#     the "try" clause.
#     Program exocution moves to the beginning of the "except" clause
#     in case of an error.

# Collatz Sequence

def collatz(num):
    num = int(num)
    isOdd = int(num) % 2
    if isOdd == 1:
        colVal = 3 * num + 1
        print('collatz: ', colVal)
        return colVal
    else:
        # it's even--whole number, no remainder
        colVal = num // 2
        print('collatz: ', colVal)
        return colVal

version = '0.01'
print("Welcome to The Collatz Sequence Explorer " + version)
userNum = input('Enter an integer value: ' )
coltz = collatz(userNum)
loopcount = 1
while coltz != 1:
    loopcount += 1
    coltz = collatz(coltz)
print('loopcount: ', loopcount)
print('Program end.')