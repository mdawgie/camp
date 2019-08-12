import random
def main():
  
  ans = random.randint(1,1000)
  print("Welcome to the random number guessing game")
  tries = 4
  while (tries>0):
     guess = int(input("guess a number between 1 and 1000:  "))
     if (ans == guess):
       print("You win!")
       break
     elif (guess>ans):
       print("guess is too big")
       tries =  tries - 1
     else:
       print("Guess is to small")

  
  
if __name__== "__main__":
    main()
    
    
    