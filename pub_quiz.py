# Function to check whether the response input matches the correct answer
def check_answer(response, answer):

    # Global variable for tracking score
    global score

    # Execute if response matches the correct answer
    if response.lower() == answer.lower():

        # Increment score counter
        score += 1

        # Give feedback and updated score
        print('Correct answer!  Your current score is ' + str(score) + '.')

    # Execute if response doesn't match the correct answer
    else:

        # Give feedback
        print('Sorry, the answer was ' + answer + '.  Moving on...')

# Set score to 0 at the beginning
score = 0

# Introduce quiz
print('Try your luck in our Pub Quiz!')

# Questions and function call to check answers
# Example questions from www.freepubquiz.co.uk/multiple-choice-quiz.html
response1 = input('In which city did poet John Keats die?\n \
A) Rome\n B) Paris\n C) London\n \
Type A, B or C\n ')
check_answer(response1, 'A')

response2 = input('Which two states border Florida?\n \
A) Alabama and Georgia\n B) Alabama and Louisiana\n C) Georgia and Louisiana\n \
Type A, B or C\n ')
check_answer(response2, 'A')

response3 = input('The first ever commercial bungie jump took place in which country?\n \
A) South Africa\n B) Australia\n C) New Zealand\n \
Type A, B or C\n ')
check_answer(response3, 'C')

response4 = input('Britain\'s first black archbishop became bishop of where in 2005?\n \
A) Durham\n B) York\n C) Canterbury\n \
Type A, B or C\n ')
check_answer(response4, 'B')

response5 = input('Who played Colonel Pickering in the 1964 Film, My Fair Lady?\n \
A) Wilfrid Hyde-White\n B) Rex Harrison\n C) Stanley Holloway\n \
Type A, B or C\n ')
check_answer(response5, 'A')

response6 = input('The river Senne flows through which capital city?\n \
A) Amsterdam\n B) Brussels\n C) Copenhagen\n \
Type A, B or C\n ')
check_answer(response6, 'B')

response7 = input('Who is the protagonist of Victor Hugo\'s 1862 novel, Les Miserables?\n \
A) Jean Valjean\n B) Jean Piaget\n C) Jean Seri\n \
Type A, B or C\n ')
check_answer(response7, 'A')

response8 = input('When did the British children\'s TV programme Blue Peter first air?\n \
A) 1958\n B) 1968\n C) 1978\n \
Type A, B or C\n ')
check_answer(response8, 'A')

response9 = input('Who was the fourth man to walk on the moon?\n \
A) Mr. Bean\n B) Mr. Darcy\n C) Mr. Kipling\n \
Type A, B or C\n ')
check_answer(response9, 'A')

response10 = input('Who was king during the Peasant\'s Revolt?\n \
A) King John\n B) Henry III\n C) Richard II\n \
Type A, B or C\n ')
check_answer(response10, 'C')

response11 = input('Where did Disney open a resort on June 16, 2016?\n \
A) Singapore\n B) Shanghai\n C) Tokyo\n \
Type A, B or C\n ')
check_answer(response11, 'B')

response12 = input('What was Charles Dickens\' first novel?\n \
A) The Pickwick Papers\n B) The Old Curiosity Shop\n C) Oliver Twist\n \
Type A, B or C\n ')
check_answer(response12, 'A')

#End of the questions, give final score
print('And that\'s the last of the questions.  Your final score is ' + str(score) + ' out of 12.')

