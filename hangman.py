HANGMANPICS = [''' 
     +----+
     |    |
          |
          |
          |
          |
          |
===========''',''' 
     +----+
     |    |
     O    |
          |
          |
          |
          |
===========''',''' 
     +----+
     |    |
     O    |
     |    |
          |   
          |
          |
===========''','''
     +----+
     |    |
     O    |
    /|    |
          |
          |
          |
===========''','''
     +----+
     |    |
     O    |
    /|\   |
          |
          |
          |
===========''','''
     +----+
     |    |
     O    |
    /|\   |
    /     |
          |
          |
===========''','''
     +----+
     |    |
     O    |
    /|\   |
    / \   |
          |
          |
==========='''
]



def cls():
	print ('\n' * 100)

def displayBoard(HANGMANPICS, missedLetters, correctLetters,word):
	print(HANGMANPICS[len(missedLetters)])
	print()

	print('Missed Letters:', end=' ')
	for letter in missedLetters:
		print (letter, end=' ')
	print()

	blanks = '_' * len(word)

	for i in range(len(word)):#replace blanks with correctly guessed words
		if word[i] in correctLetters:
			blanks = blanks[:i]+word[i]+blanks[i+1:]

	for letter in blanks:#show word with spaces between each  letter
		print (letter, end=' ')
	print()

def getGuess(alreadyGuessed):
	#Returns the letter the player enteres. Function ensures player enters only single letter
	while True:
		print('Guess a letter.')
		guess = input()
		guess = guess.lower()
		if len(guess) != 1:
			print('Please enter a single letter')
		elif guess in alreadyGuessed:
			print('You have already guessed that letter, choose again')
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print('Please enter a LETTER!!')
		else: 
			return guess

def playAgain():
	#Returns true if player wants to play again else false
	print('Do you wish to play again?')
	return input().lower().startswith('y')

#Main begins here
print ('H A N G M A N')
missedLetters=''
correctLetters=''
word = input('Enter word to be guessed:')
cls()
gameIsDone = False

while True:
	displayBoard(HANGMANPICS,missedLetters,correctLetters,word)
	#Let the player type in a letter.
	guess = getGuess(missedLetters + correctLetters)

	if guess in word:
		correctLetters = correctLetters + guess

		#Check if player has won
		foundAllLetters = True
		for i in range(len(word)):
			if word[i] not in correctLetters:
				foundAllLetters = False
				break
		if foundAllLetters:
			print('Yes! The secret word is "'+word+'"! You have won!') 
			gameIsDone = True
	else:
		missedLetters = missedLetters + guess

	#Check if player has guessed too many times 
		if len(missedLetters) == len(HANGMANPICS) - 1:
			displayBoard(HANGMANPICS,missedLetters,correctLetters,word)
			print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and '+str(len(correctLetters))+' correct guesses, the word was "'+ word +'"')
			gameIsDone = True

#Ask player if they want to play again(but only if game is done).
	if gameIsDone:
		if playAgain():
			missedLetters = ''
			correctLetters = ''
			gameIsDone = False
			word = input('Enter the word to guess: ')
		else:
			break
