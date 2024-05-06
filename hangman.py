import random
from words import easy_words,medium_words,hard_words

def intro():
    print("welcome to the game!")
    difficulty_given = False
    while difficulty_given==False:
      level = input("choose your level of difficulty     easy / medium / hard ").lower()
      if (level == "easy") or (level == "medium") or (level == "hard"):
         difficulty_given = True
         continue
      print("invalid level. Try again.")
    return level


def get_word(level):
   if level == "easy":
      word = str(random.choices(easy_words))
      return word.upper()
   elif level == "medium":
      word = str(random.choices(medium_words))
      return word.upper()
   elif level == "hard":
      word = str(random.choices(hard_words))
      return word.upper()
   

def play(word):
   word = word[2:-2]
   letters_unguessed = "_" * len(word)
   guessed = False 
   guessed_letters = []
   guessed_words = []
   tries = 6

   print("Let the game begin!")
   print(display_hangman(tries))
   print(letters_unguessed + "\n")

   while not guessed and tries >0 :
      guess = input("please guess a letter or word? ").upper()
      if len(guess)==1 and guess.isalpha():
         if guess in guessed_letters:
            print("you already guessed the letter", guess)
         elif guess not in word:
            print(guess, "is not in the word.")
            tries-= 1
            guessed_letters.append(guess)
            print(display_hangman(tries))
         else:
            print("Well done! " + guess + " is in the word!")
            guessed_letters.append(guess)
            words_as_list = list(letters_unguessed)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
               words_as_list[index]= guess
            letters_unguessed = "".join(words_as_list)
            print(letters_unguessed)
            if "_" not in letters_unguessed:
               guessed = True
      
      elif len(guess)==len(word) and guess.isalpha():
         if guess in guessed_words:
            print("You already guessed the word ", guess)
         elif guess != word:
            print(guess, "is not the word")
            tries-= 1
            guessed_words.append(guess)
            print(display_hangman(tries))
         else: 
            guessed = True
            letters_unguessed = word

      else:
         print("Invalid guess:(")

   if guessed:
      print("Congrats, you won!")
      return
   else:
      print("sorry you ran out of tries, the word was ", word)
      return
      

def display_hangman(tries): 
   stages = stages = [
    """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """
]
   return stages[tries]




def main():
   level = intro()
   word = get_word(level)
   play(word)
   response = input("Play Again? (Y/N) ").upper()
   while response == "Y":
      level = intro()
      word = str(get_word(level))
      play(word)
      response = input("Play Again? (Y/N) ").upper()
   print("Thank you for playing!")


if __name__ == "__main__":
   main()