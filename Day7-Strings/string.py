
# String is a sequence of characters


# string in single quotes
a = 'my name is shivraj'

# string in double quotes
b = "my name is shivraj khose"

# mutli line string using triple quotes
c = ''' 
        my 
        name
        is
        shivraj
    '''

print(c)



# string is immutable in java

# index of a string starts from 0 and goes till (length-1)
#

test = "america"

# this will slice the test string from 0 to 2, excludes 3
print(test[0:3])  # prints "ame"


# this will slice the test string from 1 to 2, excludes 3
print(test[1:3])  # prints "me"


# this will slice the test string from 2 to 2, excludes 3
print(test[2:3])  # prints "e"

# this will slice the test string from 1 to length-1
print(test[1:])

# this will slice the test string from 0 to 3
print(test[:4])

# this will slice the entire test string
print(test[:])




# String functions
name = "shivraj"

# length of string
print(len(name))

# check whether string ends with particular string
print(name.endswith("raj")) # prints true since name string ends with "raj"
print(name.endswith("abc")) # prints false since name string does not end with "abc"

# check whether string starts with particular string
print(name.startswith("shiv")) # prints true since name string starts with "shiv"
print(name.startswith("aaa"))  # prints false since name string does not start with "shiv"


# convert first character of the string from lowercase to uppercase, does not capitalise every word's first character
print(name.capitalize())  # prints "Shivraj"

# convert first character of each word to uppercase
n = "shivraj khose"
print(n.title()) # prints "Shivraj Khose"

# trim blank spaces present in start and end of the string
print(n.strip())  # prints "shivrajkhose"

# count occurrence of any substring in the string
print(name.count("shi")) # returns 1 since "shi" exists 1 time in string "name"

# find and return first index of the substring
print(n.find("hose"))  # returns 9 since "hose" substring starts from 9th index 

# replace substring with another substring
print(n.replace("khose","sharma"))  # prints "shivraj sharma"
