days = int()
def Rainfall(days):
  rain_log = float()
  rain_log = []
  dayss=int(days)
  for I in range (0,dayss):
    rain_log.append(float(input()))
  return(rain_log)
                    
def main():
  days = int()
  days = int(input())
  myRain = [0.0] * days 
  myRain = Rainfall(days)
  print(myRain) 
main()
