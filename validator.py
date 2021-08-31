import re

class Validate:

	@staticmethod
	def is_valid_num(data):
		
		#checking for non digit character
		pattern = re.compile(r'\D+')
		result = pattern.findall(data) 

		if len(result)>0:
			return False
		else:
			return True
	
