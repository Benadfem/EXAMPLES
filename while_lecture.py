prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = None
while message != 'quit':
    message = input(prompt)
    print(message)