import math

class Category:

  def __init__(self, category_name):
    self.category_name = category_name
    self.ledger = []

  def deposit(self, amount, description=""):   
    self.ledger.append({"amount":amount, "description":description})

  def withdraw(self, amount, description=""):
    #if balance > amount withdrawn - add to ledger
    if self.check_funds(amount):
      self.ledger.append({"amount":(0-amount), "description":description})
      return True
    else:  
      return False

  def get_balance(self):
    balance = 0.00
    for tx in self.ledger:
      balance = balance + tx.get("amount")
    return balance

  def check_funds(self, amount):
    bal = self.get_balance()
    ret = True
    if (amount > bal):
      ret = False
    return ret

  def transfer(self, amount, target_category):
    w_description = "Transfer to "+target_category.category_name
    d_description = "Transfer from "+self.category_name

    if self.check_funds(amount):
      self.withdraw(amount, w_description)
      target_category.deposit(amount, d_description)
      return True
    else:
      return False

  def get_totalwithdrawals(self):
    balance = 0.00
    for tx in self.ledger:
      if tx.get("amount") < 0:
        balance = balance + tx.get("amount")
    return abs(balance)    

  def __str__(self):
    to_str = self.category_name.center(30, '*')+"\n"
    for tx in self.ledger:
      desc = (tx.get("description")[:23]).ljust(23, ' ')
      amt = "{:.2f}".format(tx.get("amount")).rjust(7, ' ') 
      to_str += desc+amt+"\n"
    bal = "{:.2f}".format(self.get_balance())
    to_str += "Total: "+str(bal)
    return to_str


def create_spend_chart(categories):
  title = "Percentage spent by category\n"
  total = 0
  cat_list = []
  full_str = ''
  max_label_len = 0

  for category in categories:
    total += category.get_totalwithdrawals()

  for category in categories:
    if max_label_len == 0 or len(category.category_name) > max_label_len:
      max_label_len = len(category.category_name)
    percent = math.floor(((category.get_totalwithdrawals() / total)*100) / 10)*10
    cat_list.append({"name": category.category_name, "percent": percent})

  #construct max length for rows
  #max digits (100 = 3), + pipe, + categories*3, + 1 extra space
  max_len_full = 3+1+(3*len(categories))+1
  max_len_yaxis = 4

  #bar graph area with y-label
  top_str = title
  brackets = ['100', '90', '80', '70', '60', '50', '40', '30', '20', '10', '0']
  for bracket in brackets:
    
    top_str += bracket.rjust(3, ' ')+'|'
    for cat in cat_list:
      if cat.get("percent") >= int(bracket):
        top_str += ' o '
      else:
        top_str += '   '
    top_str += ' \n'

  #middle
  dash_str = (''.rjust(3*len(categories)+1, '-')).rjust(max_len_full, ' ')

  #bottom/x-label
  bottom_str = ''
  for x in range(0, max_label_len):
    bottom_str += '\n'+''.rjust(max_len_yaxis, ' ')
    for cat in cat_list:
      n = cat.get("name")
      if len(n) > x:
        bottom_str += ' '+n[x]+' '
      else:
        bottom_str += '   '
    bottom_str += ' '

  full_str = top_str + dash_str + bottom_str

  return full_str




    


  
