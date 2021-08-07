from socket import *
from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

#Bank system handler to handle all requests
class BankSystem(SRH):

    #demo data
    demo_data = {
        "ac1":{
            "pass":"1234ty",
            "name":"kisakye Joel Nkanji",
            "ac":"x1gsf",
            "bal":20000
        },

        "ac2":{
            "pass":"1234",
            "name":"kisakye Joel Nkanji",
            "ac":"x1hsf",
            "bal":40000
        },

        "ac3":{
            "pass":"1234",
            "name":"Ben Joel Nkanji",
            "ac":"x1fsk",
            "bal":30000
        },
    }


    def handle(self):
        print("connected from ",self.client_address)
        #Tostore current card
        self.current_card = ""
        self.display_welcome()
        self.get_card()
            
    #display welcome
    def display_welcome(self):
        self.send_message("Welcome our esteemed customer")

    def send_message(self,message):
        self.wfile.write("{}".format(message).encode("utf-8"))

    #receive messages
    def receive_message(self):
        message = ""
        message = self.rfile.readline()

        if message is not "":
            message = message.decode("utf-8").replace("\n","")

        return message

    def get_card(self):
        card = ""
        card = self.receive_message()
        if card in BankSystem.demo_data:
            self.current_card = card
            self.send_message(1)
            password = BankSystem.demo_data[self.current_card]["pass"]

            received_pass = self.receive_message()

            if received_pass == password:
                self.send_message(1)
                option = self.receive_message()

                option = int(option)

                if option is 1 :
                    self.send_balance()
                elif option is 2 :
                    self.withdraw()
                elif option is 3 :
                    pass
                elif option is 4 :
                    pass

            else:
                self.send_message(0)

        else:
            self.send_message(0)

    
    def send_balance(self):
        self.send_message("Current Balance on {} is: $ {} ".format(ctime(),BankSystem.demo_data[self.current_card]["bal"]))

    def withdraw(self):
        self.send_message("Enter amount not greater than $ {} -: ".format(BankSystem.demo_data[self.current_card]["bal"]))
        amount = self.receive_message()
        amount = int(amount)

        if amount < BankSystem.demo_data[self.current_card]["bal"]:
            BankSystem.demo_data[self.current_card]["bal"] = BankSystem.demo_data[self.current_card]["bal"]-amount
            self.send_message(1)
        else:
            self.send_message(0)
            
        
                
#instantiating the TCP server       
bankSystem = TCP(("localhost",8800),BankSystem)

print(
    """

    >>>>>>> BANK SERVER IS UP @'localhost:8800'>>>>>>

    """


    )

#commanding the bank system to wait for requests forever
bankSystem.serve_forever()

