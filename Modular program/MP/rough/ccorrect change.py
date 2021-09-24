def GetChanges(pennies, nickles, dimes, quarters):
      cents = int()
      cents =  cents+ pennies
      cents = nickles + nickles * 5
      cents =dimes + dimes * 10
      cents = quarters + quarters * 25
      if cents >= 100:
        return "CONGRATULATIONS"
      else:
        return "TRY AGAIN"

newpennies = int()
newnickles = int()
newdimes = int()
newquarters= int()
cents = int()

newpennies = int(input())
newnickles = int(input())
newdimes = int(input())
newquarters= int(input())

cents = GetChanges(newpennies, newnickles, newdimes, newquarters)
print(cents)


    
