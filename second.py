# Chapter 2 Questions
# 1. Booleans are True and Fals
# 2. Three boolean operators: and, or, not 
# 3. Truth tables. Ich. I will look it up if needed
# 4. false, false, true, false, false, true
# 5. Comparison operators: >, <, >=, <=, !=, ==
# 6. One compares, one assigns
# 7. Conditions are used to determine whether to do something (again) or not--ask for a legal password until user enters a legal password discarding illegal passwords
# 8. Blocks
# 9. 
def greeting(spam):
    if spam == 1:
        print('Hello')
    elif spam == 2:
        print('Howdy')
    else:
        print('Greetings')

greeting('eggs')
greeting(2)
greeting(1)

# 10. ^c
# 11. break breaks out of a loop; continue continues the loop
# 12. range(10), range(0, 10), range(0,10,1) all the same.
# 13.
def countTo10():
    start = 1
    for val in range(10):
        print(start)
        start = start + 1

countTo10()

print('************')

def whileTo10():
    start = 1
    while start < 11:
        print(start)
        start = start + 1

whileTo10()

# 14. spam.bacon()