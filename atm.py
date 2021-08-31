from socket import * #importing sockets
from sys import platform
import os
import re 
from client_socket import ClientSocket
from security  import Security
from validator import Validate

class ATM(ClientSocket):
    def __init__(self):
      super().__init__()
      self.welcome()

    #send card 
    def send_card(self,card):
      card_status = 0
      self.send_message(card)
      pin = self.receive_message()
      # card_status = int(self.receive_message())

      if pin is not None or pin is not "" :
        return pin
      else:
        return None

    #show welcome message
    def welcome(self):
        message = self.receive_message()
        print(message)
    
    #read card and returns PIN 
    def read_card(self):
      card = ""
      card = input("=> Enter card -: ")
      return(self.send_card(card))

    #pin verification 
    def verified(self,sent_pin):
      is_valid = 0

      valid_count = 0
      pin = ""
      pin = Security._input_PIN("=> Please enter your pin-: ")
      while pin != sent_pin:
        pin = Security._input_PIN("=> Re-enter correct pin please-: ")
        valid_count = valid_count+1

        #checking input attempt times
        if valid_count is 4:
          return False
      return True

    #for displaying the menu
    def menu(self):
      option = 0
      ATM.log(
        """    
                    *
                   BANK
                **********
                [-MENU-]
        (1) Check Account Balance
        (2) Withdraw Cash
        (3) Deposit Cash
        (4) Quit
        """
        )
      options = [1,2,3,4]
      option = input("=> Enter option -: ")

      #validating the options

      while not Validate.is_valid_num(option):
        option = input("=> Please enter a numeric option -: ")
      
      option = int(option)

      while option not in options :
        option = input("=> Please enter right option -: ")

        if not Validate.is_valid_num(option):
          option = input("=> Please enter a numeric option -: ")
        else:
          option = int(option)


      self.send_message(option)
      if option is 1:
        self.view_balance()
      elif option is 2:
        self.withdraw()
      elif option is 3:
        self.deposit()
      elif option is 4:
        pass
            
    @staticmethod
    def log(info):
      ATM.clear()
      print(info)

    @staticmethod
    def clear():
      if platform is "linux":
        os.system("clear")
      elif platform is "win32" or platform is "win64":
        os.system("cls")

    #to view balance
    def view_balance(self):
      bal = ""
      bal =  self.receive_message()
      ATM.log("\n--Viewing balance--")
      ATM.log(bal)

    #for cash withdrawal
    def withdraw(self):
      withdraw_message = ""
      withdraw_message =  self.receive_message()
      user_value = input(withdraw_message)
      self.send_message(user_value)
      withdraw_status = self.receive_message()

      withdraw_status = int(withdraw_status)

      #withdraw status ok
      if withdraw_status is 1:
        ATM.log("$$ Pick Your Cash ( )")
        
        return True
      else:
        ATM.log(">>Sorry!! Transaction Failed..")
        return False

    #for cash deposit
    def deposit(self):
      deposit_message = ""
      deposit_message =  self.receive_message()
      user_value = input(deposit_message)
      self.send_message(user_value)
      deposit_status = self.receive_message()

      deposit_status = int(deposit_status)

      if deposit_status is 1:
        ATM.log("Deposit was succesfull..")
        return True
      else:
        ATM.log("Sorry!! Transaction Failed..")
        return False