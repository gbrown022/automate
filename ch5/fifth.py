# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}

# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1

# print(count)


theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

#printBoard(theBoard)

turn = 'X'

for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space? (q to quit):')
    move = input()
    if move.lower() == 'q':
        break
    else:
        theBoard[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
                turn = 'X'

#Chapter 5 Questions	
# 1. What does the code for an empty dictionary look like?
emptyDict = {}

# 2. What does a dictionary value with a key 'foo' and a value 42 look like?
myDict = {'foo': 42}
	
# 3. What is the main difference between a dictionary and a list?
# Dictionary is unordered, and has access by keys

# 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
# KeyError
	

# 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
# They are different ways to refernce keys in the dictionary
print()
spam = {'tall': '12oz', 'grande':'16oz', 'venti': '24oz', 'trenta': '31oz'}
for d, s in spam.items():
    print(d + ' cup size is ' + s)
print()
# spam['cat'] is a key that will return the value associated with the key 'cat'
# spam.keys() will return the list of all keys

# 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
# spam['cat'] is a value referenced by a key; spam.values() is a list of all values in the spam dictionary
	
# 7. What is a shortcut for the following code?
#if 'color' not in spam:
#    spam['color'] = 'black'
# Answer:
#	spam.setdefault('color', 'black')

# 8. What module and function can be used to “pretty print” dictionary values?
# Module: pprint, function: pprint: pprint.pprint(dict)


# For practice, write programs to do the following tasks.
# Fantasy Game Inventory

# You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary where the keys 
# are string values describing the item in the inventory and the value is an integer value detailing how many of that item the 
# player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the 
# player has 1 rope, 6 torches, 42 gold coins, and so on.

# Write a function named displayInventory() that would take any possible “inventory” and display it like the following:

# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62

# Hint: You can use a for loop to loop through all the keys in a dictionary.

# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
more_stuff = {'backpack': 1, 'spellbook': 3, 'pointy hat': 1, 'robes': 2}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL IN THE CODE HERE
        print(k + ' ' + str(v))
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)
print()
displayInventory(more_stuff)

# List to Dictionary Function for Fantasy Game Inventory

# Imagine that a vanquished dragon’s loot is represented as a list of strings like this:

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing 
# the player’s inventory (like in the previous project) and the addedItems parameter is a list like dragonLoot. The addToInventory()
# function should return a dictionary that represents the updated inventory. Note that the addedItems list can contain multiples
# of the same item. Your code could look something like this:

def addToInventory(inventory, addedItems):
    # my code follows
    for item in addedItems:
        if item in inventory.keys():
            inventory[item] = inventory[item] + 1
        else:
            # using the subscript notation 
            inventory[item] = 1
    return(inventory)

# Starter loot
inv = {'gold coin': 42, 'rope': 1}

# After raiding dragon's lair
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Add up the takings!
inv = addToInventory(inv, dragonLoot)

# Show 'em what I got
print()
displayInventory(inv)