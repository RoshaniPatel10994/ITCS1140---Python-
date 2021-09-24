
class NetPay:
    #constructor to set hours and rate
    def __init__(self, hours,rate):
        self.hours=hours
        self.rate=rate

    #Method that returns the net pay
    def GetNetPay(self):
      netpay=self.GetGrossPay()-self.GetDeductions()
      return netpay

    # Method that returns the gross pay
    def GetGrossPay(self):
      grossPay = self.hours*self.rate
      return grossPay

    # Method that returns the deductions
    def GetDeductions(self):
      deductions=self.GetGrossPay()*0.35
      return deductions

#set hours and rate
hours=20
rate=15
#create an object of NetPay class with hours and rate
netpay=NetPay(hours,rate)
#Print hours and rate
print('Number of hours : ',hours)
print('Rate /Hour : ',rate)
#Print gross pay ,deductions and net pay
print('\nGross Pay: ',netpay.GetGrossPay())
print('Deductions: ',netpay.GetDeductions())
print('Net pay : ',netpay.GetNetPay())
