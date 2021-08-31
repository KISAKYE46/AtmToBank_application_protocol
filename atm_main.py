from atm import ATM
from security import Security

# Main function
def main():
  while True:
    atm = ATM()
    
    # Receiving and decrypting the sent encrypted PIN
    PIN =  Security._decrypt(atm.read_card())

    if len(PIN)>0:
      if(PIN is not None or PIN is not "" or PIN != '0' ):
        if atm.verified(PIN):
          atm.menu()
      else:
        ATM.log("Faulty Card")

      ATM.clear()
    else:
      print("Card invalid")


# Executing our main
if __name__ == '__main__':
  try:
    main()
  except Exception as e:
    print(e)
  finally:
    print("Execution stopped")