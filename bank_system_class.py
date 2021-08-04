from socket import *
from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)

#demo data
demo_data = {
    "ac1":{
        "pass":"1234ty",
        "name":"kisakye Joel Nkanji",
        "ac":"x1gsf",
        "bal":"20000"
    },

    "ac2":{
        "pass":"1234",
        "name":"kisakye Joel Nkanji",
        "ac":"x1hsf",
        "bal":"40000"
    },

    "ac3":{
        "pass":"1234",
        "name":"Ben Joel Nkanji",
        "ac":"x1fsk",
        "bal":"30000"
    },
}

#Bank system handler to handle all requests
class BankSystemHandler(SRH):
    def handle(self):

        print("connected from ",self.client_address)
        account = ""

        #receiving account
        account = self.rfile.readline()

        if(account is not None):
            account = account.decode("utf-8").replace("\n","")
            #if account exists
            if(account in demo_data):

                #sending response that account exists
                self.wfile.write(bytes("Account Exists".encode("utf-8")))

                password = ""
                #receiving user password
                password = self.rfile.readline().decode("utf-8").replace("\n","")
                
                #checking if account is true and sending response to atm
                if(demo_data[account]["pass"] == password):
                    self.wfile.write(bytes("Right Password".encode("utf-8")))
                else:
                    self.wfile.write(bytes("Wrong Password".encode("utf-8")))

       
      
        
        
#instantiating the TCP server       
bankSystem = TCP(("localhost",8700),BankSystemHandler)


print("......Waiting for connections.........")




#commanding the bank system to wait for requests forever
bankSystem.serve_forever()
