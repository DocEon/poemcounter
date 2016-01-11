
import sys

# to do list: recognize roman numerals and omit lines that begin with roman numerals
# give an option to not be case-sensitive with first-line matches.

def main():
	poemToRead = raw_input("What poem do you want to search through? Answers should be in the form poemname.txt\n")
	keepGoing = True
	while keepGoing:
		f = open(poemToRead)
		totalLines = 0
		numberOfStarters = 0
		startingWordToLookFor = raw_input("What word are we looking for?\n")
		for line in f:
			lineArray = []
			lineArray = line.split()
			if len(lineArray) > 0:
				totalLines += 1
				if lineArray[0] == startingWordToLookFor:
					numberOfStarters += 1
		print numberOfStarters, "lines begin with", startingWordToLookFor
		print "There are", totalLines, "lines with text on them."
		nextCommand = raw_input("Input your next command - exit to quit, again to search the same poem, new to search a new poem.\n")
		if nextCommand == "new":
			poemToRead = raw_input("What's the new poem you want to search through?")
		elif nextCommand == "exit":
			keepGoing = False

print "Welcome to PoemCounter! This program takes two arguments, a starting word to look for and a file."
print "The file should be saved in the same folder as this snippet of code."
print "This code is case-sensitive!"
print "Note that total line counts ONLY remove blank lines - if there are stanza markers, you'll need to count those yourself."
main()
