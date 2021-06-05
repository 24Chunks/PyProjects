import random

capital_dic = {
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
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
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
    'Neveda': 'Carson City',
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
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
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

# TODO: CREATE 35 QUIZES
for quiz_num in range(35):
    # TODO: CREATE QUIZ AND ANSWER KEY FILES
    quiz_file = open(f'quizes/quiz{quiz_num}.txt', "w")
    answer_key_file = open(f'quizes/quiz{quiz_num}answer_KEY.txt', "w")

    # TODO: WRITE HEADER FOR QUIZ
    quiz_file.write(f"Name:\n\nDate:\n\nPeriod:\n\n" + "\n")
    quiz_file.write(" "*20 + f"State Capitals Quiz (Form {quiz_num + 1})" + "\n")

    answer_key_file.write(f"QUIZ #{quiz_num + 1}: ANSWER KEY".center(60, "*") + "\n")

    # TODO: SHUFFLE ORDER OF STATES
    # state_l = list()
    # for state in capital_dic:
    #     state_l.append(state)
    state_l = list(capital_dic.keys())
    random.shuffle(state_l)

    # TODO: LOOP THROUGH ALL 50 STATES MAKING A QUESTION FOR EACH
    for question_num, state in enumerate(state_l):
        correct_answer = capital_dic[state]
        answers_l = [correct_answer]

        for random_ans in range(3):
            # PREVENT FROM GETTING DUPLICATE ANSWERS
            random_state = state_l[random.randint(0,49)]
            while capital_dic[random_state] in answers_l:
                random_state = state_l[random.randint(0, 49)]

            random_answer = capital_dic[random_state]
            answers_l.append(random_answer)

        random.shuffle(answers_l)

        choices = "ABCD"
        question = f"{question_num + 1}. Whats the capital of {state}:\n"
        for i in range(len(choices)):
            question += f"\t{choices[i]}) {answers_l[i]}\n"

        quiz_file.write(question + "\n")

        # TODO: WRITE ANSWER KEY
        for i in range(len(answers_l)):
            if answers_l[i] == capital_dic[state]:
                answer_key_file.write(f"{question_num+1}. {choices[i]} \n")



    # CLOSE FILES
    quiz_file.close()
    answer_key_file.close()
