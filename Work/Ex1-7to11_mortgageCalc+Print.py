# mortgage.py
#
# Exercise 1.7 thru 1.10
# base variables.  Floats vs Ints implicit type based on initial data value.
principal = 500000.0
rate = 0.05
payment = 2684.11
payment_month = 0
monthly_payment = 0.0
total_paid = 0.0

# extra payment variables, user enterable for appropriate values
print_flag = input('Enter values for extra payments (Y/N)?')
if (print_flag.upper().startswith('Y')):
    extra_payment_start_month = int(input('Extra payment starting month (e.g. 1):'))
    extra_payment_end_month = int(input('Extra payment ending month (e.g. 12):'))
    extra_payment = float(input('Extra payment amount (e.g. 1000.0):'))
else:
    extra_payment_start_month = 0
    extra_payment_end_month = 0
    extra_payment = 0.0
    
print_table = input('Print a table of monthly principal owing and total paid? (Y/N)')
if (print_table.upper().startswith('Y')):
    print('Month Principal Left        Total Paid')  # table headings
    
while principal > 0:
    payment_month += 1
    # test if extra payment needs to be applied
    if (payment_month >= extra_payment_start_month
        and payment_month <= extra_payment_end_month):
        monthly_payment = payment + extra_payment
    else:
        monthly_payment = payment
    # decrement principal until its less than the current payment, then quit
    if monthly_payment > principal:
        monthly_payment = principal
        principal = 0
    else:
        principal = principal * (1+rate/12) - monthly_payment
    total_paid += monthly_payment
    # optional printout table of payments
    # NOTE newer f string usage vs older str.format for total_paid
    if (print_table.upper().startswith('Y')):
        print(f'{payment_month:5}', f'{principal:>14,.2f}',
              '  ${:>14,.2f}'.format(total_paid),
              '  >> this month >', round(monthly_payment,2))
    
print(' ')
print('Total paid:', round(total_paid,2), f'over {payment_month} months')
