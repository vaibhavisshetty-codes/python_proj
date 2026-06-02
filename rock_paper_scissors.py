#rock,paper,scissor python model
import random
choices=["rock","paper","scissors"]
comp=random.choice(choices)
guess=str(input("Enter the user choice:-"))
print(f"Computer chose: {comp}")
if guess==comp:
    print("Its a Draww!!")
elif(guess=="rock" and comp=="scissors")or\
    (guess=="paper" and comp=="rock")or\
    (guess=="scissors" and comp=="paper"):
        print("User wins!!")
else:
    print("computer wins")
