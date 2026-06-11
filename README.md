# 💬 Python Client-Server GUI Chat Application 

## Project Overview

This project is a real-time chat application developed using Python. It uses a client-server architecture where multiple users can communicate over a network using TCP sockets and a graphical user interface built with Tkinter.

## Features

- Real-time messaging
- Multiple client support
- TCP socket communication
- Client-server architecture
- Graphical User Interface (GUI)
- User connection and disconnection notifications
- Communication between devices on the same network

## Technologies Used

- Python 3
- Socket Programming
- TCP/IP Protocol
- Threading
- Tkinter GUI

## Project Structure

```
Chat_App_Project/
│
├── server.py        # Server application
├── client.py        # Client GUI application
├── README.md        # Project documentation
└── Screenshots/     # Application screenshots
```

## How to Run the Application

### Start the Server

Run:

```bash
python server.py
```

The server will start and wait for client connections.

### Start the Client

Open another terminal and run:

```bash
python client.py
```

Enter the server IP address and port number when requested.

## Network Testing

- Run the server on one computer.
- Connect other computers using the server's IP address.
- All connected users can exchange messages in real time.

## Challenges Encountered

- Managing multiple users using threads.
- Handling network connection errors.
- Synchronizing the GUI with incoming messages.
- Ensuring proper message transmission using UTF-8 encoding.

## Future Improvements

- User authentication
- Private messaging
- File sharing
- Chat history storage
- Message encryption

## Conclusion

This project demonstrates the use of Python socket programming, networking, multithreading, and GUI development to create a functional real-time chat system.
