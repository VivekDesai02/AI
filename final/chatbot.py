import random
responses = {
"hello": ["Hi there!", "Hello, how can I help you?", "Hey! What can I do for you?"],
"goodbye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"],
"thank you": ["You're welcome!", "No problem!", "Happy to help!"],
"help": ["Sure, what do you need help with?", "What do you need assistance with?", "How can I assist you?"],
"default": ["I'm sorry, I don't understand. Can you please rephrase that?", "Please provide moreinformation.", "I'm not sure what you mean."]
}
while True:
    user_input = input("User: ")
    if user_input.lower() in responses:
        bot_response = random.choice(responses[user_input.lower()])
    else:
        bot_response = random.choice(responses["default"])
    print("Bot:", bot_response)