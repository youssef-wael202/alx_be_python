row = 10
i = 1
while i <= row :
    spaces = row - i
    j = 1
    while j <= spaces :
        print(" ", end="")
        j += 1
    k = 1
    while k <= (2 * i - 1) :
        print("*", end="")
        k += 1
    print()
    i += 1