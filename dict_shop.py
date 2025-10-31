store=[
    {
        "name": "Animals dict.",
         "price": 14.99,
        "page count": 150
    },
    {
        "name": "cars dict.",
        "price": 19.99,
        "page count": 300
    },
    {
        "name": "russian dict.",
        "price": 49.99,
        "page count": 980
    }
]
cart = []
cartp = 0
for index, item in enumerate(store):
    print(index, ":", item["name"], index, ":", item["price"])
while True:
    dict = int((input("pick which dicionary you want, 0 1 or 2: ")))
    ch = store[dict]
    cart.append(ch["name"])
    cartp += ch["price"]
    print(cart,cartp)

    pc = input("want to proceed to checkout: ")
    if "proceed" in pc.lower or "yes" in pc.lower:
        print(f"you have {cart} in your cart, and it costs {cartp}")
    elif "no" in pc:
        continue










































































#      dict = (input("pick which dicionary you want, 1 2 or 3. Or do you want to proceed to checkout: "))

#     if dict in ["1", "2", "3"]:

#             if dict == "1":
#                 print("this is the, animals dictonary it cost $14.99 it is 150 pages")
#                 opt = input("do you want it, yes or no: ")
#                 opt = str(opt)

#                 if opt == "yes":
#                     cart.append(store["name"])
#                     price.append(dict_1["price"])
#                     nxt = input("do you want to continue shopping , view cart, or proceed to checkout: ")
#                     if nxt == "continue shopping":
#                         continue
#                     elif nxt == "view cart":
#                         print(f"this is your cart, dict{cart}, is costs {sum(price)}")
#                         continue
#                     elif nxt == "proceed to checkout":
#                         print(f"the price comes out to {sum(price)}, now pay")
#                         break

#                 elif opt == "no":
#                     continue
                    
#                 else:
#                     print("i dont understand your terminology, make sure youre not using caps")

#             if dict == "2":
#                 print("this is the, cars dictonary it cost $19.99 it is 300 pages")
#                 opt = input("do you want it, yes or no: ")
#                 opt = str(opt)


#                 if opt == "yes":
#                     cart.append(dict_2["name"])
#                     price.append(dict_2["price"])
#                     nxt = input("do you want to continue shopping , view cart, or proceed to checkout: ")
#                     if nxt == "continue shopping":
#                         continue
#                     elif nxt == "view cart":
#                         print(f"this is your cart, dict{cart}, is costs {sum(price)}")
#                         continue
#                     elif nxt == "proceed to checkout":
#                         print(f"the price comes out to {sum(price)}, now pay")
#                         break

#                 elif opt == "no":
#                     continue
                    
#                 else:
#                     print("i dont understand your terminology, make sure youre not using caps")
#             if dict == "3":
#                 print("this is the, Russian dictonary it cost $49.99 it is 980 pages")
#                 opt = input("do you want it, yes or no: ")
#                 opt = str(opt)


#                 if opt == "yes":
#                     cart.append(dict_3["name"])
#                     price.append(dict_3["price"])
#                     nxt = input("do you want to continue shopping , view cart, or proceed to checkout: ")
#                     if nxt == "continue shopping":
#                         continue
#                     elif nxt == "view cart":
#                         print(f"this is your cart, dict{cart}, is costs {sum(price)}")
#                         continue
#                     elif nxt == "proceed to checkout":
#                         print(f"the price comes out to {sum(price)}, now pay")
#                         break

#                 elif opt == "no":
#                     continue
                    
#                 else:
#                     print("i dont understand your terminology, make sure youre not using caps")
#     elif dict == "proceed to checkout":
#             print(f"the price comes out to {sum(price)}, now pay")
#             break
# main()