
class HumanBeing:
	def __init__(self, n, w, c):
		self.__name = n
		self.weight = w
		self.citizenship = c

	def set_name(self, n):
		self.__name = n

	def get_name(self):
		print (self.__name)
	   
# Main Program
iw = HumanBeing("Ing-wen", 70, "Taiwanese")
iw.get_name()
iw.set_name("Hao-ting")
iw.get_name()


