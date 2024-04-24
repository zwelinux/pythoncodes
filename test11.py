username = "zwelinhtet"
password = "1234pass"
user = input("Enter username : ")
pwd = input("Enter password : ")
if user == username and pwd == password:
    print("Hello " + user)
elif user == username and pwd != password:
    print("Password Error")
else:
    print("Something Went Wrong. Try Again")