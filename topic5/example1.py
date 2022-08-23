class Animal: 
  def print_age(self): 
    	print("Age of the animal.") 
     
class Rabbit(Animal): 
  def print_age(self): 
    	print("Age of rabbit.") 
       
class Horse(Animal): 
  def print_age(self): 
    	print("Age of horse.") 

class Ostrich (Animal):
  def fly(self):
	print ("I am flying")

a1 = Rabbit()
a2 = Horse()
a3 = Ostrich()

a1.print_age()
a2.print_age()
a3.print_age()
