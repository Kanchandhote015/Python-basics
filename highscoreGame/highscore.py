# the game() function in a program lets a user play a game and returns the score as an integer

import random


def game():
  print("You are playing the game.")
  score = random.randint(1, 62)

  # fetch the high score
  with open("highscore.txt") as f:
    highscore = f.read()
    if(highscore != ""):
      highscore = int(highscore)
    else:
      highscore = 0

  print(f"Your score : {score}")
  if(score > highscore):
    # write this hihscore to the file
    with open("highscore.txt", "w") as f:
      f.write(str(score))

  return score  

game()
