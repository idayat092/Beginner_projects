import random
from time import sleep

def magic_8_ball():
    
    responses = ['As I see it, yes', 'Ask again later', 'Better not tell you now', 'Cannot predict now',
                 'Concentrate and ask again',
                 'Don’t count on it', 'It is certain', 'It is decidedly so', 'Most likely', 'My reply is no',
                 'My sources say no',
                 'Outlook not so good', 'Outlook good', 'Reply hazy, try again', 'Signs point to yes', 'Very doubtful',
                 'Without a doubt',
                 ' Yes', 'Yes - definitely', 'You may rely on it']

    question = input("Ask your question: ")

    if len(question) <= 1:
        print("Enter a Valid question")

    else:
        print("Thinking...")
        sleep(1)
        response = random.choice(responses)
        print("Answer: " + response)

    next_action = input("Will you like to ask another question or quit? [input Ask or Quit]")

    if next_action == "Ask":
        magic_8_ball()

    else:
        print("Thank you for playing")


magic_8_ball()
