from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter


# Receive messages from the server
def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
            msg_list.see(tkinter.END)  # Auto-scroll to latest message
        except OSError:
            break


# Send messages to the server
def send(event=None):
    msg = my_msg.get()

    if msg.strip() == "":
        return

    my_msg.set("")
    client_socket.send(bytes(msg, "utf8"))

    if msg == "{quit}":
        client_socket.close()
        top.quit()


# Called when user closes the window
def on_closing(event=None):
    my_msg.set("{quit}")
    send()


# ==============================
# GUI DESIGN
# ==============================

top = tkinter.Tk()
top.title("💬 Python Network Chat App")
top.geometry("650x550")
top.configure(bg="#2C3E50")
top.resizable(False, False)


# Chat frame
messages_frame = tkinter.Frame(
    top,
    bg="#2C3E50"
)
messages_frame.pack(pady=15)


# Scrollbar
scrollbar = tkinter.Scrollbar(messages_frame)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)


# Message display
msg_list = tkinter.Listbox(
    messages_frame,
    height=20,
    width=65,
    yscrollcommand=scrollbar.set,
    bg="white",
    fg="black",
    font=("Arial", 11)
)

msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)

scrollbar.config(command=msg_list.yview)


# Input frame
input_frame = tkinter.Frame(
    top,
    bg="#2C3E50"
)

input_frame.pack(pady=10)


# Message variable
my_msg = tkinter.StringVar()
my_msg.set("Type your message here...")


# Text entry
entry_field = tkinter.Entry(
    input_frame,
    textvariable=my_msg,
    width=45,
    font=("Arial", 12)
)

entry_field.bind("<Return>", send)
entry_field.pack(side=tkinter.LEFT, padx=10)


# Send button
send_button = tkinter.Button(
    input_frame,
    text="Send",
    width=10,
    font=("Arial", 12, "bold"),
    bg="#3498DB",
    fg="white",
    command=send
)

send_button.pack(side=tkinter.LEFT)


# Handle closing
top.protocol("WM_DELETE_WINDOW", on_closing)


# ==============================
# NETWORK CONNECTION
# ==============================

HOST = input("Enter server IP: ")
PORT = input("Enter server port: ")

if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDRESS = (HOST, PORT)


# Create socket and connect
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDRESS)


# Start receiving messages
receive_thread = Thread(target=receive)
receive_thread.start()


# Start GUI
tkinter.mainloop()