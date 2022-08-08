class HumanBeing:
	def __init__(self, n, w, c):
		self.__name = n
		self.weight = w
		self.citizenship = c

	def set_name(self, n):
		self.__name = n

	def get_name(self):
		print (self.__name)
		self.__get_more_name()
		
	def __get_more_name(self):
	    print (self.__name)
	    print (self.__name)
	   
# Main Program
iw = HumanBeing("Ing-wen", 70, "Taiwanese")
iw.get_name()
#iw.__get_more_name()  # This is illegal, take note

