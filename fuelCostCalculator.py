def fuelCostCalculator():
  distance = float(input('Enter your travel distance in kilometers: '))
  petrol_price = float(input('What is the current petrol price per litre? Ksh '))

  litres_needed = distance / 10
  total_cost = round(litres_needed * petrol_price, 2)

  print(f'The total fuel cost required for your travel is: Ksh {total_cost}')
fuelCostCalculator()