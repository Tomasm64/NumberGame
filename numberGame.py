# Modules
import random

# Initialization
random.seed()

# Variables
chances = [10,5,3]
attempts = 0
gameReady = False
keepPlaying = True
answer = random.randint(1,100)

while(keepPlaying):
	print("Temp: " + str(answer))
	print("Welcome to the number guessing game!")
	print("I'm thinking of a number between 1 and 100.")
	print("You have a limited number of guesses.\n")
	print("Difficulty Settings")
	print("1. Easy (10 chances)")
	print("2. Medium (5 chances)")
	print("3. Hard (3 chances)\n")

	while(not gameReady):
		difficulty = input("Make a selection: ")
		if(difficulty != "1" and difficulty != "2" and difficulty != "3"):
			print("Please choose a number between 1 and 3")
		else:
			chancesLeft = chances[int(difficulty) - 1]
			print("You have " + str(chancesLeft) + " chances.")
			gameReady = True

	while(chancesLeft > 0):
		attempts += 1
		guess = input("Guess a number: ")
		if(not guess.isdigit()):
			print("Please enter a valid number between 1 and 100")
		else:
			guess = int(guess)
			if(guess == answer):
				print("Congratulations! The answer was "+str(answer))
				print("You got the answer in "+str(attempts)+" attempt(s)\n")
				break
			else:
				chancesLeft -= 1
				if(chancesLeft <= 0):
					print("Game over. The correct answer was "+str(answer)+"\n")
				else:
					if(guess < answer):
						print("Wrong, too low")
					else:
						print("Wrong, too high")
					print(str(chancesLeft) + " more chance(s)")

	playAgain = input("Keep playing? (y/N): ")
	if(playAgain == "y" or playAgain == "Y"):
		keepPlaying = True
		answer = random.randint(1,100)
		gameReady = False
		attempts = 0
	else:
		keepPlaying = False
		print("\nThank you for playing. Goodbye!\n")
