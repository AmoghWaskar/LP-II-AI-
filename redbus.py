import re

print("RedBus Chatbot")
print("Type exit to stop")

while True:
    user = input("You: ").lower()

    if re.search("hello|hi", user):
        print("Bot: Welcome to RedBus!")

    elif re.search("booking|ticket", user):
        print("Bot: You can book bus tickets online.")

    elif re.search("cancel", user):
        print("Bot: Tickets can be cancelled before departure.")

    elif re.search("payment", user):
        print("Bot: We accept UPI, cards and net banking.")

    elif re.search("offers|discount", user):
        print("Bot: Cashback and discount offers are available.")

    elif re.search("exit", user):
        print("Bot: Thank you!")
        break

    else:
        print("Bot: Sorry, I could not understand.")
