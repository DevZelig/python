b = ''
while b != 'stop':
    b = input("how are you feeling today?")
    if b == "good":
        print("thats great")
    elif b == "bad":
        print('sorry to hear that')
    elif b == "stop":
        print("ok")
    else:
        print('i dont know what youre saying')
