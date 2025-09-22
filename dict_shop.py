cart = []

dict = int(input("pick which dicionary you want, 1 2 or 3. Or do you want to proceed to checkout: "))

while dict == 1 or 2 or 3:

    if dict == 1:
     print("this is the, animals dictonary it cost $15 it is 150 pages")
     opt = input("do you want it, yes or no: ")
     opt = str(opt)
     if opt == "yes":
         cart.append(dict)
         nxt = input("do you want to continue shopping , view cart, or proceed to checkout")
         if nxt == "continue shopping":
                break
         elif nxt == "view cart":
             print(f"this is your cart, dict{cart}")
             break

     elif opt == "no":
         print("restart procces")
     else:
          print("i dont understand your terminology, make sure youre not using caps")

    if dict == 2:
     print("this is the, russian dictonary it cost $100 it is 5000 pages")
     opt = input("do you want it, yes or no: ")
     opt = str(opt)
     if opt == "yes":
         input("do you want to continue shopping , view cart, or proceed to checkout")
     elif opt == "no":
         print("restart procces")
     else:
          print("i dont understand your terminology, make sure youre not using caps")
    
    if dict == 3:
     print("this is the, websters dictonary it cost $9 it is 960 pages")
     opt = input("do you want it, yes or no: ")
     opt = str(opt)
     if opt == "yes":
         input("do you want to continue shopping , view cart, or proceed to checkout")
     elif opt == "no":
         print("restart procces")
     else:
          print("i dont understand your terminology, make sure youre not using caps")
