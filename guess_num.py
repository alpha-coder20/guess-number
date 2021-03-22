import time

print("***Welcome to Guess The Number Game***")
n = 18
for i in range(9):
    inp = int(input("Enter Your Guess: "))
    if inp>n:
        print("Your guess is greater than the number")
        print( 8-i, "guesses left.")
    elif inp<n:
        print("Your guess is lesser than the number")
        print( 8-i, "guesses left.")
    else:
        print("Congrats you guessed right.")
        break
if inp==n:        
    print("You took", i+1, "guesses to crack the number.")
else:
    print("Game Over ! Play Again.")

time.sleep(5)