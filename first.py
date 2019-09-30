# This program says Hello and asks for my name

print('Hello world!')
print('What is your name?')    # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')    # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

# Questions/Answers CH1
# 1. op, value, value, op, op, op, val
# 2. var, string
# 3. string, int, list
# 4. expressions are made up of values and operators that resolve into a single value
# 5. statements are diffrenet from expressions in that the result of a statement gets assigned to a variable
# 6. bacon = 20; bacon + 1; bacon == 21
# 7. 'spam' + 'spamspam'; 'spam' * 3 both evaluate to 'spamspamspam'
# 8. eggs is a variable 'cuz it's made of characters, 100 is an integer that may not be assigned a value
# 9. str(), int(), float()
# 10. 'I have eaten' + 99 + ' burritos.' should be something like str(99) or '99'
