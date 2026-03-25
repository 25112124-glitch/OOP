#1
print("+ - - - - + - - - - +")
for grid_2 in range(1,3):
    for grid_2_1 in range(1,5):
        print("|         |         |")
    print("+ - - - - + - - - - +")

#2
def grid_4_1():
        print("+ - - - - "*4,end="+\n")
def grid_4_2():
       for line1 in range(1,5):
           print("|         "*4,end="|\n")
for grid_4 in range(1,5):
     grid_4_1()
     grid_4_2()
grid_4_1()

