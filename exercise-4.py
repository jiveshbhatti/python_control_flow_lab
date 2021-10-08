# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

tri_a = input('Enter first side: ')
tri_b = input('Enter second side: ')
tri_c = input('Enter third side: ')

if tri_a == tri_b == tri_c:
	print(f"A triangle with sides of {tri_a}, {tri_b} & {tri_c} is an Equilateral triangle")
elif tri_a==tri_b or tri_b==tri_c or tri_c==tri_a:
	print(f"A triangle with sides of {tri_a}, {tri_b} & {tri_c} is an isosceles triangle")
else:
	print(f"A triangle with sides of {tri_a}, {tri_b} & {tri_c} is an Scalene triangle")

