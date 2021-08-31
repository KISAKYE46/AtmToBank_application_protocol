from socketserver import TCPServer as TCP
from bank_system  import BankSystem

# main function
def main():
	#instantiating the TCP server       
	bankSystem = TCP(("localhost",8100),BankSystem)
	print("BANK SERVER IS UP @'localhost:8800'")

	#commanding the bank system to wait for requests forever
	bankSystem.serve_forever()

# Executing our main
if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print(e)