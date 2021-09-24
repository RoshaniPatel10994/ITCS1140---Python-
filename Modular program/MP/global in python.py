your_name = str()
def PrintName():
    global your_name
    print("My name is: ", your_name)
    your_name = "Bob"
    
def main():
    #declaring the global variable
    global your_name
    #getting your_name from the user
    your_name = input("Enter your name:  ")
    #call the print name function
    PrintName()
    print("Current Value of your_name:  ", your_name)
    #calling main
    
main()
