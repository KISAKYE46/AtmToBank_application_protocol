from socket import * #importing sockets
from sys import platform
import os
import re 
from client_socket import ClientSocket

class ATM(ClientSocket):
    def __init__(self):
      super().__init__()
      self.welcome()

    def send_card(self,card):
      card_status = 0
      self.send_message(card)
      card_status = int(self.receive_message())

      if card_status is not 0 :
        return True
      else:
        return False

    def welcome(self):
        message = self.receive_message()
        print(message)
        
    def read_card(self):
      card = ""
      card = input("Enter card -: ")
      return(self.send_card(card))

    #password verification 
    def verified(self):
      is_valid = 0
      password = ""
      password = input("Please enter your password-:")
      self.send_message(password)
      is_valid = int(self.receive_message())

      if is_valid is not 0:
        return True
      else:
        return False

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

      option = input("Enter option -: ")

      if option is not "":
        option = int(option)
        if option in [1,2,3,4]:
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
      if platform is "linux":
        os.system("clear")
      elif platform is "windows":
        os.system("cls")
      print(info)

    #to view balance
    def view_balance(self):
      bal = ""
      bal =  self.receive_message()
      ATM.log(bal)

    #for cash withdrawal
    def withdraw(self):
      withdraw_message = ""
      withdraw_message =  self.receive_message()
      user_value = input(withdraw_message)
      self.send_message(user_value)
      withdraw_status = self.receive_message()

      withdraw_status = int(withdraw_status)

      if withdraw_status is 1:
        ATM.log("Deposit was succesfull..")
        return True
      else:
        ATM.log(">>-------->Sorry!! Transaction Failed..")
        return False


    #for cash deposit
    def deposit(self):
      withdraw_message = ""
      withdraw_message =  self.receive_message()
      user_value = input(withdraw_message)
      self.send_message(user_value)
      withdraw_status = self.receive_message()

      withdraw_status = int(withdraw_status)

      if withdraw_status is 1:
        ATM.log("$$ Pick Your Cash _/_/_/_/")
        return True
      else:
        ATM.log(">>-------->Sorry!! Transaction Failed..")
        return False

atm = ATM()

if(atm.read_card()):
  if atm.verified():
    atm.menu()
  else:
    ATM.log("Wrong password")
  
else:
  ATM.log("Faulty Card")
