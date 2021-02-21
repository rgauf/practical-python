# Exercise is originally run at command line
print('hello world')

# these commands return values directly in the shell.
# the multi-line command uses "implicit continuation", to finish the parenthesized stmt
## 12 + 20
## (3 + 4
## + 5 + 6)
# The "_" is previous calculated value.  Only works in shell.
## _ - 7
# need explicit PRINT to return value when run as script
print(12 + 20)
print(3 + 4
+ 5 + 6)
# third command needs PRINT to output 'i' value in shell or in script
for i in range(5):
    print(i)
    