import re

print("Blinkit Chatbot")
print("Type exit to stop")

while True:
    user = input("You: ").lower()

    if re.search("hello|hi", user):
        print("Bot: Welcome to Blinkit!")

    elif re.search("items|products", user):
        print("Bot: We deliver groceries, fruits and snacks.")

    elif re.search("delivery", user):
        print("Bot: Delivery takes around 10-20 minutes.")

    elif re.search("payment", user):
        print("Bot: We accept UPI, cards and cash.")

    elif re.search("exit", user):
        print("Bot: Thank you!")
        break

    else:
        print("Bot: Sorry, I don't understand.")
