# 1. Functions are good for modularization, code reuse, optimization etc.
# 2. A function executes when the function is called
# 3. def fname(): creates a function
# 4. Funtction is a block of code that does something; a funtcion call executes the block of code when the intrepreter finds the statement in the stript
# 5. One global scope, as many local scopes are there are local blocks of code
# 6. Local scope variables are released when the function call returns
# 7. Return value is a variable and contents returned by a function. Yes, a return value can be part of an expression
# 8. If a function does not have a return statment, it returns None
# 9. Force a global reference by preceeding variable with "global" keyword
# 10. Data type of None is NoneType
# 11. import areallyourpetsnamederic pulls in the module 'areallyourpetsnamederic'
# 12. spam.bacon()
# 13. a "try/catch error handling block"
# 14. try takes the statement that might have an error, except catches the error and handles gracefully

# Collactz() sequence
# Write a function named collatz() that has one parameter named number. 
# If number is even, then collatz() should print number // 2 and return this value. 
# If number is odd, then collatz() should print and return 3 * number + 1.

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False


def collactz(number):
    coll = 0
    if isEven(number) :
        coll = number // 2
        print(str(coll))
        return(coll)
    else:
        coll = 3 * number + 1
        print(str(coll))
        return(coll)

while True:
    try:
        val = int(input("Enter a number: "))
        break
    except ValueError:
        print("You must enter an integer.")

result = collactz(int(val))

while result != 1:
    result = collactz(result)
    