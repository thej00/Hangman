import random
import string
from words import words
HANGMAN_PICS = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
       +---+
       O   |
       |   |
           |
          ===''', '''
       +---+
       O   |
      /|   |
           |
          ===''', '''
       +---+
       O   |
      /|\  |
           |
          ===''', '''
       +---+
       O   |
      /|\  |
      /    |
          ===''', '''
       +---+
       O   |
      /|\  |
      / \  |
          ===''']
HANGMAN_PICS.reverse()
def get_word():
    word=random.choice(words)
    while  ' ' in word or '-' in word:
         word=random.choice(words)
    return word
def hangman():
    word=get_word().upper()
    word_letters=set(word)
    alphabets=set(string.ascii_uppercase)
    used_letters=set()
    lives=6
    while len(word_letters)!=0 and lives>0:
        print('you have',lives,'lives and you have used','-'.join(used_letters),'letters')
        print()
        word_list=[letter if letter in used_letters else '_' for letter in word]
        print('Current Status:',''.join(word_list))
        print()
        user=input('guess a letter: ').upper()
        if user in alphabets-used_letters:
            used_letters.add(user)
            if user in word_letters:
                word_letters.remove(user)
                print()
            else:
                lives-=1
                print('letter is not in the word')
                print(HANGMAN_PICS[lives])
                print()
        elif user in used_letters:
            print('you already guessed that letter')
            print()
        else:
            print('invalid letter!!')
            print('')

    if lives==0:
        print('you died!! the word is ','------',word,'------')
        print()
    else:
        print('-----',word,'-----','\n','yay! you guessed the word')
        print()

hangman()
