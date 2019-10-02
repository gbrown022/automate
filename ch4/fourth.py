# Fourth Chapter Questions and exercise

# 1. [] denotes a list\
# 2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
# For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].
spam = ['a', 'b', 'c', 'd']

spam[2] = 'hello'
# 3. What does spam[int(int('3' * 2) // 11)] evaluate to?
# 'd'
# 4. What does spam[-1] evaluate to: 'd'
# 5. what does spam[:2] evaluate to: 'a' 'b'
# For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].
# 6. What does bacon.index('cat') evaluate to: 1
# 7. What does bacon.append(99) make the list value in bacon look like: [3.14, 'cat', 11, 'cat', True, 99]
# 8. What does bacon.remove('cat') make the list value in bacon look like? [3.14, 11, 'cat', True, 99]
# 9. What are the operators for list concatenation and list replication: +, +=, *, *=
# 10. What is the difference between the append() and insert() list methods: append() adds to end of list, insert inserts at the specified index.
# 11. What are two ways to remove values from a list: remove() when you know the item, del() when you know the index
# 12. Name a few ways that list values are similar to string values: ordered,indexable,may be sliced
# 13. What is the difference between lists and tuples: Lists are mutable, tuples may not be changed
# 14. How do you type the tuple value that has just the integer value 42 in it: myTuple = ('a', 42) 
#      myTuple(1) 
#      > 42
# 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
#  Tuple of list:  tuple(['cat', 'dog', 5])
#  List of tuple: list(('cat','dog', 5))
# 16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
# References to memory locations of lists
# 17. What is the difference between copy.copy() and copy.deepcopy()?
#  copy.copy(list) creates a new memory referesce for the copyied list
# copy.deepcopy() is used when lists contain other lists

# Comma code
# Write a function that takes a list value as an argument and returns a string with all the items
#  separated by a comma and a space, with and inserted before the last item. 
def commaCode(lst):
    newList = []
    for item in range(len(lst)-1):  # treat the last item differently
        newList.append(lst[item]+ ', ') 
    newList.append('and ' +lst[-1])
    return(newList)

bacon = ['hog', 'pig', 'oinker']
print(commaCode(bacon))


Grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def printCharsSideways(grid):
    
    #for each row select each first element starting with the last row
    #build a new matrix
    #print the new matrix
    
    # Next five lines prints the grid bottom to top. It's a solution, just not the one I want 28-Sep-2019
    #for row in range((len(lst)-1), -1, -1)
    #    for elem in range((len(lst[row])-1), -1 -1):
    #        newGrid.append(row[elem])
    #        print(row[elem])
    
    #Need to make a new grid, swapping first column for first row, second column for second row etc.

    rows = len(grid) # Number of elements in the list
    cols = len(grid[0]) # Number of elements in every single element in the list

    for x in range(cols):
        for i in range(rows):
            print(grid[i][x], end='')
        print()
    

printCharsSideways(Grid)