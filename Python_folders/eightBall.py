import random as rnd
def eight_ball():
    answers = [
        "Yes, definitely.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes, in due time.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    return rnd.choice(answers)

if __name__ == "__main__":
    print("Welcome to the Magic 8-Ball!")
    question = input("Ask a yes or no question: ")
    if question.strip():
        print("Magic 8-Ball says:", eight_ball())
    else:
        print("Please ask a valid question.")