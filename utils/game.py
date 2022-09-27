
import random

class Hangman:
    """_summary_ this is a class for the game "Hangman", it has all the methods and attributes to run the game.
    :param possible_words: this gives a pool of words the computer will select "word to find" from
    :param lives: this gives how many guesses you have before you begin the game, each wrong guess, you loss 1 life.
    """
    possible_words = ['becode', 'learning', 'mathematics', 'sessions']
    
    def __init__(self, lives=5):
        self.word_to_find = list(random.choice(Hangman.possible_words))
        self.lives = lives
        self.correctly_guessed_letters = ["_"] * len(self.word_to_find)
            
        self.wrongly_guessed_letters= []
        self.turn_count = 0
        self.error_count = 0
        
                
    def play(self):
        """_summary_this gives the main part of the game itself, you have to pick a letter and find if the letter is or not in the "word to find"
        """
        print('Please enter a letter:')
        guessed_letter = input()
        while not guessed_letter.isalpha():
            guessed_letter = input()

        for i, letter in enumerate(self.word_to_find):
            if letter == guessed_letter:
                self.correctly_guessed_letters[i] = guessed_letter

        if guessed_letter not in self.word_to_find:
            self.wrongly_guessed_letters.append(guessed_letter)
            self.error_count +=1
            self.lives -=1

        print(f"the letter is: {self.correctly_guessed_letters}")
        print(f"the wrongly guessed letters are:. {self.wrongly_guessed_letters}")
        
    def start_game(self):
        """_summary_this is the function to start the game and make the counts, and linked to other methods inside the class
        """

        while True:
            self.play()
            self.turn_count+=1
            
            if self.word_to_find == self.correctly_guessed_letters:
                self.well_played()
                break

            elif self.lives == 0:
                self.game_over()
                break

    def game_over(self):
        """_summary_tell you that game is over, you lost
        """
        print('Game Over')

    def well_played(self):
        """_summary_give a result of the performance of you on the game when it is over and when you won
        """
        print(f"You found the word:{self.word_to_find},in {self.turn_count} turns with {self.error_count} errors")
