N = []
f = list(input("put in the rocks that you want 1-100: "))
x = 1

if {f(x)} % 2 == 0 :
    N.append(f)
    x + 1
elif f % 2 != 0 :
    N.clear()
    x + 1


print(sum(N))