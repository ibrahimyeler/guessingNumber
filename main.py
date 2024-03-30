import random
def guessNumber(x):
    randomNumber = random.randint(1,x)
    guessNumber = 0
    while guessNumber != randomNumber:
        guessNumber = int(input(f'Guess a number between 1 and {x}: '))
        if guessNumber < randomNumber:
            print('Too low. Please guess another number')
        elif guessNumber > randomNumber:
            print('Too high. Please guess another number.')
        
        
    print (f'CONGRATULATIONS! You guessed the number {randomNumber} correctly')


    
guessNumber(100)