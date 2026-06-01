import random
secret=(random.randint(1, 100))
attempts=0
guess_num=int(input("Enter the guess no from the user:-"))
while guess_num!=secret:
    attempts+=1
    if guess_num < secret:
        print("Too low!!")
    elif guess_num > secret:
        print("Too high!!")    
    guess_num=int(input("Guess again:"))
print(f"You got it in {attempts} attempts!")
