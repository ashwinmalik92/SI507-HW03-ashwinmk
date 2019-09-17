# asks user to submit their question
# param: none
# returns: user question
def get_question():
    question = input('What is your question? ')
    return(question)

# checks if user asked a question
# param: question
# returns: none
def check_question(question):
    if question[-1] == "?":
        provide_answer()
    elif question == 'quit':
        pass
    else:
        print('I\'m sorry, I can only answer questions.')

# main program
question = ''
while question != 'quit':
    question = get_question()
    check_question(question)