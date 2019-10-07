#! python

print('hello world')

# 1. What are escape characters?
# Characters with special meaning to the system, like /t (tab), /n newline etc.

# 2. What do the \n and \t escape characters represent? 
# See previous answer

# 3. How can you put a \ backslash character in a string?
# # add an 'escape' character:  \\

# 4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?
# Because the surrounding quotes are double quotes: "" 
	

# 5. If you don’t want to put \n in your string, how can you write a string with newlines in it?
# By triple quoting a multiline string """"


# """
#

# 6. What do the following expressions evaluate to?

    # 'Hello world!'[1]
    # e

    # 'Hello world!'[0:5]
    # Hello

    # 'Hello world!'[:5]
    # Hello

    # 'Hello world!'[3:]
    # lo world!

# 7. What do the following expressions evaluate to?

    # 'Hello'.upper()
    # HELLO

    # 'Hello'.upper().isupper()
    # True

    # 'Hello'.upper().lower()
    # hello

# 8. What do the following expressions evaluate to?

#    'Remember, remember, the fifth of November.'.split()
# {'Remember,', 'remember,', 'the', 'fifth', 'of', 'November.'}
#    '-'.join('There can be only one.'.split())
#   {'There-can-be-only-one.'}

# 9. What string methods can you use to right-justify, left-justify, and center a string?
# ljust(), rjust(), center()

# 10. How can you trim whitespace characters from the beginning or end of a string?
# lstrip(), rstrip()

# Practice Project

# For practice, write a program that does the following.
# Table Printer

# Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:

# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dogs', 'cats', 'moose', 'goose']]

# Your printTable() function would print the following:

#   apples Alice  dogs
#  oranges   Bob  cats
# cherries Carol moose
#   banana David goose

# Hint: Your code will first have to find the longest string in each of the inner
#  lists so that the whole column can be wide enough to fit all the strings. 
#  You can store the maximum width of each column as a list of integers. 
#  The printTable() function can begin with colWidths = [0] * len(tableData), 
#  which will create a list containing the same number of 0 values as the number 
#  of inner lists in tableData. That way, colWidths[0] can store the width of the 
#  longest string in tableData[0], colWidths[1] can store the width of the longest
#  string in tableData[1], and so on. You can then find the largest value in the 
#  colWidths list to find out what integer width to pass to the rjust() string 
#  method.

# Write a function named printTable() that takes a list of lists of strings and 
# displays it in a well-organized table with each column right-justified. Assume
#  that all the inner lists will contain the same number of strings.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def getMaxWidth(lists):
    longest = 0
    for list in lists:
        for elem in list:
            if len(elem) > longest:
                longest = len(elem)
    return(longest)

def printTableFullJustification(lists):
    #fully justified by longest string in table with
    maxWidth = getMaxWidth(lists)
    for list in lists:
        subListLength = len(list)
        i = 0
        while i < subListLength:
            #  'end=" "' to add a space between elements
            print(list[i].rjust(maxWidth), end=" ")
            i += 1
        print()

def printTableColumnJustification(lists):
    # fully justified by longest string in each column
    # this is the problem spec; i didn't like it so I wrote the full justification
    # function as well

    # iterate over the list of lists passed to the funtcion (lists) and 
    # find the longest word per column for rjusttification
    maxCol = getMaxWidth(lists)
    print("max col =  " + str(maxCol))
    # Iterate over the sublists and print each value from the inner list
    # right justified to the colWidth value already determined
    for l in range(len(lists)):
        for s in range(len(lists[l])):
            print(lists[l][s].rjust(maxCol), end=' ')
        print()

#printTableFullJustification(tableData)
print("*********")
printTableColumnJustification(tableData)
        