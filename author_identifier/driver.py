import nltk
import os

# this is a CLI to manage the entire process

print("Welcome to the Markov model supervised machine learning tool.")
print("This is the root prompt. Before proceeding, please follow the instructions that will appear:\n")

def setWorkingDir():
	workingDirectory = input("Please set working directory.\nTo select last accessed directory, enter # (hash).")

	if workingDirectory is "#":
		try:
			txtfile = open("MarkovModel/last.txt",'r')
			workingDirectory = txtfile.read()
			txtfile.close()
			print("Good, you have selected your working directory as %s."%workingDirectory)
			print("This is the directory housing all your materials pertaining to any one project.")
		except:
			print("Error: no recent directory in record. Please try again from main menu.\n")
	else
		print("Good, you have selected your working directory as %s."%workingDirectory)
		print("This is the directory housing all your materials pertaining to any one project.")
		txtfile = open("MarkovModel/last.txt",'w')
		txtfile.write(workingDirectory)
		txtfile.close()
	
flag = True

while flag:
	print("Welcome to the main menu. Please make a choice and enter the corresponding number.")
	print("1 - Change working directory. (Your current directory is:\n    %s)"%workingDirectory)
	print("2 - ")
	
	choice = input("Please choose from above options and input the number (only): ")
	if choice in range(7):
		vars()["function by-name"]() # to call a function dynamically using local variables.
