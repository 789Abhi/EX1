class Dog:

	def __init__(self, i, j, k):
		self.i = i
		self.j = j
		self.k = k

	def name(self):
		print("charlii")

	def desc(self):
		print("Age is", self.i)
		print("Live in", self.j)
		print("Looks after by Alape family", self.k)


my_dog = Dog("1 years", "Mangalore", "Abhishek")
my_dog.name()
my_dog.desc()
