# AtmToBank_application_protocol
This is an appliction protocol for communiction between an atm machine and the bank in case of transactions 

#The supported transactions include;
    => Withdraw
    => Check balance
    => deposit


This system is implemented in python programming language

#In order to  test the application
Run the "bank_main.py" file first followed by "atm_main.py" file

#sample demo data is below
For sample data, we created a simple class Data with a dictionary name demo_data
=> The data is arranged as shown below

    demo_data = {
            "ac1":{
                "pin":"1234",
                "name":"kisakye Joel Nkanji",
                "ac":"0",
                "bal":20000
            },

            "ac2":{
                "pin":"1234",
                "name":"kisakye Joel Nkanji",
                "ac":"1",
                "bal":40000
            },

            "ac3":{
                "pin":"1234",
                "name":"Ben Joel Nkanji",
                "ac":"2",
                "bal":30000
            },
    }

#Security
For Security a class labeled Security was created with _encrypt() and _decrypt() functions in order to encrypt and decrypt sensitive data like pins.
