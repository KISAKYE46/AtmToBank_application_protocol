from socket import * 
import os

class ClientSocket:

  def __init__(self):
    self.client_socket=socket(AF_INET,SOCK_STREAM)
    self.conn()

  #for connection
  def conn(self):
    self.client_socket.connect(("localhost",8800))
      
  #for receiving messages
  def receive_message(self):
    return self.client_socket.recv(1024).decode("utf-8")
      
  #for sending messages
  def send_message(self,data):
    self.client_socket.send(bytes("{}\n".format(data).encode("utf-8")))
