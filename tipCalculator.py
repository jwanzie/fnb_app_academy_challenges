def tipCalculator():
  bill = float(input('Enter your bill amount: Ksh '))
  tip = 0.15

  val_tip = bill * tip
  total_cost = bill + val_tip

  print(f'Your tip amount is: Ksh {round(val_tip, 2)}')

  print(f'Your total amount is: Ksh {round(total_cost, 2)}')
tipCalculator()