'''
This is a reference file for the main hangman.
Please note: This is not my work or property.
These two lists are courtasy of github @chrishorton.
The original repository is chrishorton/hangmanwordbank.py
or 
https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c

I am using this file in part of Assignment 5A in CISC101 at Queens.
Student Number: <Blocked>

(I dont know how to properly cite another program that I did not write in a program)..? 
The repo does not have a licence so I am not sure how to properly cite it in order to align
with Queen's accademic integrity standards, I am aware this program is not for marks so I assume this is enough.

'''
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

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
 
