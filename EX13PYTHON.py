m = float(input("enter a number : "))
n = float(input("enter another number : "))
if ( m >= 0 and n >= 0 ) or ( m <= 0 and n <= 0) :
    k = m
    m= n
    n = k
    print("the first number is : " , m)
    print("the other number is : " , n)
else :
    print ("the sum is : " , m + n)
    print ("the multiplication is : ", m * n)
