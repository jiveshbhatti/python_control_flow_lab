# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input("Input the month (e.g. January, February etc.): ")
day = int(input("Input the day: "))

if month in ('January', 'February', 'March'):
    if day > 19:
        season = 'spring'
    else:
        season = 'winter'

elif month in ('April', 'May', 'June'):
    if day > 20:
        season = 'spring'
    else:
        season = 'summer'
elif month in ('July', 'August', 'September'):
    if day > 21:
        season = 'autumn'
    else:
        season = 'summer'
elif (month == 'December') and (day > 20):
        season = 'winter'



print("Day is ", day)
print("Month is ", month)
print("Season is in ",season)




