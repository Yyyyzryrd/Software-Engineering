storing data in programs

- pep8 recommends use of snake_case for python's variables
-


integers are whole numbers
floats are numbers with running decimals
strings are similar to nouns, in that they are more "ideas". "92" can be a string, while 92 is an integer
characters are single letters, numbers, punctuation, etc
booleans represent two modes; True or False

we are able to change the type of a variable. we can do this through casting, which is shown below:

number = "30"
#this means that number is a string
int(number) #will use number as if it was an integer. this does not permanently change number into an int, it just acts like
			#an int for this time. 
			#you can't change something invalid into an integer. you can't change "dave" into an int

f-string = formatted string. 