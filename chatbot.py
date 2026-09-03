def get_reply(srt):

    sr = srt.lower()
    if (sr == "hello"):
        return "Hi!"
    elif (sr == "how are you"):
        return "I am fine, thanks!"
    elif (sr == "bye"):
        return "Goodbye!"
    else:
        return "Sorry! I do not understand that"


while (True):
    st = input("Write a message...")
    reply = get_reply(st)
    print("Ai: ", reply)
    if (reply == "Goodbye!"):
        break
