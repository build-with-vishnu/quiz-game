print("Welcome to your quiz game")

play = input("Are u ready to play the game?(Yes/no)").lower()
if play!= "yes" :
    print("Maybe next time!")
    quit()
else:
    print("Lets start the game")

score=0

ans = input("What is the full form of CPU? ").lower()
if ans=="central processing unit":
    print("You are correct\n")
    score +=1
else:
    print("You are wrong\n")
    score +=0

ans1 = input("What is the full form of GPU? ").lower()
if ans1=="graphics processing unit":
    print("You are correct\n")
    score +=1
else:
    print("You are wrong\n")
    score +=0

ans2 = input("What is the full form of RAM? ").lower()
if ans2=="random access memory":
    print("You are correct\n")
    score +=1
else:
    print("You are wrong\n")
    score +=0

print("Your score is "+ str(score) +"/3")
print("You scored  "+ str(round((score/3)*100))+"%")