class Dog:

	def __init__(self, i, j):
		self.i = i
		self.j = j

	def name(self):
		print("charlii")

	def desc(self):
		print("Age is", self.i)
		print("Live in", self.j)


my_dog = Dog("1 years", "Mangalore")
my_dog.name()
my_dog.desc()
