import random
result = random.randint(1, 2)
choice = int(input("Enter choice (Head for 1 / Tail for 2) : "))
if choice == 1 and result == 1:
    print("It's Head and you won")
elif choice == 1 and result == 2:
    print("It's Tail and you lost")
elif choice == 2 and result == 1:
    print("It's Head and you lost")
elif choice == 2 and result == 2:
    print("It's Tail and you won")