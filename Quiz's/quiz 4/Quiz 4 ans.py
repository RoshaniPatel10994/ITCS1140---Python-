def main():
#define variables
    numorders = int()
    amt = int()
    coupon = str()
#getinputs   
    numorders = int(input("Enter number of orders: "))
    amt = int(input("Enter total spent: "))
#call function
    CalcCoupon(numorders, amt)

#define function
def CalcCoupon(numorders, amt):
#logic determine order
    if numorders >= 6:
#logic determine coupon
        if amt >=10 and amt <=20:
            coupon = "Customer Coupon: 10% off coupon"
        elif amt >20 and amt <=30:
            coupon = "Customer Coupon: 20% off coupon"
        elif amt>30:
            coupon = "Customer Coupon: 30% off coupon"
        else:
            coupon = "Customer Coupon: no coupon"
    else:
        coupon = "Customer Coupon: no coupon"
#print output
    print(coupon)

#define main
main()
