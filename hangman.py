from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import re
import os
import random

class English:
    allLetters = "Congratulations! The word you guessed was "
    oneLetter = "You already guessed the letter "
    goodGuess = "Good guess, "
    letterInput = "Guess a letter: "
    lettersGuessed = "Letters guessed: "
    isIn = " is in the word."
    isNotIn = " is not in the word."
    sorry = "Sorry, "
    remaining1 = ""
    remaining2 = " chances remaining."
    gameOver = "You lost. The word was "
    congrats = "Congratulations YOU WON! The word was "
    guess = "Guess the word: ('quit' to give up) "
    gaveUp = "You gave up, the word was "
    quit = 'quit'
    finalGuessQuest = 'Take your final guess: '
    wordSet = ["cat"]

class Polish:
    allLetters = "Odgadłeś słowo "
    oneLetter = "Odgadłeś już literę "
    goodGuess = "Zgadłeś, "
    letterInput = "Podaj literę: "
    lettersGuessed = "Odgadnięte litery: "
    isIn = " znajduje się w słowie."
    isNotIn = " nie znajduje się w słowie."
    sorry = "Niestety "
    remaining1 = "Pozostała liczba prób: "
    remaining2 = "."
    gameOver = "Przegrałeś! Chodziło o słowo "
    congrats = "Gratulacje - wygrałeś! Odgadywane słowo to "
    guess = "Odgadnij słowo: ('koniec' aby zakończyć) "
    gaveUp = "Koniec gry. Odgadywane słowo to "
    quit = 'koniec'
    finalGuessQuest = 'Podejmij ostatnią próbę odgadnięcia słowa: '
    wordSet = ("dom","droga","kajak","kot","pies")

class HangmanE(English):

    def play(self):
        self.guesses = []
        self.guesses_string = ''
        self.bad_guesses = []
        self.chances = 6
        self.word = random.choice(English.wordSet)
        self.wordTuple = tuple(list(self.word.upper()))
        while self.chances > 0:
            printable = []
            for i in self.wordTuple:
                if i in self.guesses:
                    printable.append(i)
                else:
                    printable.append("_")
            print(" ".join(printable))
            if sorted(self.word.upper()) == sorted(self.guesses_string.upper()):
                print("\n" + self.allLetters + self.word.upper() + ".")
                time.sleep(2)
                break
            guess = (input(self.letterInput)).upper()
            if guess in self.guesses or guess in self.bad_guesses:
                print(self.oneLetter + guess + ".")
                continue
            elif guess.upper() in self.word.upper():
                print(self.goodGuess + guess + self.isIn)
                self.guesses.append(guess)
                self.guesses_string = ''.join(self.guesses)
                print(self.lettersGuessed + self.guesses_string)
            else:
                print(self.sorry + guess + self.isNotIn)
                self.bad_guesses.append(guess)
            self.chances -= 1
            print(self.remaining1 + str(self.chances) + self.remaining2)
            time.sleep(0.5)

        if self.chances == 0:
            if sorted(self.word.upper()) == sorted(self.guesses_string.upper()):
                print(self.allLetters + self.word.upper() + '.')
                time.sleep(2)
            elif sorted(self.word.upper()) != sorted(self.guesses_string.upper()):
                self.finalGuess = input(self.finalGuessQuest)
                if self.word.upper() == self.finalGuess.upper():
                    print(self.allLetters + self.word.upper() + '.')
                    time.sleep(2)
                else:
                    print(self.gameOver + self.word.upper() + '.')
                    time.sleep(2)

class HangmanP(Polish):

    def play(self):
        self.guesses = []
        self.guesses_string = ''
        self.bad_guesses = []
        self.chances = 6
        self.word = random.choice(Polish.wordSet)
        self.wordTuple = tuple(list(self.word.upper()))
        while self.chances > 0:
            printable = []
            for i in self.wordTuple:
                if i in self.guesses:
                    printable.append(i)
                else:
                    printable.append("_")
            print(" ".join(printable))
            if sorted(self.word.upper()) == sorted(self.guesses_string.upper()):
                print("\n" + self.allLetters + self.word.upper() + ".")
                time.sleep(2)
                break
            guess = (input(self.letterInput)).upper()
            if guess in self.guesses or guess in self.bad_guesses:
                print(self.oneLetter + guess + ".")
                continue
            elif guess.upper() in self.word.upper():
                print(self.goodGuess + guess + self.isIn)
                self.guesses.append(guess)
                self.guesses_string = ''.join(self.guesses)
                print(self.lettersGuessed + self.guesses_string)
            else:
                print(self.sorry + guess + self.isNotIn)
                self.bad_guesses.append(guess)
            self.chances -= 1
            print(self.remaining1 + str(self.chances) + self.remaining2)
            time.sleep(0.5)

        if self.chances == 0:
            if sorted(self.word.upper()) == sorted(self.guesses_string.upper()):
                print(self.allLetters + self.word.upper() + '.')
                time.sleep(2)
            elif sorted(self.word.upper()) != sorted(self.guesses_string.upper()):
                self.finalGuess = input(self.finalGuessQuest)
                if self.word.upper() == self.finalGuess.upper():
                    print(self.allLetters + self.word.upper() + '.')
                    time.sleep(2)
                else:
                    print(self.gameOver + self.word.upper() + '.')
                    time.sleep(2)


class Communicator():
    clear = lambda: os.system('cls')
    clear()
    print("""
Welcome to the hangman game!
Witamy w grze wisielec!
    """)
    time.sleep(1)
    while True:
        clear()
        try:
            action = int(input("""
Which language would you like to play the game? Type in an appropriate number and hit ENTER:
(1) English.   (2) Polish.   (3) I want to close the program.

W jakim języku chciał(a)byś zagrać w wisielca? Wpisz odpowiedni numer i naciśnij ENTER:
(1) Po angielsku.   (2) Po polsku.   (3) Chcę zamknąć program.
    """))
            if action == 1:
                HangmanE().play()
            elif action == 2:
                HangmanP().play()
            elif action == 3:
                print("""
Closing the program...
Zamykanie programu...
    """)
                time.sleep(1)
                print("""
Program closed.
Zamknięto program.
    """)
                break
            else:
                raise ValueError()
        except ValueError:
            print("""
Type in 1, 2 or 3.
Wpisz 1, 2 lub 3.
            """)
            time.sleep(1)