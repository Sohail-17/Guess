SECRET_WORD = "python"

def check_guess(guess):
    if not guess:
        return "Please enter a world!"
    if guess.lower() == SECRET_WORD:
        return "Correct! You guessed the word."
    else:
        return "Oops! Wrong guess"
    
    