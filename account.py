class BankAccount:
  bank = "Barclays"
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    self.balance = 0
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
acc1 = BankAccount("Betty", "Njambi")
acc2 = BankAccount("Ivy", "Hellen")
acc1.deposit(100)
acc2.deposit(50)
acc1.deposit(75)
acc2.deposit(100)
acc1.withdraw(20)
acc2.withdraw(-500)
acc1.withdraw(30)
acc2.withdraw(-5)
print(acc2.get_balance())
print(acc1.get_balance())
print(acc2.account_name())
print(acc1.account_name())
