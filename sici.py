principal = 1500
time = 3
rate = 9

# Calcualtion
simple_interest = (principal*time*rate)/100
compound_interest = principal * ( (1+rate/100)**time - 1)

# Displaying result
print('Simple interest is: %f' % (simple_interest))
print('Compound interest is: %f' %(compound_interest))
