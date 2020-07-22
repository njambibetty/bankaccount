class BankAccount:
  bank = "Barclays"


  def __init__(self, first_name, last_name,phone_number):
    self.first_name = first_name
    self.last_name = last_name
    self.balance = 0
    self.phone_number = phone_number
    
  def account_name(self):
    name = "{} account for {} {}".format(
      self.bank, self.first_name, self.last_name)
    return name
  def deposit(self,amount):
    if amount > 0:
     self.balance += amount
     print("You have deposited {} to your account".format(amount))
    else:
      print("Kindly,you cannot deposit {} to your account".format(amount))
  def withdraw(self,amount):
    if amount > 0:
     self.balance -= amount
     print("You have withdrawn {} from your account".format(amount))
    else:
      print("Kindly,you cannot withdraw {} from your account".format(amount))
  def get_balance(self):
    return "The balance for {} is {}".format(
      self.account_name(), self.balance)
