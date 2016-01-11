
import sys

# to do list: recognize roman numerals and omit lines that begin with roman numerals
# give an option to not be case-sensitive with first-line matches.

def main():
	poemToRead = raw_input("\nWhat poem do you want to search through? \nAnswers should be in the form poemname.txt\n\n")
	nextCommand = ""
	while nextCommand != "exit":
		f = open(poemToRead)
		totalLines = 0
		numberOfStarters = 0
		startingWordToLookFor = raw_input("\nWhat word are we looking for?\n")
		for line in f:
			lineArray = []
			lineArray = line.split()
			if len(lineArray) > 0:
				totalLines += 1
				if lineArray[0] == startingWordToLookFor:
					numberOfStarters += 1
		print "\n", numberOfStarters, "lines begin with \"", startingWordToLookFor, "\"\n"
		print "There are", totalLines, "lines with text on them.\n"
		nextCommand = raw_input("Input your next command - exit to quit, again to search the same poem, new to search a new poem.\n")
		if nextCommand == "new":
			poemToRead = raw_input("What's the new poem you want to search through?")

print "\nWelcome to PoemCounter! This program takes two arguments, a starting word to look for and a file.\n"
print "The file should be saved in the same folder as this snippet of code."
print "This code is case-sensitive!"
print "Note that total line counts ONLY remove blank lines."

main()