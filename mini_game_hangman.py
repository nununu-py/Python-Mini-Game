import random

STAGES = \
    ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
     '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
     '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
     '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
     '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
     '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
     '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


FILM = ["Captain America", "Spiderman", "Wanda Vision",
        "Black Phanter 2", "Secret Invasion", "Thor", "Avengers"]
ANIME = ["Naruto", "Dragonball", "One Piece", "One Punch Man",
         "Demon Slayer", "Chainsaw Man", "Spy X Familly"]
CARTOON = ["Tom And Jerry", "Spongebob", "Ben 10",
           "Si Dudung", "Upin Ipin", "Boboiboy", "Sopo Jarwo"]


def game(genre, secret_word, display):

    life = 7
    guess_list = []
    info = "WIN"

    while "?" in display:

        guess = input("Guess the letter : ").lower()

        if guess in guess_list and guess.isalpha():

            print(f"You Already Guess With Letter '{guess}'")

        elif guess.isalpha():
            guess_list.append(guess)

            if guess in secret_word.lower():

                for i in range(len(secret_word)):
                    if secret_word[i].lower() == guess:
                        display[i] = secret_word[i]

                print(f"{display}")

            else:
                life -= 1
                print(STAGES[life])

                if life == 0:
                    info = "LOSE"

                    break

        else:
            print("Program Only Accept Alphabet")

    print(f"YOU {info} THE GAMEE, THE SECRET WORD iS {secret_word} from {genre}")


display = []
word = []
genre = ["FILM", "ANIME", "CARTOON"]

user_input = input(
    "What's Genre You Want To Choose 'Film/Anime/Cartoon' : ").upper()

while user_input not in genre:

    print(f"---> {user_input} IS NOT AVAILABLE NOW, TRY AGAIN!")

    user_input = input(
        "What's Genre You Want To Choose 'Film/Anime/Cartoon' : ").upper()

if user_input == "film":
    secret_word = random.choice(FILM)

elif user_input == "anime":
    secret_word = random.choice(ANIME)

elif user_input == "cartoon":
    secret_word = random.choices(CARTOON)

for i in secret_word:

    if i == " ":
        display.append("   ")

    else:
        display.append("?")

print(f"Try to guess this word ---> {display}")

game(genre=user_input, secret_word=secret_word, display=display)
