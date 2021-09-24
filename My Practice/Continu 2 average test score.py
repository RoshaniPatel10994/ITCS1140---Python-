#Demonstration of Continu
#variables
test_score = float()
total_test = float()
avg_test = float()
counter = int()
counter = 1
while counter <= 3:
    test_score = float(input("Enter a test score:  "))
    if test_score < 0:
        continue
    print(test_score)
    total_test = total_test + test_score
    print(total_test)
    counter = counter + 1
#end loop
avg_test = total_test/3
print("Your average is:  ", format(avg_test, '.2f'))
halt = input
()
