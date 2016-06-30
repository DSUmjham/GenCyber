#!/usr/bin/python

first = 65 # 65 represents a 'A'
second = 97 # 97 represents an 'a'
third = 0
pattern = ""

print "buf = (" 

for count in range (0, 26):
	pattern = "" # blank out the pattern variable, helps with formatting in the print later
	second = 97 # make sure to start at 'a' for the second digit

	# this for loop increments the second digit, should always be a lowercase letter
	for count2 in range (0, 26):
		third = 0 #the third digit needs to start at 0
		
		# this for loop increments the third digit, should always be an int
		for count3 in range (0, 10):
			pattern += chr(first) + chr(second) + `third` # combine our three vairables (Uppercase, lowercase, number)
			third += 1 # increment the third character by 1 (number)

		second += 1 # increment the second character by 1 (lowercase)
		

	first += 1 # increment the first character by 1 (uppercase)
	print "\"" + pattern  + "\"" # print out our new line of the pattern

#print pattern #print out what we have in one large string
print ")"
