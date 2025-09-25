cart = []
def main():
    while True:
        dict = int(input("pick which dicionary you want, 1 1 or 1. Or do you want to proceed to checkout: "))

        if dict == 1 or 2 or 3:

            if dict == 1:
                print("this is the, animals dictonary it cost $15 it is 150 pages")
                opt = input("do you want it, yes or no: ")
                opt = str(opt)
                dict_1{
                    "name": ""


                }

                if opt == "yes":
                    cart.append(dict_1)
                    nxt = input("do you want to continue shopping , view cart, or proceed to checkout")
                    if nxt == "continue shopping":
                        continue
                elif nxt == "view cart":
                    print(f"this is your cart, dict{cart}")
                    continue

                elif opt == "no":
                    continue
                    
                else:
                    print("i dont understand your terminology, make sure youre not using caps")
main()
