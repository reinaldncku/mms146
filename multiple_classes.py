# This is the Car class
class Car:
	def __init__(self, c, n, s, f):
		self.color = c
		self.name = n
		self.speed = s
		self.fuel = f

	def increase_speed(self):
		self.speed = self.speed + 1

# This is the Robot class
class Robot:
	def __init__(self, c, n):
		self.color = c
		self.name = n


# Main program
car1 = Car("blue", "May ToyoSiya", 0, 1000)
car2 = Car("red", "Subarururu", 100, 5)
elon_robot = Robot("gray", "Elon Mask")

print ("Before increase speed: ", car1.speed)
car1.increase_speed()
print ("After increase speed: ", car1.speed)
print ("Name of new robot: ", elon_robot.name)



