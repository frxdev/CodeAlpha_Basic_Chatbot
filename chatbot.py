import tkinter as tk

def get_reply(srt):
    sr = srt.lower()
    if sr == "hello":
        return "Hi!"
    elif sr == "how are you":
        return "I am fine, thanks!"
    elif sr == "bye":
        return "Goodbye!"
    else:
        return "Sorry! I do not understand that"

def send():
    user_msg = entry.get()
    if user_msg.strip() == "":
        return

    chat_box.insert(tk.END, "You: " + user_msg + "\n")
    reply = get_reply(user_msg)
    chat_box.insert(tk.END, "Ai: " + reply + "\n")
    entry.delete(0, tk.END)

    if reply == "Goodbye!":
        chat_box.insert(tk.END, "--- Chat Ended ---\n")
        entry.config(state="disabled")
        send_btn.config(state="disabled")

root = tk.Tk()
root.title("Chatbot")

chat_box = tk.Text(root, height=20, width=50)
chat_box.pack(padx=10, pady=10)

entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=10, pady=10)
entry.bind("<Return>", lambda event: send())  # Enter key se bhi bhej sakte ho

send_btn = tk.Button(root, text="Send", command=send)
send_btn.pack(side=tk.LEFT)

root.mainloop()