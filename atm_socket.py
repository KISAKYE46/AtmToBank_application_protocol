from socket import * #importing sockets
import re 
atm_socket = socket(AF_INET,SOCK_STREAM) #instattiating our socket


"""
def data_stringify(dict_data):
    str_data = ""
    for key in dict_data:
        str_data = str_data+key+"="+dict_data[key]+","
    return str_data

def regex_match(pattern,string):
    pattern = re.compile(pattern)
    matcher = pattern.findall(string)
    if matcher:
        return matcher 
    else:
        return None
"""


#data = data_stringify(dict_data)
data_pattern = "[a-z]{1,}[=]{1,1}[a-z0-9]{1,}" 

#to store bank system response data
response_data = None
atm_data = "ac3\n"

if atm_socket:

      #connecting to the bank system
      atm_socket.connect(("localhost",8700)) 

      #encoding the data to be sent
      atm_socket.send(atm_data.encode("utf-8")) 

      #Receiving the data from the central bank system
      response_data = atm_socket.recv(1024)
      if response_data is not None:
          response_data = response_data.decode("utf-8")
          print(response_data)
          if response_data =="Account Exists":
             password = ""
             password = input("Enter password:")
             atm_socket.send(bytes("{}\n".format(password).encode("utf-8")))
             
             #receiving password status response from the central bank system
             response_data = atm_socket.recv(1024)

             response_data = response_data.decode("utf-8")

             #Displaying to the user the password status
             if(response_data == "Right Password"):
                 print("Right Password")
             else:
                 print("Wrong Password")


              
      else:
          print("No data")




    
    

