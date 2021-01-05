import math
num_of_years = 10
annual_interest = 7
principal_amount = 1000
amounts = []
for idx in range(num_of_years+1):
    yearly_amount = principal_amount * (1 + annual_interest / 100) ** idx
    amounts.append(yearly_amount)
print(amounts)
                                        