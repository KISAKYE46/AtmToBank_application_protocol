import re
from keys import Key
import stdiomask as mask
class Security:
	"""
	This class will govern all the security for our system
	"""
	@staticmethod
	def _encrypt(string):#to encrypt our data
		string = string
		enc_string = ""
		arr = []
		for character in string:
			arr.append(Key.enc_keys[character])
		for element in arr:
			enc_string = enc_string+"{}".format(element)
		return(enc_string)

	@staticmethod
	def  _decrypt(string):#to decrypt our data
		dec_string =""
		ten_char =""
		char_count = 1
		for character in string:
			if char_count <10:
				ten_char = ten_char+"{}".format(character)
				char_count = char_count+1
			elif char_count ==10:
				ten_char = ten_char+"{}".format(character)
				dec_string = dec_string+"{}".format(Key.dec_keys[ten_char])
				ten_char=""
				char_count= 1
		return dec_string

  #to allow pin input
	@staticmethod
	def _input_PIN(prompt):
		PIN = mask.getpass(prompt=prompt)
		return PIN

