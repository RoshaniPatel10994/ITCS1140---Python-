rocksdays = int()
weeks = 0
total = int()
days = 0
rocks = int()

for weeks in range(0, 2):
    for days in range(0, 7):
        rocks = int(input(" Enter the rocks you collected todays: "))+rocks
        print("You collected: ", rocks, " rocks today")
    weeks = weeks+ days
    
    print(" You collected: ", rocks, " rocks this week.")
    
      
        
    
