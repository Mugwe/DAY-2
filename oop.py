class Vehicle(object):
	def __init__(self, vehicle_type = none , year_of_manufacture = 2008):
		if self.vehicle_type != 'tractor':
			self.vehicle_type = 'subaru'

class Car(Vehicle):
	vel = 0  

	def motion(self):
		print ("shift to gear 1 and take off!")

	def set_num(self, num):
		self.vel = num

	def get_num(self):
		return self.vel


class Truck(Vehicle):
	vel = 0

	def motion(self):
		print ("shift to gear 3 and take off!")

	def set_num(self, num):
		self.vel = num

	def get_num(self):
		return self.vel

def vehicle_motion(any_vehicle):
	return any_vehicle.motion()