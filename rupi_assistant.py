import datetime
import random

# -------------------- MOTIVATIONAL QUOTES ---------------------
quotes = [
    "Believe in yourself — you are capable of amazing things.",
    "Every expert was once a beginner.",
    "Success comes from consistency, not speed.",
    "Small progress every day leads to big results.",
    "Dream big, work hard, stay focused."
]

# -------------------- FUNCTIONS ---------------------

def show_time():
    now = datetime.datetime.now()
    print("\n⏰ Current Date & Time:", now.strftime("%d-%m-%Y %I:%M %p"))

def save_notes():
    note = input("\n📝 Type your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("✔ Note saved successfully!")

def read_notes():
    try:
        with open("notes.txt", "r") as file:
            content = file.read()
            if content.strip():
                print("\n📒 Your Notes:\n")
                print(content)
            else:
                print("\n📘 No notes saved yet.")
    except FileNotFoundError:
        print("\n📘 No notes found (file not created yet).")

def calculator():
    print("\n➕ BASIC CALCULATOR")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Choose operation (+, -, *, /): ")

        if operation == "+":
            print("Result:", num1 + num2)
        elif operation == "-":
            print("Result:", num1 - num2)
        elif operation == "*":
            print("Result:", num1 * num2)
        elif operation == "/":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Cannot divide by zero.")
        else:
            print("Invalid operation selected.")

    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")

def motivation():
    print("\n💡 Motivation Boost:")
    print(random.choice(quotes))

# -------------------- MAIN PROGRAM ---------------------

print("\n🤖 Hello, I am *Rupi-Assistant* — your friendly Python program!")
print("I can help you with basic tasks. Let's begin! 🚀")

while True:
    print("\n--------------- MENU ---------------")
    print("1️⃣  Show Date & Time")
    print("2️⃣  Save a Note")
    print("3️⃣  Read Notes")
    print("4️⃣  Calculator")
    print("5️⃣  Motivation")
    print("6️⃣  Exit")
    print("-----------------------------------")

    choice = input("👉 Choose an option (1-6): ")

    if choice == "1":
        show_time()
    elif choice == "2":
        save_notes()
    elif choice == "3":
        read_notes()
    elif choice == "4":
        calculator()
    elif choice == "5":
        motivation()
    elif choice == "6":
        print("\n👋 Goodbye! Keep learning and growing! 🚀")
        break
    else:
        print("⚠ Invalid choice — please enter a number from 1 to 6.")
