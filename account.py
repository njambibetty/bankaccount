class BankAccount:
  #bank = "Barclays"


  def __init__(self, first_name, last_name, phone_number,bank):
    self.first_name = first_name
    self.last_name = last_name
    self.balance = 0
    self.phone_number = phone_number
    self.bank= bamk
    self.deposits = []
    self.withdrawals= []
    
    

  def account_name(self):
    name = "{} account for {} {}".format(
      self.bank, self.first_name, self.last_name)
    return name

  def deposit(self,amount):
    try:
      amount + 1
    except TypeError:
      print("You must enter the amounnt in figures")
      return
    else:
      self.balance += amount
      self.deposits.append(amount)
      print("You have deposited {} to {}".format(amount, self.account_name))

  def withdraw(self,amount):
    try:
      amount + 1
    except TypeError:
      print("You must enter the amount in figures")
    if amount <= 0:
      print("You cannot withdraw zero or negative")
    elif amount > self.balance:
       print("You don't have enough balance")
    else:
      self.balance -= amount
      self.withdrawals.append(amount)
      print("You have withdrawn {} from {}".format(amount, self.account_names))

  def get_balance(self):
    return "The balance for {} is {}".format(
      self.account_name(), self.balance)
  
  def show_deposit_statements(self,amount):
     for deposit in self.deposits:
       print(deposit)

  def show_withdrawals_statement(self):
    for withdrawal in self.withdrawals:
      print(withdrawal)

  def request_loan(self,amount):
    try:
      amount + 1
    except TypeError:
      print("You must enter the amount in figures")
    if amount <= 0:
      try:
        amount + 1
      except TypeError:
        print("The amount should be in figures")
        return
      print("You cannot request a loan of that amount")
    else:
        self.loan = amount
        print("You have be a given a loan of {}".format(amount))

  def repay_loan(self,amount):
    try:
      amount + 1
    except TypeError:
      print("The amount should be in figures")
      return
    if amount <= 0:
      print("You cannot repay with that amount")
    elif amount < self.loan:
        print("Your loan is {}, please enter an amount less or equal".format(self.loan))
    else:
        self.loan -= amount
        print("You have repaid your loan with {}.Your loan is {}".format(amount,self.loan))
