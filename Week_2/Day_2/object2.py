class Vehicle:
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
	def print_info(self):
		print(self.make,self.model,self.year)
		
car = Vehicle('Honda','Civic Type R','2017')
car.print_info()