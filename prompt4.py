'''
Write a Python program that declares a class describing your favorite animal. 
Have the data members of the class represent the following physical parameters of the animal: 
length of the arms (float), length of the legs (float), number of eyes (int), does it have a tail? (bool), is it furry? bool). 
Write an initialization function that sets the values of the data members when an instance of the class is created. 
Write a member function of the class to print out and describe the data members representing the physical characteristics of the animal.
'''

#My favorite animal is a dog and I will be creating a class that has the attributes of one!

class Dog:

	def __init__(bark, arm_length: float, leg_length: float, eye_num: int, has_tail: bool, is_furry: bool):
		bark.arm_length = arm_length
		bark.leg_length = leg_length
		bark.eye_num = eye_num
		bark.has_tail = has_tail
		bark.is_furry = is_furry

	def member_func(bark):
		print(f"These are the attributes of a Dog!\n")
		print(f"Length of arms: {bark.arm_length} inches\n")
		print(f"Length of legs: {bark.leg_length} inches\n")
		print(f"Number of eyes: {bark.eye_num}\n")
		print(f"Does it have a tail?: {bark.has_tail}\n")
		print(f"Is it furry?: {bark.is_furry}\n")

golden = Dog(21.0, 21.5, 2, True, True)

golden.member_func()