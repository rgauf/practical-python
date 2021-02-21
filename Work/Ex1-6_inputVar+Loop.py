# Exercise 1-6 embellished a bit. Sample program features;
#   input a string, dynamic data type, if/elif/else, pass (no-op),
#   escape special chars, convert string to numeric,
#   str.format() use, string literal use, suppress PRINT newline (end= param)
bill_thickness = 0.11 * 0.001 # Meters (0.11 mm)
num_bills = 1
day = 1
input_value = input('Enter max height (defaults to 442 meters):')

# Python isnumeric tests only allow number characters, not arithmetic characters
# have to use a RegEx test (i.e. [0-9,.-] ) to test float numbers
if (input_value == ''):
    input_value = '442'
elif (input_value.isdigit()):
    pass
else:
    print('That wasn\'t a valid integer, reset as 0')
    input_value = '0'   

max_height = int(input_value)   # = float(input_value)
while num_bills * bill_thickness < max_height:
    print(f'Day: {day:3}', ' Bills:', num_bills, ' Thickness:', num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print(f'Final height is {num_bills * bill_thickness}')
print('Number of days', day, end=' > ')
print('Number of bills', num_bills)
