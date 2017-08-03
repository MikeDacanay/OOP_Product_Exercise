# Assignment: Product
# The owner of a store wants a program to track products. Create a product class to fill the following requirements.

class Product(object):
	def __init__(self,price,item,weight,brand,cost):
		self.price=price
		self.item_name=item
		self.weight=weight
		self.brand=brand
		self.cost=cost
		self.status="for sale"
	def sold(self):
		self.status="sold"
# method below is for testing purposes
	def display_all(self):	
		print self.price
		print self.item_name
		print self.weight
		print self.brand
		print self.cost
		print self.status
		# return self.price
#ASK QUESTIONS ABOUT THE BELOW
		# return self.item_name
		# return self.weight
		# return self.brand
		# return self.cost
		# return self.status
	def add_tax(self,tax):
		self.price+=tax
		return self.price
	def return_product(self,reason):
		if reason=="defective":
			self.price=0
			return self.price
		elif reason=="returned with box":
			self.status="for sale"
			return self.status
		elif reason=="returned opened":
			self.price=self.price*.80
			return self.price


# test product
prod1=Product(100,"Shish",5,"eh",60)
