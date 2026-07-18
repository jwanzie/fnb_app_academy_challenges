'''The Challenge: “The Smart ATM Withdrawal Simulator”

Simulate a bank transaction checking if a user has enough money.

1. Set a fixed variable representing a bank balance, for example: balance = 500.

2. Ask the user how much money they want to withdraw. (Remember to cast it to an integer or float!).

3. If the request is less than or equal to the balance, deduct the amount and print:
“Withdrawal successful! Remaining balance: RX”.

4. But what if they try to withdraw a negative amount or zero? Add an elif statement checking if the request is less than or equal to 0. If so, print: “Invalid amount”. You must withdraw more than “R0”.

5. Otherwise (else), print: “Declined. Insufficient funds”'''

def withdarawalSimulator():
  balance = 500.90
  withdrawal_amount = float(input('Enter how much you would like to withdraw: '))

  if 0 < withdrawal_amount < balance:
    print(f'Withdrawal successful! \nRemaining balance: Ksh {round(balance - withdrawal_amount, 2)}')
  elif withdrawal_amount <= 0:
    print('Invalid amount! \nAmount must be greater that Ksh 0.')
  else:
    print('Declined! \nInsufficient Funds.')
withdarawalSimulator()