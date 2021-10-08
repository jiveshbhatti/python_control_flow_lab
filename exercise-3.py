# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

dog_age = int(input('please enter dog age: '))

for i in range(1, dog_age+1):
    age = 0
    totalAge = 1
    print(i)
    while age < 3:
        totalAge = totalAge * 10
        age += 1
        continue
    print(i)
    print(totalAge, 'this is totalAge')
    
h_age = int(input("Input a dog's age in human years: "))

if h_age < 0:
	print("Age must be positive number.")
	
elif h_age <= 2:
	d_age = h_age * 10
else:
	d_age = 20 + (h_age - 2)* 7

print("The dog's age in dog's years is", d_age)