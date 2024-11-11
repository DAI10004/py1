def print_multiplication_table():
    for i in range(9,0,-1):
        for j in range(1,i+1):
            print(f"{i}*{j}={i*j:2}",end=" ")
        print("")
    print("\n\n")
    for i in range(1,10):
        for j in range(1,i+1):
            print(f"{i}*{j}={i*j:2}",end=" ")
        print("")

print_multiplication_table()
