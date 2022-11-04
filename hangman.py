import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')

empty_list = []
for letter in chosen_word:
    empty_list += "_"
#empty = "_"*len(chosen_word)
#empty_list = list(empty)
print(HANGMANPICS[0])
print(empty_list)

x = 6
y = 0
z = 0
count_ = len(chosen_word)
while x > 0 and count_ != 0 and z <= len(chosen_word):
    user_input = input("Guess a letter: ").lower()
    if user_input in chosen_word:
        for n in range(0,len(chosen_word)):
            if chosen_word[n] == user_input:
                empty_list[n] = user_input
        print(empty_list)
        count_ = empty_list.count("_")
        z += 1
    else:
        x -= 1
        y += 1
        print(HANGMANPICS[y])
if x == 0:
    print("Gameover!, You lost")
elif count_ == 0:
    print("Gameover!, You Won")
elif z > len(chosen_word):
    print("Gameover! You exhausted your number of chances")
        
 