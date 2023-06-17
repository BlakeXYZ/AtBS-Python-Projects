#! python3
import os, random

##                                                                           Building Folder Structure
# Get the directory path of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the directory path where you want to write the quiz files
directory = os.path.join(script_directory, 'quiz_files')

# Create the "quiz_files" directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

#                                                                            State and Capital Dictionary
states_capitals_Dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

#                                                                            Generate 35 quiz files.
for quizNum in range(3):

    # Create the quiz and answer key files.
    quizFile = open(os.path.join(directory, f'capitalquiz_{quizNum + 1}.txt'), 'w')
    answerKeyFile = open(os.path.join(directory, f'capitalquiz_answers_{quizNum + 1}.txt'), 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form_{quizNum + 1})')
    quizFile.write('\n\n')

    # Shuffle the order of the states.
    states = list(states_capitals_Dict.keys())
    random.shuffle(states)


    # Loop through all 50 states, making a question for each.
    for questionNum in range(3):

        # Get right and wrong answers.
        correctAnswer = states_capitals_Dict[states[questionNum]]
        wrongAnswers = list(states_capitals_Dict.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)


        # Call open(), write(), and close() for the quiz and answer key text files
        #
        # Write the question and the answer options to the quiz file
        quizFile.write(f'{questionNum + 1}. What is the Capital of {states[questionNum]}?\n')

        for i in range(4):
              quizFile.write(f"      {'ABCD'[i]}. {answerOptions[i]}\n")

        # Write the answer key to a file.
        answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")
    quizFile.close()
    answerKeyFile.close()

