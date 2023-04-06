#create nested loop
i = 1
# Stock contains:
#   25 nickels
#   25 dimes
#   25 quarters
#   0 ones
#   0 fives

  #intro
print("Welcome to the vending machine change maker program")
print("Change maker initialized.")
  #intial stock commit
n_stock = 25
d_stock = 25
q_stock = 25
o_stock = 0
f_stock = 0
print('Stock contains:\n', f'  {n_stock} nickels\n', f'  {d_stock} dimes\n', f'  {q_stock} quarters\n', f'  {o_stock} ones\n', f'  {f_stock} fives')
print()
while True:
  purchase_price = input('Enter the purchase price (xx.xx) or `q\' to quit: ')
  if purchase_price == 'q':
    print('Stock_contains:\n', f' {n_stock} nickels\n', f' {d_stock} dimes\n', f' {q_stock} quarters\n', f' {o_stock} ones\n', f' {f_stock} fives')
    break
  # elif float(purchase_price) * 100 < 0 or ((
  #  (float(purchase_price)) * 100) % 5) != 0:
  #  print('Illegal price: Must be a non-negative multiple of 5 cents.')
  else:
    try:
      purchase_price = float(purchase_price)
      if 100.0 * (float(purchase_price)) % 5 != 0 or 100.0 * (float(purchase_price)) < 0:
        print('Illegal price: Must be a non-negative multiple of 5 cents. \n')
      else:
        break
    except:
      print('Invalid purchase price. Try again')
      continue

n = 'deposit a nickel'
d = 'deposit a dime'
q = 'deposit a quarter'
o = 'deposit a one dollar bill'
f = 'deposit a five dollar bill'
c = 'cancel the purchase'
print()
deposit_values = {
      'n': float(0.05),
      'd': float(0.10),
      'q': float(0.25),
      'o': float(1.00),
      'f': float(5.00)
    }
deposit_menu = [n, d, q, o, f, c]
    #    print(deposit_menu)
    #Menu for deposits:
    #  'n' - deposit a nickel
    #  'd' - deposit a dime
    #  'q' - deposit a quarter
    #  'o' - deposit a one dollar bill
    #  'f' - deposit a five dollar bill
    #  'c' - cancel the purchase
print('Menu for deposits:\n', f' \'n\' - {n}\n', f' \'d\' - {d}\n', f' \'q\' - {q}\n', f' \'o\' - {o}\n', f' \'f\' - {f}\n', f' \'c\' - {c}\n')
deposit = input("Indicate your deposit: ")
deposit_math = 0
purchase_price = int(round(float(purchase_price) * 100))
purchase_price_var = purchase_price
while True:
  if deposit == 'n':
    purchase_price_var -= 5
    print("Payment due:",
          int(purchase_price_var) // 100, "dollars and",
          int(purchase_price_var) % 100, "cents")
    n_stock += 1
    deposit_math += 5
    if purchase_price_var == 0:  #exact payment deposited
      print('No change.')
      break
    if purchase_price_var < 0:
      print('Pause!')
      break
    deposit = input("Indicate your deposit: ")
  elif deposit == 'd':
    purchase_price_var -= 10
    print("Payment due:",
          int(purchase_price_var) // 100, "dollars and",
          int(purchase_price_var) % 100, "cents")
    d_stock += 1
    if purchase_price_var == 0:  #exact payment deposited
      print('No change.')
      break
    if purchase_price_var < 0:
      print('Pause!')
      break
    deposit = input("Indicate your deposit: ")
    deposit_math += 10 
  elif deposit == 'q':
        purchase_price_var -= 25
        print("Payment due:",
              int(purchase_price_var) // 100, "dollars and",
              int(purchase_price_var) % 100, "cents")
        q_stock += 1
        if purchase_price_var == 0:  #exact payment deposited
          print('No change.')
          break
        if purchase_price_var < 0:
          print('Pause !')
          break
        deposit = input("Indicate your deposit: ")
        deposit_math += 25
  elif deposit == 'o':
    purchase_price_var -= 100
    print("Payment due:",
          int(purchase_price_var) // 100, "dollars and",
          int(purchase_price_var) % 100, "cents")
    o_stock += 1
    if purchase_price_var == 0:  #exact payment deposited
      print('No change.')
      break
    if purchase_price_var < 0:
      print('Pause !')
      break
    deposit_math += 100
    deposit = input("Indicate your deposit: ")
  elif deposit == 'f':
    purchase_price_var -= 500
    print("Payment due:",
          int(purchase_price_var) // 100, "dollars and",
          int(purchase_price_var) % 100, "cents")
    f_stock += 1
    if purchase_price_var == 0:  #exact payment deposited
      print('No change.')
      break
    if purchase_price_var < 0:
      print('Pause !')
      break
    deposit_math += 500
    deposit = input("Indicate your deposit: ")
  elif deposit == 'c':
    print("Please take the change below.")
    q_new = deposit_math // 25
    if q_stock - q_new < 0:
        q_return = q_stock
    q_stock = q_stock - q_new
    deposit_math = deposit_math - q_new * 25
    #print(quarters, "quarters")
    d_new = deposit_math // 10
    if d_stock - d_new < 0:
        d_new = dimes
    d_stock = d_stock - d_new
    deposit_math = deposit_math - d_new * 10
    n_new = deposit_math // 5
    if n_stock - n_new < 0:
      n_new = n_stock
    n_stock = n_stock - n_new
    deposit_math = deposit_math - n_new * 5
    if q_new > 0:
      print(' ', q_new, ' quarters')              
    if d_new > 0:
      print(' ', d_new, ' dimes')           
    if n_new > 0:
      print(' ', n_new, ' nickels')
    print("Stock contains:\n  ", q_stock, "quarters\n  ", d_stock, "dimes\n  ", n_stock, "nickels\n  ", o_stock, "ones\n  ", f_stock, "fives\n  ")
    break
  elif purchase_price_var == 0.00:
    print('No change.')
    break
  elif purchase_price_var < 0:
    print()
  else:  #illegal input
    print("Illegal selection:", deposit)
    print("Payment due:",
          int(purchase_price_var) // 100, "dollars and",
          int(purchase_price_var) % 100, "cents")
    deposit = input("Indicate your deposit: ")
    continue
