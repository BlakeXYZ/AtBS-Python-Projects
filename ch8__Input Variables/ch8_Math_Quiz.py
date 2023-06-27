import pyinputplus as pyip
import random, time

numberOfQuestions = 3
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    # pick two random numbers
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)

    try:
        # right answers by allowRegexes
        # wrong answers by blockRegexes

        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # This runs if no exceptions were raised in the try
        print('Correct!')
        correctAnswers += 1

    # brief pause to let user read result
    time.sleep(1)

    if questionNumber != numberOfQuestions - 1:
        print('Score %s / %s' % (correctAnswers, numberOfQuestions))
        print(f'Score {correctAnswers} / {numberOfQuestions}')

    else:
        print("The End, Your Final Score = %s / %s" % (correctAnswers, numberOfQuestions))










     







