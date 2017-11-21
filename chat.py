#!usr/bin/env python

import socket
import threading
import select
import time

def main():

    class Chat_Server(threading.Thread):
        connections = []
        def __init__(self):
            threading.Thread.__init__(self)
            self.running = 1
            self.user = None
            self.conn = None
            self.addr = None
        def run(self):
            HOST = ''
            PORT = 8000
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((HOST,PORT))
            s.listen(1)
            self.conn, self.addr = s.accept()
            self.connections.append(conn)
            # Select loop for listen
            while self.running == True:
                inputready,outputready,exceptready \
                = select.select ([self.conn],[self.conn],[])
                for input_item in inputready:
                    # Handle sockets
                    message  = self.conn.recv(1024)
                    for connections in self.connection
                        if message :
                            print message 
                        else:
                            break
                time.sleep(0)
        def kill(self):
            self.running = 0
     
    class Chat_Client(threading.Thread):
            def __init__(self):
                threading.Thread.__init__(self)
                self.user = None
                self.host = None
                self.sock = None
                self.running = 1
            def run(self):
                PORT = 8000
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((self.host, PORT))
                # Select loop for listen
                while self.running == True:
                    inputready,outputready,exceptready \
                      = select.select ([self.sock],[self.sock],[])
                    for input_item in inputready:
                        # Handle sockets
                        message  = self.sock.recv(1024)
                        if message :
                            print message
                        else:
                            break
                    time.sleep(0)
            def kill(self):
                self.running = 0
                
    class Text_Input(threading.Thread):
            def __init__(self):
                threading.Thread.__init__(self)
                self.running = 1
            def run(self):
                while self.running == True:
                    text = raw_input('')
                    if text == "exit()":
                        self.kill()
                        chat_client.kill()
                        chat_server.kill()
                    else:
                        try:
                            msg = chat_client.user + ':' + text
                            chat_client.sock.sendall(msg)
                        except:
                            Exception
                        try:
                            msg = chat_server.user + ':' + text
                            chat_server.conn.sendall(msg)
                        except:
                            Exception
                        time.sleep(0)
            def kill(self):
                self.running = 0

    # Prompt, object instantiation, and threads start here.

    ip_addr = raw_input('What IP (or type host)?: ')
    id_user = raw_input("User Name?: ")
    # It gets initialized in both anyways, so why put it in an if statement?
    chat_server = Chat_Server()
    chat_client = Chat_Client()

    if ip_addr.lower() == 'host': # case insensitive check
        chat_server.user = id_user
        chat_server.start()
    else:
        chat_client.user = id_user
        chat_client.host = ip_addr
        chat_client.start()

    text_input = Text_Input()
    text_input.start()

if __name__ == "__main__":
    main()



            
