import datetime
import random

print("====================================")
print("         AI CHATBOT")
print("====================================")

# Get user name
name = input("\nEnter your name: ")

print(f"\nHello {name}! I am your chatbot.")
print("Type 'bye' to exit.\n")

# Random responses
greetings = [
    "Hello!",
    "Hi there!",
    "Hey!"
]

how_are_you = [
    "I am fine!",
    "Doing great!",
    "Awesome as always!"
]

while True:

    user = input(f"{name}: ").lower().strip()

    # Greeting
    if user in ["hi", "hello", "hey"]:
        print("Bot:", random.choice(greetings))

    # How are you
    elif user in ["how are you", "how are you?"]:
        print("Bot:", random.choice(how_are_you))

    # Time
    elif "time" in user:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print("Bot: Current time is", current_time)

    # Date
    elif "date" in user:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    # AI
    elif "ai" in user:
        print("Bot: AI stands for Artificial Intelligence.")

    # Motivation
    elif "motivate" in user:
        print("Bot: Believe in yourself. You can do anything!")

    # Calculator
    elif any(op in user for op in ["+", "-", "*", "/"]):

        try:
            if "+" in user:
                num1, num2 = user.split("+")
                result = float(num1) + float(num2)

            elif "-" in user:
                num1, num2 = user.split("-")
                result = float(num1) - float(num2)

            elif "*" in user:
                num1, num2 = user.split("*")
                result = float(num1) * float(num2)

            elif "/" in user:
                num1, num2 = user.split("/")
                result = float(num1) / float(num2)

            print("Bot: Answer =", result)

        except:
            print("Bot: Please enter a valid calculation.")

    # Thanks
    elif user in ["thanks", "thank you"]:
        print("Bot: You're welcome!")

    # Exit
    elif user == "bye":
        print(f"Bot: Goodbye {name}! Have a nice day.")
        break

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand.")