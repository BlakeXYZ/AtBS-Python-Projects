import pyinputplus as pyip

# def addsUpToTen(numbers):
#     numbersList = list(numbers)
#     for i, digit in enumerate(numbersList):
#         numbersList[i] = int(digit)
#     if sum(numbersList) != 10:
#         raise Exception('The digits must add up to ten, not %s' % (sum(numbersList)))
#     return int(numbers) # return an int form of numbers


# response = pyip.inputCustom(addsUpToTen)

############
############
############

while True:
    myPrompt = 'Want to know how to keep a goober busy for hours?\n'
    response = pyip.inputYesNo(myPrompt)
    if response == 'no':
        break
print('Thank You')





