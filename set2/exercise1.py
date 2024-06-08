"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think this will create a list with several strings in it
some_words = ["what", "does", "this", "line", "do", "?"] # it initialised a list with several strings in it!

# I think this will loop over each string in the list
for word in some_words: # it loops over each of those strings
    # i think it will print the string to the console (the given one for this part of the execution in the for loop)
    print(word) # it does print the string to the console

# exact same thing as above except the bound variable is x rather than word (ie. every time we loop x will be assigned to the next word in some_words)
for x in some_words: # same as explained above!
    # similar to above it will print out each word to the console - one line per word from some_words
    print(x) # does exactly that :)

# prints the entire list as > ["what", "does", ...]
print(some_words) # does that but actually uses single quotes rather than double (these are mostly interchangeable in python with some exceptions)

# checks the length of some_words (would be 6) and as it is greater than 3, we will enter the indented code block
if len(some_words) > 3: # does exactly that :)
    # prints out the given string to the console
    print("some_words contains more than 3 words") # prints that string to the console

# defines a function called usefulFunction with no input args
def usefulFunction(): # does exactly that!
    # multiline comment
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    # i think it prints out username for the device I'm using
    print(platform.uname()) # it prints out the username and also a bunch of system info about my system like the kernel version and processor type

# calls the function usefulFunction defined above (this will cause it to execute the code within the function and output the device info of my device)
usefulFunction() # does exactly that!
