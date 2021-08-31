from server import Server
from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime
from security import Security
from data import Data

#Bank system handler to handle all requests
class BankSystem(Server):
    #display welcome
    def display_welcome(self):
        self.send_message("------------------\nHello!!!\nWelcome our esteemed customer")

    #To get card
    def get_card(self):
        card = ""
        card = self.receive_message()
        if card in Data.demo_data:
            self.current_card = card
            PIN = Data.demo_data[self.current_card]["PIN"]

            #sending encrypted PIN to our atm for verification
            self.send_message( Security._encrypt(PIN)) 
            option = self.receive_message()
            option = int(option)

            if option is 1 :
                self.send_balance()
            elif option is 2 :
                self.withdraw()
            elif option is 3 :
                self.deposit()
            elif option is 4 :
                pass
        else:
            self.send_message(0)

    #To send balance data
    def send_balance(self):
        print("Checking balance.......")
        self.send_message("Current Balance on {} is: $ {} ".format(ctime(),Data.demo_data[self.current_card]["bal"]))

    #To handle withdraw transactions
    def withdraw(self):
        self.send_message("Enter amount not greater than $ {} -: ".format(Data.demo_data[self.current_card]["bal"]))
        amount = self.receive_message()
        amount = int(amount)

        #Checkin if withdraw amount is greater than available amount
        if amount < Data.demo_data[self.current_card]["bal"]:
            Data.demo_data[self.current_card]["bal"] = Data.demo_data[self.current_card]["bal"]-amount
            self.send_message(1)
        else:
            self.send_message(0)

    #To handle deposit transactions
    def deposit(self):
        self.send_message("Enter deposit amount -: ")
        amount = self.receive_message()
        amount = int(amount)

        #Checking if submited amount is greater than zero
        if amount >0:
            Data.demo_data[self.current_card]["bal"] = Data.demo_data[self.current_card]["bal"]+amount
            self.send_message(1)
        else:
            self.send_message(0)