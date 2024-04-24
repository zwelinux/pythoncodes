answer = 8
guess = int(input("Enter your guess (1 - 10) : "))

if guess > answer:
    print("Wrong Guess. Try Smaller One ")
elif guess < answer:
    print("Wrong Guess. Try Bigger One ")
elif guess == answer:
    print("Bingo!")

# ရာသီဥတု program 

answer = input("Enter Weather (sunny, rainy, windy)")
if answer == "sunny":
    print("it's sunny let's go for a walk") 
elif answer == "rainy":
    print("it's rainy take umbrella when you go outside") 
elif answer == "windy":
    print("Nya Ka Man U Ma Shone Loz") 
else:
    print("Enter (sunny, rainy, windy) Only Please")