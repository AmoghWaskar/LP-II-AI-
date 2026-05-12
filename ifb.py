import re

print("IFB Washing Machine Chatbot")
print("Type exit to stop")

while True:
    user = input("You: ").lower()

    if re.search("hello|hi", user):
        print("Bot: Hello! Welcome to IFB Support.")

    elif re.search("price|cost", user):
        print("Bot: Prices start from Rs. 15,000.")

    elif re.search("features", user):
        print("Bot: Smart Wash, Child Lock and Quick Wash available.")

    elif re.search("service|repair", user):
        print("Bot: Free installation and service support available.")

    elif re.search("warranty", user):
        print("Bot: 4 years product warranty and 10 years motor warranty.")

    elif re.search("exit", user):
        print("Bot: Thank you!")
        break

    else:
        print("Bot: Sorry, please ask another question.")
