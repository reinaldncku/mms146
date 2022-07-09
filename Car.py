class Car:
	def __init__(self, c, n, s, f):
		self.color = c
		self.name = n
		self.speed = s
		self.fuel = f

	def increase_speed(self):
		self.speed = self.speed + 1

	def change_name(self, n):
		self.name = n

car1 = Car("blue", "May ToyoSiya", 0, 1000)
car2 = Car("red", "Subarururu", 100, 5)

print ("Name before: ", car1.name)
car1.change_name("Walang ToyoSiya")
print ("Name after: ", car1.name)
