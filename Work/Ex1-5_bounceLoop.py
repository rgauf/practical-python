# bounce.py
#
# Exercise 1.5
height = 100
bounce = 1

while (bounce <= 10):
    height = height * 3/5
    print('Bounce:', f'{bounce:2}', 'height is:', round(height,4))
    bounce += 1
    
print('Done')