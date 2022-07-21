# An illustration of inheritance
# Prepared by RADP

class HumanBeing:
	def __init__(self, n, w, c):
		self.name = n
		self.weight = w
		self.citizenship = c
		
	def print_weight(self):
	    print (self.weight, " kg")


class Student(HumanBeing):
	def __init__(self, g, s, n, w, c):
	    super().__init__(n, w, c)
	    self.gwa = g
	    self.school = s
		
	def print_gwa(self):
		print ("GWA: ", self.gwa)


jiawen = Student(1.5, "NCKU", "Jiawen", 60, "Chinese")
jiawen.print_weight()
jiawen.print_gwa()

timothy = HumanBeing("Timothy", 70, "Taiwanese")
timothy.print_weight()
#timothy.print_gwa() # This line of code will result in an error
