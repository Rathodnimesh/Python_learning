import udf

while True:

    print("**********")
    print("1.odd/even")
    print("2.max of two number")
    print("3.max of three number")
    print("4.prime number")
    print("5.fibonacci series")
    print("6.Exit")
    print("**********")

    choice=int(input("Enter your choice:"))
    if choice==1:
        n1=int(input("Enter Your number:"))
        print("**********")
        udf.oddeven(n1)

    elif choice==2:
         n1=int(input("Enter your number:"))
         n2=int(input("Enter your number:"))
         print("**********")
         udf.maxoftwo(n1,n2)

    elif choice==3:
         n1=int(input("Enter your number:"))
         n2=int(input("Enter your number:"))
         n3=int(input("Enter your number:"))
         print("**********")
         udf.maxofthree(n1,n2,n3)

    elif choice==4:
          n1=int(input("Enter your number:"))
          print("**********")
          udf.prime(n1)

    elif choice==5:
          n13=int(input("Enter your number:"))
          print("**********")
          udf.fibonacci(n13)

    elif choice==6:
           print("Thank You for using!")
           print("**********")
           
    else:
           print("Invaild choice.please try again")
           print("******")
           



         
