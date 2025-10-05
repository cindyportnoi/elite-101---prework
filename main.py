print("Welcome to the Elite 101 Chatbot!")
name = input("What is your name? ")
age = int(input("Hello " + name + ", how old are you? "))
if age < 15:
    print("You are so young! How may I help you today?")
elif 15<=age<18:
    print(f"Oh, how to be {age} again! How may I help you today?")
elif 18<=age<55:
    print(f"I hope {age} is treating you well! How may I help you today?")
elif 55<=age<120:
    print("The older, the wiser! How may I help you today?")
else:
    print("You're the oldest person I've ever met! How may I help you?")
print()
print("Please choose one of these following options: ")
print("1. Placeholder")
print("2. Placeholder")
print("3. Placeholder")
print("4. Exit the conversation")
choice = input("Option number: ")
if choice == "1":
    print()
elif choice == "2":
    print()
elif choice == "3":
    print()
elif choice == "4":
    print("Have a good day, " + name + "!")
else:
    print("Sorry, that's not one of the choices.")
