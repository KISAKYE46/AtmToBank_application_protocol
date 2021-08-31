from socket import *
from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
class Server(SRH):
  def handle(self):
    print("connected from ",self.client_address)
    #Tostore current card
    self.current_card = ""
    self.display_welcome()
    self.get_card()
   
  #send messages 
  def send_message(self,message):
    self.wfile.write("{}".format(message).encode("utf-8"))

  #receive messages
  def receive_message(self):
    message = ""
    message = self.rfile.readline()
    if message is not "":
        message = message.decode("utf-8").replace("\n","") 
    return message
