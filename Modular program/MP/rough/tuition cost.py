def GetTuition(rate):
  percredithour = 100
  tution = float()
  for count in range(0, 10):
    if count == 0:
      tution = 12 * percredithour
    else:
      tution = 12 * (percredithour + (percredithour * rate))
      tution = round(tution, 2)
      percredithour += percredithour * rate
      #percredithour = round(percredithour, 2)
  return tution

newrate = float()
tution = float()
percredithour = float()


newrate = float(input())
tution = float(input())
percredithour = float(input())


gettution = GetTuition(newrate)
print(gettution)
