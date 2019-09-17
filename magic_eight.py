import random

# asks user to submit their question
# param: none
# returns: user question
def get_question():
    question = input('What is your question? ')
    return(question)

answers = ["It is certain.","It is decidedly so.", "Without a doubt.", "Yes- definitely", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you know.", "Cannot predict now.", "Concentrate and ask again.","Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.","Very doubtful."]

def provide_answer():
    index = random.randint(0,19)
    return answers[index]

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
