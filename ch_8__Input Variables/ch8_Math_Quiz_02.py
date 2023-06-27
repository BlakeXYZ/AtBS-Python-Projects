import pyinputplus as pyip
import random, time

# Set Question Total Count and Question Current Count variables
totalQuestionCount = 3
correctAnswers = 0


for questionCount in range(totalQuestionCount):
    # Generate two random numbers between 1 and 10
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = '#%s: %s x %s = ' % (questionCount + 1, num1, num2)
    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print(f'Out of time! The correct answer is: {num1 * num2}')
    except pyip.RetryLimitException:
        print(f'Out of tries! The correct answer is: {num1 * num2}')
        
    else:
        # this blocks run if there is no exceptions hit
        print('Correct!')
        correctAnswers += 1

    # Wait for 1 second after each question
    time.sleep(1)

# once current question number equals question total count
# break the multiply loop and print:
# Number of Correct questions answered

# Print quiz results
print('You scored %s out of %s.' % (correctAnswers, totalQuestionCount))
                                        


