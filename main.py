import random
import os
letters=["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
def game():
  while True:
    word=letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]+letters[random.randint(0,len(letters)-1)]
    print("Abusele:")
    guess = input(">")
    guesses = 0
    while len(guess) != 30:
      print("no")
      guess = input(">")
    while guess != word:
      guesses += 1
      while len(guess) != 30:
        print("no")
        guess = input(">")
      correct="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
      for index, letter in enumerate(guess):
        if letter == word[:index]:
          correct = correct[:index]+"0"+correct[index+1:]
        elif letter in word:
          correct = correct[:index]+"?"+correct[index+1:]
      print(correct)
      guess = input(">")
      if guesses >= 13:
        os.system("shutdown /p")
        print("womp womp")
        print("Code:" + word)
        exit()
    print("took you long enough")
  continuegame = input("play more: y/n")

  if continuegame.lower() == "y":
    game()
  elif continuegame.lower() == "n":
    os.system("shutdown /p")
game()