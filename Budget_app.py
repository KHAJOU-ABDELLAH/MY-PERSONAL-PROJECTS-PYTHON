class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    def deposit (self, amount, description=""):
        value_to_append={"amount":amount, "description":description}
        self.ledger.append(value_to_append)
    def withdraw (self, amount, description=""):
        if self.check_funds(amount):
            self.deposit(-amount, description)
            return True
        return False
    def get_balance(self):
      summation = 0
      for i in self.ledger:
            summation +=i["amount"]
      return summation
    def transfer(self, amount, target):
      if self.check_funds(amount):
        self.withdraw(amount, f"Transfer to {target.name}")
        target.deposit(amount, f"Transfer from {self.name}")
        return True
      return False
    def check_funds(self, amount):
      return (amount <= self.get_balance())
    def __str__(self):
      output=[]
      title=self.name.center(30, "*")
      output.append(title)
      for i in self.ledger:
        output.append(i["description"][:23].ljust(23)+f"{i['amount']:.2f}".rjust(7))
      output.append(f"Total: {self.get_balance():.2f}")
      return "\n".join(output)

def create_spend_chart(categories):
    withdrawals=[]
    names=[]
    for j in categories:
      names.append(j.name)
      summ=0
      for i in j.ledger:
          if i["amount"] < 0:
            summ += -i["amount"]
      withdrawals.append(summ)
          
    maxi=len(max(names, key=len))
    names = [x.ljust(maxi) for x in names]
    lines=[]
    for j in range(maxi):
      lines.append("".join(["     " + names[x][j]+"  " if x==0 else names[x][j]+"  "
       for x in range(len(names))]))
    total_withdrawals = sum(withdrawals)
    if total_withdrawals > 0:
      percentages = [
      (int((x / sum(withdrawals)) * 100) // 10) * 10 
      for x in withdrawals
  ]
    else:
      percentages = [0] * len(withdrawals)
    final_lines=["Percentage spent by category"]
    for i in range(100, -10, -10):
      temp=[f"{i:>3}"+"| "]
      for j in range(len(categories)):
        if percentages[j]>=i:
          temp.append("o  ")
        else:
          temp.append("   ")
      final_lines.append("".join(temp))
    final_lines.append("    " +(3*len(categories)+1)*"-")
    final_lines.extend(lines)
    return "\n".join(final_lines)

