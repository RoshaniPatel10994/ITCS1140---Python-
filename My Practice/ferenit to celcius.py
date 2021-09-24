# change this value for a different result


Degree_Fahrenheit = float()
Degree_Celsius = float()
Continue = float()
fahrenheit = float()
while Continue != 'Q':
    Degrees_Fahrenheit = float(input("Degrees Fahrenheit:"))
    #Degree_Fahrenheit = (Degree_Fahrenheit * 9/5) + 32
    Degree_Celsius = ((Degree_Fahrenheit - 32) * 5/9)
   
 
    print("Degrees Fahrenheit:", str(Degrees_Fahrenheit))
    print("Degrees Celsius: ", str(Degree_Celsius))
    
    Continue = input("Continue Q :")
    
