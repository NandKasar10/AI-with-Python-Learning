import sys
from fractions import Fraction
#this fraction modules will give us power to do calculations
from decimal import Decimal

ideal_temp = 95.5
current_temp = 95.49999

print(f"ideal temp : {ideal_temp}")
print(f"current temp : {current_temp}")
print(f"difference temp : {ideal_temp-current_temp}") #not expected answer

#thats why for high precision calculation we need to import some libraries

print(sys.float_info)