for i in range(7):
    for j in range(i+1):
        if j == 0 or i == 6 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()