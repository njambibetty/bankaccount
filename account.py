from datetime import datetime
class Account:     #baseclass
  #bank = "Barclays"


  def __init__(self, first_name, last_name, phone_number):
    self.first_name = first_name
    self.last_name = last_name
    self.balance = 0
    self.phone_number = phone_number
    self.bank= bamk
    self.deposits = []
    self.withdrawals= []
    self.loan = 0
    #self.loan_repayments = []

       # derived classes 
    class BankAccount(Account):
      def __init__(self, first_name, last_name, phone_number, bank):
        self.bank = bank
        super().__init__(first_name, last_name, phone_number)
    
    class MobileMoneyAccount(Account):
      def __init__(self, first_name, last_name, phone_number, service_provider):
        self.service_provider = service_provider
        super().__init__(first_name, last_name, phone_number)
    
    

  def account_name(self):
    name = "{} account for {} {}".format(
      self.bank, self.first_name, self.last_name)
    return name


  def deposit(self,amount):
    try:
      amount + 1
    except TypeError:
      print("You must enter the amount in figures")
      return
    else:
      self.balance += amount
      time = datetime.now()
      deposit = {
        "time": "time",
        "amount": "amount"
      }
      self.deposits.append(deposit)
      formatted_time = time.strftime("%H:%M%p , %d/%m/%Y")
      print("You have deposited {} to {}".format(amount, self.account_name()))

  def withdraw(self,amount):
    try:
      amount + 1
    except TypeError:
      print("You must enter the amount in figures")
      return
    if amount <= 0:
      print("You cannot withdraw zero or negative")
    elif amount > self.balance:
       print("You don't have enough balance")
    else:
      self.balance -= amount
      time = datetime.now()
      withdrawal = {
        "time":"time",
        "amount": "amount"
      }
      self.withdrawals.append(withdrawal)
      formatted_time = time.strftime("%H:%M%p , %d/%m/%Y")
      print("You have withdrawn {} from {}".format(amount, self.account_name()))

  def get_balance(self):
    return "The balance for {} is {}".format(self.account_name(), self.balance)

  def get_formatted_time(self, time):
    return time.strftime("%A, %drd %B %Y, %H:%M %p")
  
  def show_deposit_statements(self,amount):
     for deposit in self.deposits:
       time = deposit['time']
       formatted_time = self.get_formatted_time(time)
       amount = deposit['amount']
       statement  = "You deposited {} on {}".format(amount, formatted_time)
       print(statement)

  def show_withdrawals_statement(self):
    for withdrawal in self.withdrawals:
      time = datetime.now()
      formatted_time = self.get_formatted_time(time)
      amount= withdrawal['amount']
      statement = "You withdrew {} on {}".format(amount, formatted_time)
      print(withdrawal)

  def request_loan(self,amount):
    try:
      amount + 10
    except TypeError:
      print("You must enter the amount in figures")
      return
    if amount <= 0:
        print("You cannot request a loan of that amount")
    else:
        self.loan = amount
        print("You have been given a loa of {}".format(amount))

  def repay_loan(self,amount):
    try:
      amount + 10
    except TypeError:
      print("Enter the repayment in figures")
      return
    if amount <= 0:
      print("You cannot repay with that amount")
    elif amount < self.loan:
        print("You don't have a loan at the moment")
    else:
        self.loan -= amount
        time = datetime.now()
        repayments = {
          "time": time,
          "amount": amount
        }
        self.loan_repayments.append(repayment)
        #formatted_time = time.strftime("%H:%M%p , %d/%m/%Y")
        print("You have repaid your loan with {}.Your loan  balance is {}".format(amount,self.loan),"formatted_time")

  def loan_repayment_statement(self):
    for repayment in self.loan_repayments:
      time = repayment['time']
      amount = repayment['amount']
      formatted_time = self.get_formatted_time(time)
      statement = "You repaid {} on {}".format(amount, formatted_time)
      print(statement)

  class BankAccount(Account):
    def __init__(self, first_name, last_name, phone_number, bank):
        self.bank = bank
        super().__init__(first_name, last_name, phone_number)

  class MobileMoneyAccount(Account):
    def __init__(self, first_name, last_name, phone_number, service_provider):
        self.service_provider  = service_provider
        self.airtime = []
        self.paybill = []
        self.send = []
        self.receive = []
        super().__init__(first_name, last_name, phone_number, service_provider)
  
    def buy_airtime(self,amount):
      try:
        amount + 1
      except TypeError:
        print("You must enter the amount in figures")
        return
      if amount > self.balance:
        print("You don't have enough balance. Your balace is {}".format(self.balance))
      else:
        self.balance -= amount
        time = datetime.now()
        airtime = {
          "time": "time"
          "airtime":  "amount"
        }
        self.airtime.append(airtime)
        print("You have bought airtime worth {} on {}".format(amount,self.get_formatted_time(time)))

    def pay_paybill(self,amount):
      try:
        amount + 1
      except TypeError:
        print("You must enter  your pin number")
        return
      if amount > self.balance:
        print("Transaction successful. Your balance is {}".format(self.balance))
      else:
        self.balance -= amount
        time = datetime.now()
        """
        paybill = {
        "time": "time",
        "amount": "amount"
        }
        self.paybill.append(paybill)
        """
        print("You paid {} Ksh on {}".format(amount, self.get_formatted_time(time)))

    def send_money(self,amount):
     try:
      amount + 1
     except TypeError:
      print("You must enter the amount in figures")
      return
     if amount > self.balance:
      print("Transaction successful. Your  new balance is {}".format(self.balance))
     else:
      self.balance -= amount
      time = datetime.now()
      """
      send = {
        "time": "time",
        "amount": "amount"
      }
      """
      self.send.append(money)
      print("You sent {} Ksh on {}".format(amount, self.get_formatted_time(time)))


    def receive_money(self,amount):
      try:
        amount + 1
      except TypeError:
        print("You must enter the amount in figures")
        return
      if amount > self.balance:
        print("Transaction successful. Your  new balance is {}".format(self.balance))
      else:
        self.balance -= amount
        time = datetime.now()
        """
        receive = {
        "time": "time",
        "amount":"" amount"
        }
        """
        self.receive.append(receive)
        print("You've received {} Ksh on {}".format(amount, self.get_formatted_time(time)))




                  #exception and error handling ,datetime and class inheritance