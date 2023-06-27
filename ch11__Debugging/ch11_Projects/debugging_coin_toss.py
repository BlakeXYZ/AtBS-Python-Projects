#! python3

#### Debugging Coin Toss

# The following program is meant to be a simple coin toss guessing game. The
# player gets two guesses (it’s an easy game). However, the program has several
# bugs in it. Run through the program a few times to find the bugs that keep
# the program from working correctly.

####

import random, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL) # Disable Logging



logging.debug('Start of program')
guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

if guess.lower() == 'tails':
    guess = 0
else:
    guess = 1

logging.debug(f'Guess equals: {guess}')

toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug(f'Toss rand int equals: {toss}')


if toss == guess:
    print('You got it!')
else:
    while guess not in ('heads', 'tails'):
        print('Nope! Guess again!')
        guess = input()

    if guess.lower() == 'tails':
        guess = 0
    else:
        guess = 1

    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

logging.debug('End of program')
