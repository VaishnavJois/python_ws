'''
program to determine simple interest

given:
    principle = 6000
    rate_of_interest = 0.1
    time = 1.5 years
'''

principle = int(input('Enter the principle amount (in rupees): '))
rate_of_interest = float(input('Enter the Percentage rate of interest(per annum): '))/100.0
time = float(input('Enter the duration: '))


simple_interest = (principle*time*rate_of_interest)/100.0

print(simple_interest)