from utils import print_message, get_size, order_latte

def coffee_bot():
  print('Welcome to the cafe!')

  order_drink = ""
  drinks = []

  while True:
    size = get_size()  
    drink_type = get_drink_type()
    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))
    drinks.append(drink)
    order_drink = input("Would you like to order another drink? (y/n) ")
    if order_drink == 'y':
      pass
    elif order_drink == "n":
      break
    else:
      print_message()
      order_drink = input("Would you like to order another drink? (y/n) ")
      
  
  name = input('Can I get your name please? \n> ')
  
  if len(drinks) > 1:
    print("Okay, so I have:")
    for drink in drinks:
      print(f"- {drink}")
    print('Thanks, {}! Your order will be ready shortly.'.format(name))
  else:
    print('Thanks, {}! Your order will be ready shortly.'.format(name))

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')

  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return order_mocha()
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()
  
# Define new functions here!
def order_mocha():
  while True:
    res = input('Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time! \n> ')
    if res.lower() == "a":
      return "peppermint mocha"
    elif res.lower() == "b":
      return "mocha"
    else:
      print_message()


coffee_bot()
