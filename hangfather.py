#Notes: Fix Bugs 

import random

game_loop = True
words = []
head = "   O"
upper = "   |"
arms = "  /|\\"
lower = "   |"
legs = "  / \\"

# Messages
head1 = "   O Help! Please I have a family!"
head2 = "   O I have money is that what you want!?"
head3 = "   O AHHHH! It hurts!"
head4 = "   O just... let me see... my wife one more time..."

print("Guess the unknown word correctly")
print("so this man is not brutally murdered!")
print("*Note* all characters must be lower case!\n")

# Checks if the letter has already been guessed
def guessCheck(guessedLetter, guessedCharacters):
    for word in guessedCharacters:
        if guessedLetter == word:
            return True

def  letterCheck(guessedLetter):
    count = 0
    guessableCharacters = "abcdefghijklmnopqrstuvwxyz"
    for char in guessableCharacters:
        if guessedLetter != char:
            count += 1
    if count >= 26:
        return False
    return True

# Opens a file with 1000 different words and enters them into the list
with open("1-1000.txt", "r") as content:
    words = content.read().split()
                
while game_loop == True:
    word = ""
    # If the list runs out of words then the game ends
    count = 0
    unknown = []
    guessedCharacters = []
    word = random.choice(words)
    words.remove(word)
    length = len(word)
    # Find the length of word in underscores
    for i in range(length):
        unknown.append("_ ")
    current_game = True
    while current_game == True:
        # reset
        index = 0
        temp = 0
        # Checks if you won
        if length == 0:
            print("You won!")
            print("The word was: " + word)
            if len(words) == 0:
                print("Out of Words")
                current_game = False
                game_loop = False 
            run_again = input("Would you like to play again? (yes/no)")
            if run_again == "yes" or run_again == "Yes":
                current_game = False
                print("\n\n")
            else:
                current_game = False
                game_loop = False 
            break
        # Word Bank
        print("\nWord Bank: ", guessedCharacters)
        # Checks how many guesses you have and print the boy
        if count <= 2:
            print(head + "\n" + upper + "\n" + arms + "\n" + lower + "\n" + legs + "\n")
        elif count > 2 and count <= 4:
            print(head1 + "\n" + upper + "\n" + arms + "\n" + lower + "\n")
        elif count > 4 and count <= 6:
            print(head2 + "\n" + upper + "\n" + arms + "\n")
        elif count > 6 and count <= 8:
            print(head3 + "\n" + upper + "\n")
        elif count > 8 and count <= 10:
            print(head4 + "\n")
        else:
            # Losing message
            print("You are out of body parts to gamble!")
            print("The word was: " + word)
            # This needs work
            run_again = input("Would you like to play again? (yes/no)")
            if run_again == "yes":
                current_game = False
                break
            else:
                current_game = False
                game_loop = False
                break
        # Shows how many letters are left
        for char in unknown:
            print(char, end="")
        # Checks to see if their guess is correct
        guess = input("\n\nGuess a character! ")
        while not letterCheck(guess):
             guess = input("\n\nGuess a valid character! ")
             beenGuessed = guessCheck(guess, guessedCharacters)
        # Repeat Check
        beenGuessed = guessCheck(guess, guessedCharacters)
        while beenGuessed and not letterCheck(guess):
            print("You already guessed this letter.")
            guess = input("\n\nGuess a new character! ")
            beenGuessed = guessCheck(guess, guessedCharacters)
            
        # Length Check 
        while len(guess) > 1 and not beenGuessed and not letterCheck(guess):
            print("Enter a single character.")
            guess = input("\n\nGuess a character! ")
            beenGuessed = guessCheck(guess, guessedCharacters)
            print("You already guessed this letter.")
        guessedCharacters.append(guess)

        for char in word:
            index += 1
            if guess == char:
                # needs to put characters in correct position
                word.replace(char, " ", index - 1)
                unknown[index - 1] = char
                temp += 1
                length -= 1
        if temp == 0:
            print("Incorrect!\n")
            count += 1
        elif temp == 1:
            print("You just got a letter!")
        else:
            print("You just got multiple letters!")
            
            
                
        
