import sys
import time

def program():
	zero = 0
	nRestart = ["restart", "r", '1']
	nQuit = ["n", "no", "q", "quit", '2']
	number = float(input("\nEnter a number: "))
	if number > zero:
		print("\n",number," is positive.\n")
		restart = input("\nrestart or quit: ").lower()
		if restart in nRestart:
			print("\nprogram restarting in 2sec...")
			time.sleep(2)
			program()
		if restart in nQuit:
			print("\nclosing program in 2sec...")
			time.sleep(2)
			def exitProgram():
				sys.exit()
				exitProgram()
			exitProgram()
	if number < zero:
		print("\n",number," is negative.\n")
		restart = input("\nrestart or quit: ").lower()
		if restart in nRestart:
			print("\nprogram restarting in 2sec...")
			time.sleep(2)
			program()
		if restart in nQuit:
			print("\nclosing program in 2sec...")
			time.sleep(2)
			def exitProgram():
				sys.exit()
				exitProgram()
			exitProgram()
	if number == zero:
		print("\n",number," is neutral.\n")
		restart = input("\nrestart or quit: ").lower()
		if restart in nRestart:
			print("\nprogram restarting in 2sec...")
			time.sleep(2)
			program()
		if restart in nQuit:
			print("\nclosing program in 2sec...")
			time.sleep(2)
			def exitProgram():
				sys.exit()
				exitProgram()
			exitProgram()
program()
